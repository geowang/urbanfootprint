from footprint.main.models.geospatial.db_entity import DbEntity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.base.cpad_holdings_feature import  CpadHoldingsFeature
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.client.configuration.fixture import RegionFixture
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.intersection import Intersection

__author__ = 'calthorpe_associates'

class DemoDbEntityKey(DbEntityKey):

    # DEMO region datasets
    CPAD_HOLDINGS = 'cpad_holdings'
    # DEMO project datasets
    PROJECT_EXISTING_LAND_USE_PARCELS = 'project_existing_land_use_parcels'
    # DEMO scenario datasets
    EXISTING_LAND_USE_PARCELS = 'existing_land_use_parcels'

class DemoKumquatCountyRegionFixture(RegionFixture):

    def default_remote_db_entities(self):
        """
            Add the any background imagery. This function is called from default_db_entities so it doesn't
            need to call the parent_fixture's method
        """
        return self.parent_config_entity_fixture.default_remote_db_entities()

    def default_db_entities(self):
        """
            Region specific db_entity_setups
        :param default_dict:
        :return:
        """

        config_entity = self.config_entity
        parent_region_fixture = self.parent_fixture
        default_db_entities = parent_region_fixture.default_db_entities()
        # The DbEntity keyspace. These keys have no prefix
        Key = DemoDbEntityKey

        # remote_db_entity_setups = map(
        #     lambda remote_setup: update_or_create_db_entity(config_entity, **remote_setup),
        #     self.default_remote_db_entities())
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return default_db_entities + [
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.CPAD_HOLDINGS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CpadHoldingsFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            ))
        ]

    def default_db_entity_permissions(self, **kwargs):
        return self.parent_fixture.default_db_entity_permissions(**kwargs)

