from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.client.configuration.fixture import GlobalConfigFixture
from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.main.lib.functions import map_dict
from footprint.main.models.keys.permission_key import PermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from django.conf import settings
__author__ = 'calthorpe_associates'


class DefaultGlobalConfigFixture(DefaultMixin, GlobalConfigFixture):

    def feature_class_lookup(self):
        return {}

    def default_remote_db_entities(self):
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        mapbox_layers = {
            'Aerial Photo': {"id": "elevan.kib62d92", "key": "mapbox_aerial"},
            'Simple Streets': {"id": "elevan.e53fa071", "key": "mapbox_streets"}
        }

        mapbox_base_url = "https://{{S}}.tiles.mapbox.com/v4/{id}/{{Z}}/{{X}}/{{Y}}.png?access_token={api_key}"

        mapbox_setups = map_dict(
            lambda name, attrs: DbEntity(
                key="mapbox_" + attrs['key'],
                name=name,
                url=mapbox_base_url.format(id=attrs['id'], api_key=settings.MAPBOX_API_KEY),
                hosts=["a", "b", "c", "d"],
                schema=self.config_entity,
                no_feature_class_configuration=True,
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('remote_imagery')
                ),
            ),
            mapbox_layers)

        cloudmade_setups = [DbEntity(
            key='osm_default',
            name='Open Street Maps',
            url="http://a.tile.openstreetmap.org/{Z}/{X}/{Y}.png",
            hosts=["a.", "b.", "c.", ""],
            schema=self.config_entity,
            no_feature_class_configuration=True,
            feature_behavior=FeatureBehavior(
                behavior=get_behavior('remote_imagery')
            ),
        )]
        return mapbox_setups + cloudmade_setups

    def default_db_entities(self):
        """
            Only the remote imagery DbEntities belong to the GlobalConfig
        :return:
        """
        config_entity = self.config_entity
        remote_db_entity_configurations = self.default_remote_db_entities()
        return map(
            lambda remote_db_entity_configuration: update_or_create_db_entity(
                config_entity,
                remote_db_entity_configuration),
            remote_db_entity_configurations)

    def default_config_entity_groups(self, **kwargs):
        """
            The Admin is the ConfigEntity Group of the GlobalConfig
        :param kwargs:
        :return:
        """
        return [UserGroupKey.ADMIN]

    def default_db_entity_permissions(self, **kwargs):
        """
            By default Admins and above can edit GlobalConfig-owned DbEntities. Everyone else can view them
        :param kwargs:
        :return:
        """
        return {UserGroupKey.ADMIN: PermissionKey.ALL,
                UserGroupKey.PLANNER: PermissionKey.VIEW}

    def import_db_entity_configurations(self, **kwargs):
        return []
