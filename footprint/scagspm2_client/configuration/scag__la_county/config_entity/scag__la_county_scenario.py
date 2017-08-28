from footprint.client.configuration.scag.base.scenario_planning_zones import ScenarioPlanningZones
from footprint.client.configuration.scag.base.existing_land_use_parcel import ExistingLandUseParcel
from footprint.client.configuration.scag.base.general_plan_parcels import GeneralPlanParcels
from footprint.client.configuration.scag.base.jurisdiction_boundary import JurisdictionBoundary
from footprint.client.configuration.scag.base.sphere_of_influence import SphereOfInfluence
from footprint.client.configuration.scag.base.tier2_taz import Tier2Taz
from footprint.client.configuration.scag.config_entity.scag_config_entities import ScagDbEntityKey
from footprint.main.models.config.scenario import BaseScenario
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.client.configuration.fixture import ScenarioFixture, project_specific_project_fixtures
from footprint.main.models.geospatial.db_entity import DbEntity
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.feature_class_creator import FeatureClassCreator
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.lib.functions import merge
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class ScagLaCountyScenarioFixture(ScenarioFixture):

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
            Scenarios define DbEntsaities specific to the Scenario. Creates a list a dictionary of configuration functionality.
            These are filtered based on whether the given scenario matches the scope in the configuration
        :return:
        """
        project = self.config_entity.parent_config_entity_subclassed

        scenario = self.config_entity
        # The DbEntity keyspace. These keys have no prefix
        Key = ScagDbEntityKey
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return super(ScagLaCountyScenarioFixture, self).default_db_entities() + map(
            lambda db_entity_dict: update_or_create_db_entity(scenario, db_entity_dict['value']),
            FixtureList([

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.EXISTING_LAND_USE_PARCELS,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=ExistingLandUseParcel,
                            import_from_db_entity_key=Key.PROJECT_EXISTING_LAND_USE_PARCELS,
                            primary_geography=True,
                            primary_key='source_id',
                            primary_key_type='int',
                            fields=dict(),
                            related_fields=dict(land_use_definition=dict(
                                single=True,
                                related_class_name='footprint.client.configuration.scag.built_form.scag_land_use_definition.ScagLandUseDefinition',
                                related_class_join_field_name='land_use',
                                source_class_join_field_name='lu12')
                            )
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature')
                        )
                    )
                ),

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.GENERAL_PLAN_PARCELS,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=GeneralPlanParcels,
                            primary_key='source_id',
                            primary_key_type='int',
                            import_from_db_entity_key=Key.REGION_GENERAL_PLAN_PARCELS,
                            filter_query=dict(city=project.name),
                            fields=dict(),
                            related_fields=dict(land_use_definition=dict(
                                single=True,
                                related_class_name='footprint.client.configuration.scag.built_form.scag_land_use_definition.ScagLandUseDefinition',
                                # Use this for the resource type, since we don't want a client-specific resource URL
                                # TODO not wired up yet
                                resource_model_class_name='footprint.main.models.built_form.ClientLandUseDefinition',
                                related_class_join_field_name='land_use',
                                source_class_join_field_name='scag_gp_code')
                            )
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature'),
                            intersection=Intersection(join_type='attribute')
                        )
                    )
                ),

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.SCENARIO_PLANNING_ZONES,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=ScenarioPlanningZones,
                            import_from_db_entity_key=Key.REGION_SCENARIO_PLANNING_ZONES,
                            filter_query=dict(city=project.name),

                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature'),
                            intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                        )
                    )
                ),

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.JURISDICTION_BOUNDARY,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=JurisdictionBoundary,
                            import_from_db_entity_key=Key.REGION_JURISDICTION_BOUNDARY,
                            filter_query=dict(city=project.name),
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature'),
                            intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                        )
                    )
                ),

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.SPHERE_OF_INFLUENCE,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=SphereOfInfluence,
                            import_from_db_entity_key=Key.REGION_SPHERE_OF_INFLUENCE,
                            filter_query=dict(city=project.name),
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('reference'),
                            intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                        )
                    )
                ),

                dict(
                    class_scope=BaseScenario,
                    value=DbEntity(
                        key=Key.TIER2_TAZ,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=Tier2Taz,
                            import_from_db_entity_key=Key.REGION_TIER2_TAZ,
                            filter_query=dict(city=project.name),
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('editable_feature'),
                            intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                        )
                    )
                )
            ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
        )
