from footprint.client.configuration.fixture import UserFixture
from footprint.main.models.keys.user_group_key import UserGroupKey

__author__ = 'calthorpe'

class DemoUserFixture(UserFixture):
    def users(self, **kwargs):
        # A sample user who belongs to the client ConfigEntity's director group
        # This user therefore has full permission to all config_entities of the demo client
        return [
            dict(groups=[self.config_entity.user_group_name(UserGroupKey.DIRECTOR)],
                 # Easy to test name
                 username='_'.join([self.config_entity.key, 'user']),
                 password='demo',
                 email='demo@demo.demo')
        ]
