from footprint.client.configuration.fixture import LayerConfigurationFixture
from footprint.client.configuration.mixins.publishing.layer_primary_base import primary_base_template_context_dict
from footprint.client.configuration.demo.built_form.demo_land_use_definition import DemoLandUseDefinition
from footprint.client.configuration.demo__kumquat_county.config_entity.demo__kumquat_county_region import DemoDbEntityKey
from footprint.main.models.config.scenario import Scenario
from footprint.main.models.presentation.presentation_configuration import LayerConfiguration
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class DemoKumquatCountyLayerConfigurationFixtures(LayerConfigurationFixture):
    def layer_libraries(self, layers=None):
        return self.parent_fixture.layer_libraries(
            FixtureList(self.layers()).matching_scope(class_scope=self.config_entity and self.config_entity.__class__))

    def layers(self):
        # Combine parent fixture layers with the layers matching the given ConfigEntity scope
        return self.parent_fixture.layers() + FixtureList([
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=DemoDbEntityKey.EXISTING_LAND_USE_PARCELS,
                visible=True,
                visible_attributes=['land_use_definition__id'],
                column_alias_lookup=dict(land_use_definition__id='land_use_definition_id'),
                built_form_set_key='demo_land_uses',
                template_context_dict=primary_base_template_context_dict(DemoLandUseDefinition)
            ),
        ]).matching_scope(class_scope=self.config_entity.__class__)

    def import_layer_configurations(self):
        return self.parent_fixture.import_layer_configurations()
