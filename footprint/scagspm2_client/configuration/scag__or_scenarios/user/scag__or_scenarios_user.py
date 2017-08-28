from footprint.client.configuration.fixture import UserFixture
from footprint.main.models.config.scenario import Scenario
from footprint.main.models.config.project import Project
from footprint.main.models.config.region import Region
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe'

class ScagOrScenariosUserFixture(UserFixture):
    def users(self, **kwargs):
        return FixtureList(
            # A Region level user for the county
            [dict(groups=[self.config_entity.user_group_name(UserGroupKey.DIRECTOR)],
                 class_scope=Region,
                 username='orange_director',
                 password='orange_director@uf',
                 email=''),
            # A Project level user for each city
            dict(groups=[self.config_entity.user_group_name(UserGroupKey.MANAGER)],
                 class_scope=Project,
                 # User name is [city]_manager
                 username='_'.join([self.config_entity.key, 'manager']),
                 password='%s@uf' % self.config_entity.key,
                 email='')] +
            # A Few Scenario-level user for each city. This will be the same user for every scenario in a project
            map(lambda i: dict(
                 # Make sure to include the groups of all sibling scenarios. Even if they haven't all been
                 # created yet, the final scenario will capture all scenario groups
                 groups=map(
                    lambda scenario: scenario.user_group_name(UserGroupKey.PLANNER),
                    self.config_entity.parent_config_entity.children()
                 ),
                 class_scope=Scenario,
                 # User name is [city]_planner_[i]
                 username='_'.join([self.config_entity.parent_config_entity.key, 'planner', str(i)]),
                 password='%s@uf' % self.config_entity.parent_config_entity.key,
                 email=''), range(1, 4))
        ).matching_scope(class_scope=self.config_entity.__class__, delete_scope_keys=True)
