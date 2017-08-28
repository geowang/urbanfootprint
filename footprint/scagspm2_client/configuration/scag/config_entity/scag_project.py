from footprint.client.configuration.fixture import ProjectFixture
from footprint.client.configuration.scag.config_entity.scag_config_entities import ScagDbEntityKey
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class ScagProjectFixture(ProjectFixture):

    def default_db_entities(self):
        """
            Project specific SCAG additional db_entities
        :param default_dict:
        :return:
        """
        project = self.config_entity
        # The DbEntity keyspace. These keys have no prefix
        Key = ScagDbEntityKey
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return self.parent_fixture.default_db_entities() + map(
            lambda db_entity_dict: update_or_create_db_entity(project, db_entity_dict['value']),
            FixtureList([
                # dict(
                #     value=DbEntity(
                #         key=Key.PROJECT_EXISTING_LAND_USE_PARCELS,
                #         feature_class_configuration=FeatureClassConfiguration(
                #             abstract_class=ExistingLandUseParcel,
                #             import_from_db_entity_key=Key.REGION_EXISTING_LAND_USE_PARCELS,
                #             filter_query=dict(city=project.name),
                #             primary_geography=True,
                #             primary_key='source_id',
                #             primary_key_type='int',
                #             fields=dict(),
                #             related_fields=dict(land_use_definition=dict(
                #                 single=True,
                #                 related_class_name='footprint.client.configuration.scag.built_form.scag_land_use_definition.ScagLandUseDefinition',
                #                 related_class_join_field_name='land_use',
                #                 source_class_join_field_name='lu12')
                #             )
                #         ),
                #         feature_behavior=FeatureBehavior(
                #             behavior=get_behavior('editable_feature')
                #         )
                #     )
                # )
            ]))
