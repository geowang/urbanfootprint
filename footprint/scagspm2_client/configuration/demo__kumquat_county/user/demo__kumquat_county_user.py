from footprint.client.configuration.fixture import UserFixture
from footprint.main.models.config.region import Region
from footprint.main.models.config.project import Project
from footprint.main.models.config.scenario import Scenario
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe'

class DemoKumquatCountyUserFixture(UserFixture):
    def users(self, **kwargs):
        return FixtureList(
            # A Region level user for the county
            [dict(groups=[self.config_entity.user_group_name(UserGroupKey.DIRECTOR)],
                  class_scope=Region,
                  username='kumkuat_director',
                  password='kumkuat_director@uf',
                  email=''),
             # A Project level user for each city
             dict(groups=[self.config_entity.user_group_name(UserGroupKey.MANAGER)],
                  class_scope=Project,
                  # User name is [city]_manager
                  username='_'.join([self.config_entity.key, 'manager']),
                  password='%s@uf' % self.config_entity.key,
                  email='')] +
            # A Few Scenario-level user for each city
            map(lambda i: dict(groups=[self.config_entity.user_group_name(UserGroupKey.PLANNER)],
                               class_scope=Scenario,
                               # User name is [city]_planner_[i]
                               username='_'.join([self.config_entity.parent_config_entity.key, 'planner', str(i)]),
                               password='%s@uf' % self.config_entity.parent_config_entity.key,
                               email=''), range(1, 3))
        ).matching_scope(class_scope=self.config_entity.__class__, delete_scope_keys=True)
