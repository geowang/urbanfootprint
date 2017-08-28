from footprint.client.configuration.sacog.base.sacog_light_rail_stops_half_mile_feature import \
    SacogLightRailStopsHalfMileFeature
from footprint.client.configuration.sacog.base.sacog_light_rail_stops_feature import SacogLightRailStopsFeature
from footprint.client.configuration.sacog.base.sacog_light_rail_stops_one_mile_feature import \
    SacogLightRailStopsOneMileFeature
from footprint.client.configuration.sacog.base.sacog_light_rail_stops_quarter_mile_feature import \
    SacogLightRailStopsQuarterMileFeature
from footprint.client.configuration.sacog.base.sacog_light_rail_feature import SacogLightRailFeature
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.client.configuration.fixture import RegionFixture
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.intersection import Intersection
from footprint.main.publishing.config_entity_initialization import get_behavior
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class SacogDbEntityKey(DbEntityKey):
    EXISTING_LAND_USE_PARCEL_SOURCE = 'existing_land_use_parcels'
    STREAM = 'streams'
    VERNAL_POOL = 'vernal_pools'
    WETLAND = 'wetlands'
    HARDWOOD = 'hardwoods'
    LIGHT_RAIL = 'light_rail'
    LIGHT_RAIL_STOPS = 'light_rail_stops'
    LIGHT_RAIL_STOPS_ONE_MILE = 'light_rail_stops_one_mile'
    LIGHT_RAIL_STOPS_HALF_MILE = 'light_rail_stops_half_mile'
    LIGHT_RAIL_STOPS_QUARTER_MILE = 'light_rail_stops_quarter_mile'


class SacogRegionFixture(RegionFixture):

    def default_remote_db_entities(self):
        """
            Add the SACOG background. This function is called from default_db_entities so it doesn't
            need to call the parent_fixture's method
        """
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate

        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return [
            DbEntity(
                key='sacog_background',
                url="http://services.sacog.org/arcgis/rest/services/Imagery_DigitalGlobe_2012WGS/MapServer/tile/{Z}/{Y}/{X}",
                no_feature_class_configuration=True,
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('remote_imagery')
                )
            )
        ]

    def default_db_entities(self):
        """
        Region specific SACOG db_entity_setups
        :param default_dict:
        :return:
        """

        config_entity = self.config_entity
        parent_region_fixture = self.parent_fixture
        default_db_entities = parent_region_fixture.default_db_entities()
        Key = SacogDbEntityKey

        if self.config_entity.key=='sacog':
            # Block the client-level region. We just want real regions
            return []

        remote_db_entity_setups = map(
            lambda db_entity: update_or_create_db_entity(config_entity, db_entity), self.default_remote_db_entities())

        return default_db_entities + remote_db_entity_setups + FixtureList([
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.LIGHT_RAIL,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogLightRailFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.LIGHT_RAIL_STOPS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogLightRailStopsFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.LIGHT_RAIL_STOPS_ONE_MILE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogLightRailStopsOneMileFeature,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.LIGHT_RAIL_STOPS_HALF_MILE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogLightRailStopsHalfMileFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.LIGHT_RAIL_STOPS_QUARTER_MILE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SacogLightRailStopsQuarterMileFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            ))
        ])

