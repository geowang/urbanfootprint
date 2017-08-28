from footprint.client.configuration.default.default_mixin import DefaultMixin
from footprint.client.configuration.fixture import UserFixture

__author__ = 'calthorpe'

class DefaultUserFixture(DefaultMixin, UserFixture):
    def groups(self, **kargs):
        return []

    # There are no default users, but global_user.py has global-level users
    def users(self, **kargs):
        return []

