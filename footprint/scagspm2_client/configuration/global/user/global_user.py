from django.conf import settings
from footprint.client.configuration.fixture import UserFixture
from footprint.main.models.keys.user_group_key import UserGroupKey

__author__ = 'calthorpe'

class GlobalUserFixture(UserFixture):
    def groups(self, **kargs):
        """
        :param kargs:
        :return:
        """
        return [
            dict(name=UserGroupKey.ADMIN),
            dict(name=UserGroupKey.DIRECTOR, superiors=[UserGroupKey.ADMIN]),
            dict(name=UserGroupKey.MANAGER, superiors=[UserGroupKey.DIRECTOR]),
            dict(name=UserGroupKey.PLANNER, superiors=[UserGroupKey.MANAGER]),
            dict(name=UserGroupKey.INTERN, superiors=[UserGroupKey.PLANNER]),
            dict(name=UserGroupKey.GUEST, superiors=[UserGroupKey.INTERN])
        ]

    def users(self, **kargs):
        """
        Here we define admin-level users based on settings.ADMINS.
        Custom users at other permission levels should be
        declared in the UserFixture of the appropriate ConfigEntity. For example,
        users with Region permission should be declared in that region's UserFixture, unless
        the user needs permission to multiple regions, in which case it should probably go here

        :param kwargs:
        :return: A list of dicts representing Users
        """
        def create_admin_dict(admin_tuple):
            # Extract the first name
            name = admin_tuple[0].split(' ')[0].lower()
            return dict(groups=[UserGroupKey.ADMIN],
                        username=name,
                        # Default pw is name@uf
                        # The software should force this to be changed immediately
                        password='%s@uf' % name,
                        email=admin_tuple[1])

        return map(lambda admin_tuple: create_admin_dict(admin_tuple),
                   settings.ADMINS)

