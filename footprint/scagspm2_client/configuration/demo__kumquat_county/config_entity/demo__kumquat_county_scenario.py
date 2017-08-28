from footprint.client.configuration.demo.base.existing_land_use_parcel import ExistingLandUseParcel
from footprint.client.configuration.demo__kumquat_county.config_entity.demo__kumquat_county_region import \
    DemoDbEntityKey
from footprint.main.models.config.scenario import BaseScenario
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.client.configuration.fixture import ScenarioFixture, project_specific_project_fixtures
from footprint.main.models.geospatial.db_entity import DbEntity
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.feature_class_creator import FeatureClassCreator
from footprint.main.lib.functions import merge
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class DemoKumquatCountyScenarioFixture(ScenarioFixture):

    def feature_class_lookup(self):
        # Get the client project fixture (or the default region if the former doesn't exist)
        project = merge(*map(
            lambda project_fixture: project_fixture.feature_class_lookup(),
            project_specific_project_fixtures(config_entity=self.config_entity)))
        return merge(
            project,
            FeatureClassCreator(self.config_entity).key_to_dynamic_model_class_lookup(self.default_db_entities())
        )

    def default_db_entities(self):
        """
            Project specific SCAG additional db_entities
        :param default_dict:
        :return:
        """
        project = self.config_entity.parent_config_entity_subclassed

        scenario = self.config_entity
        # The DbEntity keyspace. These keys have no prefix
        Key = DemoDbEntityKey
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return super(DemoKumquatCountyScenarioFixture, self).default_db_entities() + map(
            lambda db_entity_dict: update_or_create_db_entity(scenario, db_entity_dict['value']),
            FixtureList([
                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=DemoDbEntityKey.EXISTING_LAND_USE_PARCELS,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=ExistingLandUseParcel,
                            import_from_db_entity_key=Key.PROJECT_EXISTING_LAND_USE_PARCELS,
                            filter_query=dict(city=project.name),
                            primary_geography=True,
                            primary_key='source_id',
                            primary_key_type='int',
                            fields=dict(),
                            related_fields=dict(land_use_definition=dict(
                                single=True,
                                related_class_name='footprint.client.configuration.demo.built_form.demo_land_use_definition.DemoLandUseDefinition',
                                related_class_join_field_name='land_use',
                                source_class_join_field_name='lu12')
                            )
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature')
                        )
                    )
                ),
            ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
        )

    def default_db_entity_permissions(self, **kwargs):
        return self.parent_fixture.default_db_entity_permissions(**kwargs)
