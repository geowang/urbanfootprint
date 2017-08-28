from django.conf import settings
from footprint.client.configuration.default.config_entity.default_config_entities import ConfigEntityMediumKey
from footprint.client.configuration.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.main.models.category import Category
from footprint.main.models.config.scenario import BaseScenario
from django.contrib.gis.geos import MultiPolygon, Polygon
from footprint.main.models.keys.permission_key import PermissionKey, ConfigEntityPermissionKey
from footprint.main.models.keys.user_group_key import UserGroupKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'

class DemoKumquatCountyConfigEntitiesFixture(ConfigEntitiesFixture):
    def projects(self, region=None, region_keys=None, project_keys=None, class_scope=None):
        return FixtureList([
            dict(
                key='irthorn',
                import_key='irthorn',
                name='City of Irthorn',
                description="City of Irthorn",
                base_year=2012,
                region_key='kumquat_county',
                media=[
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('irthorn_logo'), name='Irthorn Logo',
                                  url='/static/client/{0}/logos/cityofirthorn.png'.format(settings.CLIENT))
                ],
                bounds=MultiPolygon([Polygon((
                    (-117.869537353516, 33.5993881225586),
                    (-117.869537353516, 33.7736549377441),
                    (-117.678024291992, 33.7736549377441),
                    (-117.678024291992, 33.5993881225586),
                    (-117.869537353516, 33.5993881225586),
                ))])
            ),
            dict(
                key='anaburo',
                import_key='anaburo',
                name='City of Anaburo',
                description="City of Anaburo",
                base_year=2012,
                region_key='kumquat_county',
                media=[
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('anaburo_logo'), name='Anaburo Logo',
                                  url='/static/client/{0}/logos/cityofanaburo.png'.format(settings.CLIENT))
                ],
                bounds=MultiPolygon([Polygon((
                    (-117.869537353516, 33.5993881225586),
                    (-117.869537353516, 33.7736549377441),
                    (-117.678024291992, 33.7736549377441),
                    (-117.678024291992, 33.5993881225586),
                    (-117.869537353516, 33.5993881225586),
                ))]),
                group_permission_configuration={
                    UserGroupKey.DIRECTOR: ConfigEntityPermissionKey.ALL,
                    UserGroupKey.PLANNER: PermissionKey.VIEW
                }
            )
        ]).matching_keys(region_keys=region_keys, key=project_keys).matching_scope(class_scope=class_scope)

    def scenarios(self, project=None, region_keys=None, project_keys=None, scenario_keys=None, class_scope=None):
        parent_fixture = self.parent_fixture
        return parent_fixture.scenarios(project, class_scope=parent_fixture.schema) + FixtureList([
            dict(
                class_scope=BaseScenario,
                key='%s_base_condition' % project.key,
                scope=project.schema(),
                name='%s Base Condition' % project.name,
                description='{0} Base Scenario {1}'.format('2012', project.name),
                year=2012,
                selections=dict(),
                categories=[Category(key='category', value='base_year')],
                group_permission_configuration={
                    UserGroupKey.MANAGER: ConfigEntityPermissionKey.ALL,
                    UserGroupKey.PLANNER: PermissionKey.VIEW
                }
            )]).matching_keys(
                region_key=region_keys,
                project_key=project.key if project else project_keys,
                key=scenario_keys,
            ).matching_scope(class_scope=class_scope)





