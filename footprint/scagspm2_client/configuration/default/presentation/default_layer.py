import logging
from footprint.client.configuration.fixture import LayerConfigurationFixture
from footprint.client.configuration.default.default_mixin import DefaultMixin

from footprint.main.publishing.layer_initialization import LayerLibraryKey, LayerMediumKey, LayerSort, LayerTag
from footprint.main.publishing.tilestache_style_configuration import create_style_template, create_template_context_dict_for_parent_model
from footprint.client.configuration.utils import resolve_fixture
from footprint.main.models.built_form.built_form import BuiltForm
from footprint.main.models.config.scenario import Scenario
from footprint.main.models.presentation.medium import Medium
from footprint.main.models.presentation.layer_selection import LayerSelection
from footprint.main.models.config.scenario import FutureScenario, BaseScenario
from footprint.main.models.geospatial.feature import Feature
from footprint.main.models.presentation.presentation_configuration import LayerConfiguration, PresentationConfiguration, ConfigurationData
from footprint.main.models.tag import Tag
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'

logger = logging.getLogger(__name__)

class DefaultLayerConfigurationFixtures(DefaultMixin, LayerConfigurationFixture):
    def layer_libraries(self, layers=None):
        """
           Returns a PresentationConfiguration for each LayerLibrary scoped to self.config_entity.
           The instance will be saved to the LayerLibrary as a foreign key, so it is persisted at that time.
           Each instance contains LayerConfiguration instances that match it's config_entity class scope
        :return:
        """
        # Just make a Scenario scoped configuration
        return [
            PresentationConfiguration(
                # The default LayerLibrary configuration for all scenarios
                scope=self.config_entity.schema(),
                key=LayerLibraryKey.DEFAULT,
                name='{0} Default Library',  # format with config_entity name
                description='The default layer library for {0}',  # format with config_entity name
                data=ConfigurationData(
                    presentation_media_configurations=FixtureList(layers or self.layers()).matching_scope(
                        class_scope=self.config_entity and self.config_entity.__class__)
                )
            )
        ]

    def background_layers(self):
        """
            Background layers are simple references to their corresponding db_entities.
        :return:
        """
        return map(
            lambda db_entity: LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=db_entity.key,
                visible=db_entity.key=='google_map',
                tags=[Tag.objects.get(tag=LayerTag.BACKGROUND_IMAGERY)],
                sort_priority=LayerSort.BACKGROUND),
            # Backgound DbEntities must already exist at this point
            self.config_entity.computed_db_entities(no_feature_class_configuration=True, url__startswith='http'))

    def layers(self):
        """
            Returns LayerConfigurations that are scoped to a certain LayerLibrary key
        :return:
        """

        return FixtureList(self.background_layers()).matching_scope(class_scope=self.config_entity.__class__) +\
               (self.parent_fixture.layers() if self.ancestor_config_entity else [])

    def import_layer_configurations(self):
        """
            Generic LayerConfigurations for db_entity layers imported into the system.
        """
        return FixtureList([
            LayerConfiguration(
                scope=FutureScenario.__name__,
                # Use Feature for the template key so we match the default Feature
                # style files
                is_template_layer_configuration=True,
                style_class=Feature,
                layer_library_key=LayerLibraryKey.DEFAULT,
                visible=True,
                visible_attributes=['wkb_geometry'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}},
                sort_priority=LayerSort.FUTURE,
                # This is meant to be replaced by the imported db_entity_key
                # It serves to uniquely identify the LayerConfiguration
                # so that it can be overridden by client configurations
                db_entity_key='default_future_scenario_layer_configuration'
            ),
            LayerConfiguration(
                scope=BaseScenario.__name__,
                # Use Feature for the template key so we match the default Feature
                # style files
                is_template_layer_configuration=True,
                style_class=Feature,
                layer_library_key=LayerLibraryKey.DEFAULT,
                visible=True,
                visible_attributes=['wkb_geometry'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}},
                sort_priority=LayerSort.BASE,
                # This is meant to be replaced by the imported db_entity_key
                # It serves to uniquely identify the LayerConfiguration
                # so that it can be overridden by client configurations
                db_entity_key='default_base_scenario_layer_configuration'
            )
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)

    def update_or_create_media(self, config_entity, db_entity_keys=None):
        """
            Iterates through the LayerConfiguration and creates Template instances for each that contain default
            styling for the configured attributes
        :return:
        """

        # Find the corresponding config_entity_fixture, or parent fixture if it doesn't exist
        layer_fixture = resolve_fixture(
            "presentation",
            "layer",
            LayerConfigurationFixture,
            config_entity.schema(),
            config_entity=config_entity)

        # Filter by db_entity key if db_entity_keys are specified
        layer_configurations = filter(
            lambda layer_configuration: layer_configuration.db_entity_key in db_entity_keys if db_entity_keys else True,
                   layer_fixture.layers() + layer_fixture.import_layer_configurations()
        )

        # Create a default Medium for any layer that doesn't need a Template
        Medium.objects.update_or_create(key=LayerMediumKey.DEFAULT)

        logger.debug("Start Default Layer Initialization for ConfigEntity %s. Processing Layer Configurations" % config_entity.name)
        for layer_configuration in layer_configurations:
            logger.debug("Default Layer Initialization. Processing Layer of db_entity_key %s" % layer_configuration.db_entity_key)

            try:
                # DbEntities with no backing feature_class_configuration, such as background layers, need not have styles
                no_feature_class_configuration = not layer_configuration.is_template_layer_configuration \
                                                 and config_entity.computed_db_entities(key=layer_configuration.db_entity_key)[0].no_feature_class_configuration
            except IndexError:
                 raise Exception('No DbEntity with key {key} found for ConfigEntity {config_entity}'.format(key=layer_configuration.db_entity_key, config_entity=config_entity))
            style_class = layer_configuration.style_class or \
                          (not no_feature_class_configuration and
                          config_entity.db_entity_feature_class(layer_configuration.db_entity_key, abstract_class=True))
            if style_class:
                logger.debug("Updating/Creating style template for layer of db_entity_key %s" % layer_configuration.db_entity_key)
                template = create_style_template(
                    layer_configuration.template_context_dict,
                    layer_configuration.db_entity_key,
                    # The template key is based on the configured feature class or the DbEntity
                    # If no feature_class exists the db_entity_key is used
                    # Some layer configurations use styled_class to force a certain class upon
                    # which to base their template names (namely the generic layer_configurations)
                    # used for importing new feature tables
                    style_class,
                    *layer_configuration.visible_attributes)
                logger.debug("Updated/Created style template for layer of db_entity_key %s with template id key %s" %
                             (layer_configuration.db_entity_key, template.key))
            elif not no_feature_class_configuration:
                raise Exception("No styling is configured for DbEntity key %s. No tilestache layer can be created." %
                                layer_configuration.db_entity_key)

        if not db_entity_keys:
            # Creates the Template for LayerSelection instances
            styled_class = LayerSelection
            # This is a magic attribute of tilestache indicating the features that match a query
            # TODO we don't style layer selections with cartocss.
            # Is this being used on the front end with css/polymaps?
            styled_attribute = 'selected'
            default_context = {
                'htmlClass': None,
                'attributes': {
                    styled_attribute: {
                        'equals': {
                            'TRUE': {"outline": {"color": "#3cff00"}, },
                        },
                    }
                }
            }
            create_style_template(default_context, None, styled_class, styled_attribute)
        logger.debug("End Default Layer Initialization")


def built_form_template_context_dict():
    """
        Create the template_context_dict based on the built_form_id attribute
    :return:
    """

    return create_template_context_dict_for_parent_model(
        BuiltForm, lambda built_form: built_form.medium.content if built_form.medium else None, 'built_form'
    )



