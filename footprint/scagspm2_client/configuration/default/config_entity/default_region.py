from footprint.client.configuration.fixture import RegionFixture, GlobalConfigFixture
from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.utils import resolve_fixture
from footprint.main.lib.functions import merge
from footprint.main.models.keys.permission_key import PermissionKey, DbEntityPermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class DefaultRegionFixture(DefaultMixin, RegionFixture):

    def feature_class_lookup(self):
        # Get the client global_config fixture (or the default region if the former doesn't exist)
        client_global_config = resolve_fixture("config_entity", "global_config", GlobalConfigFixture)
        global_config_feature_class_lookup = client_global_config.feature_class_lookup()
        return merge(global_config_feature_class_lookup, {})

    def default_db_entities(self):
        """
            Region define DbEntities specific to the region.
            Currently there are none.
        """
        return self.default_remote_db_entities()

    def default_config_entity_groups(self, **kwargs):
        """
            Instructs Regions to create a UserGroup for directors of this region.
            The group will be named config_entity.schema()__UserGroupKey.DIRECTOR
        :param kwargs:
        :return:
        """
        return [UserGroupKey.DIRECTOR]

    def default_db_entity_permissions(self, **kwargs):
        """
            By default only Admins can edit Region-owned DbEntities and approve Feature changes.
            Everyone else can view them
        :param kwargs:
        :return:
        """
        return {UserGroupKey.DIRECTOR: DbEntityPermissionKey.ALL,
                UserGroupKey.PLANNER: PermissionKey.VIEW}

    def import_db_entity_configurations(self, **kwargs):
        return FixtureList([])
