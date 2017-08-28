from footprint.client.configuration.default.presentation.default_layer import built_form_template_context_dict
from footprint.client.configuration.fixture import LayerConfigurationFixture
from footprint.client.configuration.mixins.publishing.layer_primary_base import primary_base_template_context_dict
from footprint.client.configuration.scag.built_form.scag_land_use_definition import ScagLandUseDefinition
from footprint.client.configuration.scag.config_entity.scag_config_entities import ScagDbEntityKey
from footprint.main.models.config.scenario import Scenario, FutureScenario
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.presentation.presentation_configuration import LayerConfiguration
from footprint.main.models.tag import Tag
from footprint.main.utils.fixture_list import FixtureList
from footprint.main.publishing.layer_initialization import LayerSort, LayerLibraryKey, LayerTag

__author__ = 'calthorpe_associates'


class ScagOrScenariosLayerConfigurationFixtures(LayerConfigurationFixture):

    def layer_libraries(self, class_scope=None):
        return self.parent_fixture.layer_libraries(
            FixtureList(self.layers()).matching_scope(class_scope=self.config_entity and self.config_entity.__class__))

    def layers(self, class_scope=None):
        # Combine parent fixture layers with the layers matching the given ConfigEntity scope
        return self.parent_fixture.layers() + FixtureList([
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.BASE,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict=built_form_template_context_dict(),
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.ENERGY,
                visible=False,
                visible_attributes=['annual_million_btus_per_unit'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'annual_million_btus_per_unit': {'unstyled': True}}},
                sort_priority=LayerSort.FUTURE+4
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.WATER,
                visible=False,
                visible_attributes=['annual_gallons_per_unit'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                template_context_dict={'attributes': {'annual_gallons_per_unit': {'unstyled': True}}},
                sort_priority=LayerSort.FUTURE+4
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
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.REGION_EXISTING_LAND_USE_PARCELS,
                visible=True,
                visible_attributes=['land_use_definition__id'],
                column_alias_lookup=dict(land_use_definition__id='land_use_definition_id'),
                built_form_set_key='scag_land_uses',
                template_context_dict=primary_base_template_context_dict(ScagLandUseDefinition)
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.REGION_GENERAL_PLAN_PARCELS,
                visible=False,
                visible_attributes=['land_use_definition__id'],
                column_alias_lookup=dict(land_use_definition__id='land_use_definition_id'),
                built_form_set_key='scag_land_uses',
                template_context_dict=primary_base_template_context_dict(ScagLandUseDefinition)
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.REGION_JURISDICTION_BOUNDARY,
                visible=True,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.REGION_SPHERE_OF_INFLUENCE,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.REGION_TIER2_TAZ,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.FLOOD_ZONES,
                visible=False,
                visible_attributes=['flood_zone'],
                template_context_dict={'attributes': {'flood_zone': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.HABITAT_CONSERVATION_AREA,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.CPAD_HOLDINGS,
                visible=False,
                visible_attributes=['layer'],
                template_context_dict={'attributes': {'layer': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.FARMLAND,
                visible=False,
                visible_attributes=['polygon_fy'],
                template_context_dict={'attributes': {'polygon_fy': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.ENDANGERED_SPECIES,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.COUNTY_BOUNDARY,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.TRANSIT_PRIORITY_AREAS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.MAJOR_TRANSIT_STOPS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.HIGH_QUALITY_TRANSIT_AREAS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.HIGH_QUALITY_TRANSIT_CORRIDORS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.CENSUS_TRACTS,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=ScagDbEntityKey.SUB_REGION,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            )
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)

    def import_layer_configurations(self):
        return self.parent_fixture.import_layer_configurations()
