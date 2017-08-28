from django.conf import settings
from django.contrib.auth import get_user_model
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.feature_class_creator import FeatureClassCreator
from footprint.client.configuration.fixture import ProjectFixture, RegionFixture
from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.utils import resolve_fixture
from footprint.main.lib.functions import merge
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.models.keys.permission_key import PermissionKey, DbEntityPermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.publishing.config_entity_initialization import get_behavior
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class DefaultProjectFixture(DefaultMixin, ProjectFixture):

    def feature_class_lookup(self):
        # Get the client region fixture (or the default region if the former doesn't exist)
        client_region = resolve_fixture("config_entity", "region", RegionFixture)
        region_class_lookup = client_region.feature_class_lookup()
        return merge(
            region_class_lookup,
            FeatureClassCreator(self.config_entity).key_to_dynamic_model_class_lookup(self.default_db_entities())
        )

    def default_db_entities(self, **kwargs):
        """
            Projects define DbEntities specific to the Project config_entity instance.
            Each DbEntity configured here should be persisted using update_or_clone_db_entity so that this code
            can be run many times without creating duplicates. The instances configured here are configurations--
            a persisted instance with an id will be returned for each. Similarly the FeatureClassConfiguration
            instances and FeatureBehavior instances configured will be updated or cloned.

            kwargs: overrides can be supplied to override certain values. The override behavior must be hand-crafted
            below
        :return: a dictionary of
        """
        return []

    def default_config_entity_groups(self, **kwargs):
        """
            Instructs Projects to create a UserGroup for managers of this region.
            The group will be named config_entity.schema()__UserGroupKey.MANAGER
        :param kwargs:
        :return:
        """
        return [UserGroupKey.MANAGER]

    def default_db_entity_permissions(self, **kwargs):
        """
            By default Managers and above can edit Project-owned DbEntities and approve Feature updates.
            Planners can edit DbEntity features but cannot approve
            Everyone else can view them
        :param kwargs:
        :return:
        """
        return {
                UserGroupKey.MANAGER: DbEntityPermissionKey.ALL,  # includes APPROVAL permission
                UserGroupKey.PLANNER: PermissionKey.ALL,  # excludes APPROVAL permission
                UserGroupKey.INTERN: PermissionKey.VIEW
        }

    def import_db_entity_configurations(self, **kwargs):
        project = self.config_entity

        return map(
            lambda db_entity_dict: update_or_create_db_entity(project, db_entity_dict['value']),
            FixtureList([
                dict(
                # class_scope=Project,
                value=DbEntity(
                    name='Indian Reservations SCAG 2009 (test)',
                    key='test_indian_reservation_project_import',
                    url='file://%s/indianreservation_scag_2009.zip' % settings.STATIC_ROOT,
                    creator=get_user_model().objects.get(username='admin'),
                    srid=26911,
                    feature_behavior=FeatureBehavior(
                        behavior=get_behavior('reference'),
                        intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                    )
                ))
            ]))



def project_key(name):

    if len(name) < 7:
        return name.lower().replace(' ', '_')

    key_parts = []
    previous = None

    for l in name.lower():
        if l not in ['a', 'e', 'i', 'o', 'u', ' '] and previous != l:
            key_parts.append(l)
            previous = l

    return ''.join(key_parts)
