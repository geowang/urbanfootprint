from django.contrib.auth import get_user_model
from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.fixture import BehaviorFixture
from footprint.main.models.config.db_entity_interest import DbEntity
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe'

class DefaultBehaviorFixture(DefaultMixin, BehaviorFixture):
    def behaviors(self, **kwargs):
        key = BehaviorKey.Fab.ricate
        # This doesn't fetch from the database, since the Behavior being sought might not exist quite yet
        polygon = IntersectionKey.POLYGON

        # Create a special DbEntity used only by Behavior.feature_template_behavior instances
        dummy_user = get_user_model().objects.get(username=UserGroupKey.ADMIN)

        DbEntity.objects.update_or_create(key='template_feature_behavior', defaults=dict(creator=dummy_user, updater=dummy_user))

        return FixtureList([
            Behavior(
                key=key('environmental_constraint'),
                parents=[],
                # Environmental constraints always intersect primary features polygon to polygon
                intersection=Intersection(from_type=polygon, to_type=polygon)
            ),
            # A behavior attributed to Features representing UrbanFootprint base data
            Behavior(
                key=key('reference'),
                parents=[]
            ),
            Behavior(
                key=key('tool'),
                parents=[]
            ),
            # A behavior attributed to a Tool that produces a result from one or more inputs
            Behavior(
                key=key('analysis_tool'),
                parents=['tool']
            ),
            # A behavior attributed to a Tool that performs updates
            Behavior(
                key=key('update_tool'),
                parents=['tool']
            ),
            # A behavior attributed to a Tool that edits features or similar
            Behavior(
                key=key('editor_tool'),
                parents=['tool']
            ),
            # A behavior attributed to Features representing UrbanFootprint base data
            Behavior(
                key=key('editable_feature'),
                parents=[]
            ),
            Behavior(
                key=key('base_feature'),
                parents=[]
            ),
            Behavior(
                key=key('base_agriculture'),
                parents=[]
            ),
            Behavior(
                key=key('scenario_end_state'),
                parents=[]
            ),
            Behavior(
                key=key('scenario_increment'),
                parents=[]
            ),
            Behavior(
                key=key('agriculture_scenario'),
                parents=[]
            ),
            Behavior(
                key=key('developable'),
                parents=[]
            ),
            Behavior(
                key=key('internal_analysis'),
                parents=[]
            ),
            Behavior(
                # Background imagery
                key=key('remote_imagery'),
                parents=[]
            ),
            Behavior(
                # results
                key=key('result'),
                parents=[]
            ),
            Behavior(
                # results
                key=key('master'),
                abstract=True,
                parents=[]
            ),
            Behavior(
                # results
                key=key('draft'),
                abstract=True,
                parents=[]
            ),
            Behavior(
                # results
                key=key('default_config_entity'),
                parents=[]
            ),
            Behavior(
                # results
                key=key('base_scenario'),
                parents=['default_config_entity']
            ),
            Behavior(
                # results
                key=key('future_scenario'),
                parents=['default_config_entity']
            ),
            Behavior(
                # results
                key=key('base_master_scenario'),
                parents=['base_scenario', 'master']
            ),
            Behavior(
                # results
                key=key('base_draft_scenario'),
                parents=['base_scenario', 'draft']
            ),
            Behavior(
                # results
                key=key('future_master_scenario'),
                parents=['future_scenario', 'master']
            ),
            Behavior(
                # results
                key=key('future_draft_scenario'),
                parents=['future_scenario', 'draft']
            )
        ])
