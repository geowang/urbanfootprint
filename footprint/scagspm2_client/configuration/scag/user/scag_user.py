from footprint.client.configuration.fixture import UserFixture
from footprint.main.models.keys.user_group_key import UserGroupKey

__author__ = 'calthorpe'

class ScagUserFixture(UserFixture):
    def users(self, **kwargs):
        # A sample user who belongs to the client ConfigEntity's director group
        # This user therefore has full permission to all config_entities of the demo client
        return [
            dict(groups=[UserGroupKey.DIRECTOR], username='guoxiong', password='UF2014', email='guoxiong@scag.gov'),
            dict(groups=[UserGroupKey.DIRECTOR], username='jungA', password='UF2014', email='jungA@scag.gov'),
            dict(groups=[UserGroupKey.MANAGER], username='scag_user1', password='scag@uf1', email=''),
            dict(groups=[UserGroupKey.MANAGER], username='scag_user2', password='scag@uf2', email=''),
            dict(groups=[UserGroupKey.MANAGER], username='scag_user3', password='scag@uf3', email=''),
        ]
