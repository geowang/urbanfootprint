from footprint.client.configuration.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.client.configuration.default.config_entity.default_config_entities import ConfigEntityMediumKey
from django.conf import settings
from footprint.main.models.keys.permission_key import PermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'
from django.contrib.gis.geos import MultiPolygon, Polygon


class DemoConfigEntitiesFixture(ConfigEntitiesFixture):
    def project_key(self):
        return None

    def region_key(self):
        return 'kumquat_county'

    def regions(self, region_keys=None, class_scope=None):
        return FixtureList([
            dict(
                key='kumquat_county',
                name='Kumquat County',
                description='Kumquat County',
                media=[
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('demo_logo'), name='DEMO Logo',
                                    url='/static/client/{0}/logos/demo.png'.format(settings.CLIENT))
                ],
                #defaulting to an Irthorn view for the moment
                bounds=MultiPolygon([Polygon((
                    (-117.869537353516, 33.5993881225586),
                    (-117.869537353516, 33.7736549377441),
                    (-117.678024291992, 33.7736549377441),
                    (-117.678024291992, 33.5993881225586),
                    (-117.869537353516, 33.5993881225586),
                ))])
            )
        ]).matching_keys(key=region_keys).matching_scope(class_scope=class_scope)

    def scenarios(self, project=None, region_keys=None, project_keys=None, scenario_keys=None, class_scope=None):
        return FixtureList([])
