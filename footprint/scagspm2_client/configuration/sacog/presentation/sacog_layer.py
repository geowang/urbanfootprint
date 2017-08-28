from footprint.client.configuration.default.presentation.default_layer import built_form_template_context_dict
from footprint.client.configuration.fixture import LayerConfigurationFixture
from footprint.client.configuration.mixins.publishing.layer_primary_base import primary_base_template_context_dict
from footprint.client.configuration.sacog.config_entity.sacog_region import SacogDbEntityKey
from footprint.main.models.config.scenario import FutureScenario, Scenario
from footprint.main.models.presentation.presentation_configuration import LayerConfiguration
from footprint.client.configuration.sacog.built_form.sacog_land_use_definition import SacogLandUseDefinition
from footprint.main.models.tag import Tag
from footprint.main.publishing.layer_initialization import LayerSort, LayerLibraryKey, LayerTag
from footprint.main.utils.fixture_list import FixtureList
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey

__author__ = 'calthorpe_associates'

class SacogLayerConfigurationFixture(LayerConfigurationFixture):

    def layer_libraries(self, class_scope=None):
        return self.parent_fixture.layer_libraries(
            FixtureList(self.layers()).matching_scope(class_scope=self.config_entity and self.config_entity.__class__))

    def layers(self, class_scope=None):

        return self.parent_fixture.layers() + FixtureList([
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.CENSUS_TRACT,
                visible=False,
                visible_attributes=['tract'],
                template_context_dict={'attributes': {'tract': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.CENSUS_BLOCKGROUP,
                visible=False,
                visible_attributes=['blockgroup'],
                template_context_dict={'attributes': {'blockgroup': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.CENSUS_BLOCK,
                visible=False,
                visible_attributes=['block'],
                template_context_dict={'attributes': {'block': {'unstyled': True}}},
                sort_priority=LayerSort.BASE
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                layer_library_key=LayerLibraryKey.DEFAULT,
                db_entity_key=DbEntityKey.BASE,
                visible=False,
                visible_attributes=['built_form__id'],
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
                column_alias_lookup=dict(built_form__id='built_form_id'),
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
                scope=Scenario.__name__,
                db_entity_key=DbEntityKey.BASE_AGRICULTURE,
                visible=False,
                visible_attributes=['built_form__id'],
                column_alias_lookup=dict(built_form__id='built_form_id'),
                built_form_set_key='sacog_rucs',
                tags=[Tag.objects.get(tag=LayerTag.DEFAULT)],
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
                db_entity_key=SacogDbEntityKey.EXISTING_LAND_USE_PARCEL_SOURCE,
                visible=True,
                visible_attributes=['land_use_definition__id'],
                column_alias_lookup=dict(land_use_definition__id='land_use_definition_id'),
                built_form_set_key='sacog_land_use',
                template_context_dict=primary_base_template_context_dict(SacogLandUseDefinition)
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.STREAM,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),
            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.VERNAL_POOL,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.WETLAND,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),

            # LayerConfiguration(
            #     scope=Scenario.__name__,
            #     db_entity_key=SacogDbEntityKey.HARDWOOD,
            #     visible=False,
            #     visible_attributes=['wkb_geometry'],
            #     template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            # ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.LIGHT_RAIL,
                visible=False,
                visible_attributes=['line'],
                template_context_dict={'attributes': {'line': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.LIGHT_RAIL_STOPS,
                visible=False,
                visible_attributes=['color'],
                template_context_dict={'attributes': {'color': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.LIGHT_RAIL_STOPS_ONE_MILE,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.LIGHT_RAIL_STOPS_HALF_MILE,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            ),

            LayerConfiguration(
                scope=Scenario.__name__,
                db_entity_key=SacogDbEntityKey.LIGHT_RAIL_STOPS_QUARTER_MILE,
                visible=False,
                visible_attributes=['wkb_geometry'],
                template_context_dict={'attributes': {'wkb_geometry': {'unstyled': True}}}
            )
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)

    def import_layer_configurations(self):
        return self.parent_fixture.import_layer_configurations()