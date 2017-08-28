__author__ = 'calthorpe_associates'

from footprint.client.configuration.fixture import InitFixture

class SandagInitFixture(InitFixture):
    def import_database(self):
        return dict(
            host='10.0.0.133',
            database='sandag_urbanfootprint',
            user='calthorpe',
            password='Calthorpe123')
    def users(self):
        return  self.parent_fixture.users() + [
            dict(username='pat', password='pat!', email='plandrum@sandag.gov'),
        ]