from footprint.main.models.analysis.water_feature import WaterFeature
from footprint.main.models.analysis.energy_feature import EnergyFeature
from footprint.main.models.analysis.vmt_features.vmt_feature import VmtFeature
from footprint.main.models.analysis.vmt_features.vmt_variable_buffer_feature import VmtVariableBufferFeature
from footprint.main.models.analysis.vmt_features.vmt_one_mile_buffer_feature import VmtOneMileBufferFeature
from footprint.main.models.analysis.vmt_features.vmt_quarter_mile_buffer_feature import VmtQuarterMileBufferFeature
from footprint.main.models.analysis.agriculture_feature import AgricultureFeature
from footprint.main.models.future.core_end_state_feature import CoreEndStateFeature
from footprint.main.models.future.core_increment_feature import CoreIncrementFeature
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.analysis.fiscal_feature import FiscalFeature
from footprint.main.models.geospatial.behavior import Behavior, BehaviorKey
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.feature_class_creator import FeatureClassCreator
from footprint.client.configuration.fixture import ScenarioFixture, project_specific_project_fixtures
from footprint.main.lib.functions import merge

from footprint.main.models.config.scenario import FutureScenario, Scenario
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.model_utils import uf_model
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'


class SacogScenarioFixture(ScenarioFixture):

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
            Scenarios define DbEntities specific to the Scenario. Creates a list a dictionary of configuration functionality.
            These are filtered based on whether the given scenario matches the scope in the configuration
        :return:
        """
        scenario = self.config_entity
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return super(SacogScenarioFixture, self).default_db_entities() + map(
            lambda db_entity_dict: update_or_create_db_entity(scenario, db_entity_dict['value']),
            FixtureList([
                dict(
                    class_scope=FutureScenario,
                    value=DbEntity(
                        key=DbEntityKey.INCREMENT,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=CoreIncrementFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            import_ids_only=True,
                            related_fields=dict(built_form=dict(
                                single=True,
                                related_class_name=uf_model('built_form.built_form.BuiltForm')
                            ))
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('scenario_increment'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=FutureScenario,
                    value=DbEntity(
                        key=DbEntityKey.END_STATE,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=CoreEndStateFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            related_fields=dict(built_form=dict(
                                single=True,
                                related_class_name=uf_model('built_form.built_form.BuiltForm')
                            ))
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('scenario_end_state'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=FutureScenario,
                    value=DbEntity(
                        key=DbEntityKey.FUTURE_AGRICULTURE,
                        name='Scenario Agriculture End State',
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=AgricultureFeature,
                            import_from_db_entity_key=DbEntityKey.BASE_AGRICULTURE,
                            import_ids_only=False,
                            related_fields=dict(built_form=dict(
                                single=True,
                                related_class_name=uf_model('built_form.built_form.BuiltForm'),
                                related_class_join_field_name='key',
                                source_class_join_field_name='built_form_key'
                            ))
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('agriculture_scenario'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=FutureScenario,
                    value=DbEntity(
                        key=DbEntityKey.FISCAL,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=FiscalFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.VMT_QUARTER_MILE_BUFFER,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=VmtQuarterMileBufferFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True,
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.VMT_ONE_MILE_BUFFER,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=VmtOneMileBufferFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.VMT_VARIABLE_BUFFER,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=VmtVariableBufferFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.VMT,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=VmtFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.ENERGY,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=EnergyFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                ),
                dict(
                    class_scope=Scenario,
                    value=DbEntity(
                        key=DbEntityKey.WATER,
                        feature_class_configuration=FeatureClassConfiguration(
                            abstract_class=WaterFeature,
                            import_from_db_entity_key=DbEntityKey.BASE,
                            empty_table=True
                        ),
                        feature_behavior=FeatureBehavior(
                            behavior=get_behavior('internal_analysis'),
                            intersection=Intersection(join_type=IntersectionKey.ATTRIBUTE)
                        )
                    )
                )
            ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__))

