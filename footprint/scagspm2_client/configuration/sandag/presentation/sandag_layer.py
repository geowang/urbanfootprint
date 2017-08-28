from footprint.client.configuration.default.presentation.default_layer import built_form_template_context_dict
from footprint.client.configuration.fixture import LayerConfigurationFixture
from footprint.client.configuration.sandag.config_entity.sandag_region import SandagDbEntityKey
from footprint.main.models.config.scenario import Scenario
from footprint.main.models.config.scenario import FutureScenario
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.presentation.presentation_configuration import LayerConfiguration
from footprint.main.models.tag import Tag
from footprint.main.publishing.layer_initialization import LayerLibraryKey, LayerSort, LayerTag
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class SandagLayerConfigurationFixture(LayerConfigurationFixture):
    def layer_libraries(self, layers=None):
        return self.parent_fixture.layer_libraries(
            FixtureList(self.layers()).matching_scope(class_scope=self.config_entity and self.config_entity.__class__))

    def layers(self):
        db_entity_key = DbEntityKey.Fab.ricate

        return self.parent_fixture.layers() + self.matching_scope([
            # The following layers are Used by both BaseScenario and FutureScenario
            LayerConfiguration(
                scope=FutureScenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.DEVELOPABLE,
                visible=False,
                visible_attributes=['developable_index'],
                template_context_dict={'attributes': {'developable_index': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=db_entity_key('census_tract'),
                visible=False,
                # TODO why style tract codes?
                visible_attributes=['tract'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'tract': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=db_entity_key('census_blockgroup'),
                visible=False,
                visible_attributes=['blockgroup'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                # TODO why style blockgroup codes?
                template_context_dict={'attributes': {'blockgroup': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=db_entity_key('census_block'),
                visible=False,
                visible_attributes=['block'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                # TODO why style block codes?
                template_context_dict={'attributes': {'block': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.CPAD_HOLDINGS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.BASE,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.VMT,
                visible=False,
                visible_attributes=['vmt_daily_per_hh'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'vmt_daily_per_hh': {'unstyled': True}}},
                sort_priority=LayerSort.FUTURE+4
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=DbEntityKey.BASE_AGRICULTURE,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                built_form_set_key='sacog_rucs',
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.FUTURE+4
            ),
            LayerConfiguration(
                scope=FutureScenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.INCREMENT,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.FUTURE+1
            ),
            LayerConfiguration(
                scope=FutureScenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.END_STATE,
                visible=True,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.FUTURE+2
            ),
            LayerConfiguration(
                scope=FutureScenario.__name__,
                db_entity_key=DbEntityKey.FUTURE_AGRICULTURE,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                built_form_set_key='sacog_rucs',
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.FUTURE+3

            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SandagDbEntityKey.SCENARIO_A_BOUNDARY,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SandagDbEntityKey.SCENARIO_B_BOUNDARY,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SandagDbEntityKey.SCENARIO_C_BOUNDARY,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SandagDbEntityKey.RTP_TRANSIT_NETWORK_2050,
                visible=False,
                visible_attributes=['transit_mode'],
                template_context_dict={'attributes': {'transit_mode': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SandagDbEntityKey.RTP_TRANSIT_STOPS_2050,
                visible=False,
                visible_attributes=['transit_mode'],
                template_context_dict={'attributes': {'transit_mode': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=SandagDbEntityKey.BASE_PARCEL,
                visible=True,
                visible_attributes=['built_form__id'],
                # The SQL column returned is normally builform_id, so alias it to our expected attribute string
                column_alias_lookup=dict(built_form__id='built_form_id'),
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.FUTURE+1
            )
        ], class_scope=self.config_entity and self.config_entity.__class__)

    def update_or_create_templates(self):
        """
            Delegates to default, which will also create templates for the client's custom layers
        :return:
        """
        self.parent_fixture.update_or_create_templates()

    def import_layer_configurations(self):
        return self.parent_fixture.import_layer_configurations()
