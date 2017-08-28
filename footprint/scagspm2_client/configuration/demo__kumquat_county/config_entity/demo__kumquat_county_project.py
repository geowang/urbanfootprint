from footprint.client.configuration.demo.base.existing_land_use_parcel import ExistingLandUseParcel
from footprint.client.configuration.demo__kumquat_county.config_entity.demo__kumquat_county_region import DemoDbEntityKey
from footprint.main.models.geospatial.attribute_group import AttributeGroup, AttributeGroupKey
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.client.configuration.fixture import ProjectFixture
from footprint.main.models.geospatial.db_entity import DbEntity
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior, AttributeGroupConfiguration
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.keys.permission_key import PermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey

__author__ = 'calthorpe_associates'


class DemoKumquatCountyProjectFixture(ProjectFixture):

    def default_db_entities(self):
        """
            Project specific DEMO additional db_entities
        :param default_dict:
        :return:
        """
        project = self.config_entity
        # The DbEntity keyspace. These keys have no prefix
        Key = DemoDbEntityKey
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))
        # The AttributeGroup keyspace
        attribute_key = AttributeGroupKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_attribute_group = lambda key: AttributeGroup.objects.get(key=attribute_key(key))

        return super(DemoKumquatCountyProjectFixture, self).default_db_entities() + [
            update_or_create_db_entity(project, DbEntity(
                key=Key.PROJECT_EXISTING_LAND_USE_PARCELS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=ExistingLandUseParcel,
                    primary_geography=True,
                    primary_key='source_id',
                    primary_key_type='int',
                    fields=dict(),
                    related_fields=dict(land_use_definition=dict(
                        single=True,
                        related_class_name='footprint.client.configuration.demo.built_form.demo_land_use_definition.DemoLandUseDefinition',
                        # Use this for the resource type, since we don't want a client-specific resource URL
                        # TODO not wired up yet
                        resource_model_class_name='footprint.main.models.built_form.ClientLandUseDefinition',
                        related_class_join_field_name='land_use',
                        source_class_join_field_name='lu12')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('editable_feature'),
                    attribute_group_configurations=[
                        AttributeGroupConfiguration(
                            # For this editable_feature, we need to keep lu12 synced to land_use_definition
                            # whenever the user changes the latter
                            # This AttributeGroup should probably be created automajically by feature_class_configuration.related_fields config
                            attribute_group=get_attribute_group('relation_to_primitive_association'),
                            attribute_mapping=dict(relation='land_use_definition', primitive='lu12'),
                            group_permission_configuration={
                                # Planners and their superiors have all access
                                UserGroupKey.PLANNER: PermissionKey.ALL
                            }
                        ),
                        AttributeGroupConfiguration(
                            # Gives the admin permission to see edit the update and create dates, but nobody else
                            # This is just for testing permissions
                            attribute_group=get_attribute_group('timestamps'),
                            attribute_mapping=dict(created='created', updated='updated'),
                            group_permission_configuration={
                                # Planners and their superiors have all access
                                UserGroupKey.ADMIN: PermissionKey.ALL,
                                # Managers and their superiors can view
                                UserGroupKey.MANAGER: PermissionKey.VIEW
                                # Planners can't view at all :<
                            }
                        )
                    ]
                )
            ))
        ]

    def default_db_entity_permissions(self, **kwargs):
        return self.parent_fixture.default_db_entity_permissions(**kwargs)


