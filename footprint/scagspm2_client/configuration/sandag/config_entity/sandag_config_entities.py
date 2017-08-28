from footprint.client.configuration.fixture import ConfigEntitiesFixture
from footprint.main.models.geospatial.behavior import Behavior
from footprint.main.models.config.scenario import BaseScenario, FutureScenario
from footprint.main.models.category import Category
from footprint.main.models.geospatial.behavior import BehaviorKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'
from django.contrib.gis.geos import MultiPolygon, Polygon


class SandagConfigEntitiesFixture(ConfigEntitiesFixture):
    def regions(self, region_keys=None, class_scope=None):
        return FixtureList([
            {
                'key': 'sandag',
                'name': 'SANDAG',
                'description': 'The San Diego region',
                'bounds': MultiPolygon([Polygon((
                    (-122.719, 37.394),  # bottom left
                    (-122.719, 38.059),  # top left
                    (-121.603, 38.059),  # top right
                    (-121.603, 37.394),  # bottom right
                    (-122.719, 37.394),  # bottom leftsample_config_entities
                ))])
            },
        ]).matching_keys(key=region_keys).matching_scope(class_scope=class_scope)

    def projects(self, region=None, region_keys=None, project_keys=None, class_scope=None):
        return FixtureList([
            {
                'key': 'sandag',
                'name': 'SANDAG Scenarios',
                'description': "The San Diego Region",
                'base_year': 2012,
                'region_key': 'sandag',
                'media': [],
                'bounds': MultiPolygon([Polygon(
                    (
                        # TODO: decide if this needs updating or if it's taken care of by the project method
                        # Sacramento County bounds
                        (-121.862622000787, 38.018420999589),  # bottom left
                        (-121.862622000787, 38.7364049988308),  # top left
                        (-121.027084001338, 38.7364049988308),  # top right
                        (-121.027084001338, 38.018420999589),  # top right
                        (-121.862622000787, 38.018420999589)   # bottom left
                    )
                )])
            }
        ]).matching_keys(region_keys=region_keys, key=project_keys).matching_scope(class_scope=class_scope)

    def scenarios(self, project=None, region_keys=None, project_keys=None, scenario_keys=None, class_scope=None):

        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return FixtureList([
            {
                'class_scope': BaseScenario,
                'key': '{0}_base'.format(project.key),
                'scope': project.schema(),
                'name': 'Base',
                'description': '{0} Base Scenario {1}'.format('2012', project.name),
                'year': 2012,
                'behavior': get_behavior('base_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Base')]
            },

            {
                'class_scope': FutureScenario,
                'key': '{0}_series13'.format(project.key),
                'scope': project.schema(),
                'name': 'Series 13',
                'description': '{0} Future Scenario Series13 for {1}'.format('2050', project.name),
                'year': 2050,
                'behavior': get_behavior('future_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
            {
                'class_scope': FutureScenario,
                'key': '{0}_scenario_a'.format(project.key),
                'scope': project.schema(),
                'name': 'Scenario A',
                'description': '{0} Future Scenario Alternative A for {1}'.format('2050', project.name),
                'year': 2050,
                'behavior': get_behavior('future_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
            {
                'class_scope': FutureScenario,
                'key': '{0}_scenario_b'.format(project.key),
                'scope': project.schema(),
                'name': 'Scenario B',
                'description': '{0} Future Scenario Alternative B for {1}'.format('2050', project.name),
                'year': 2050,
                'behavior': get_behavior('future_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },

            {
                'class_scope': FutureScenario,
                'key': '{0}_scenario_c'.format(project.key),
                'scope': project.schema(),
                'name': 'Scenario C'.format(project.name),
                'description': '{0} Future Scenario Alternative C for {1}'.format('2050', project.name),
                'year': 2050,
                'behavior': get_behavior('future_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
            {
                'class_scope': FutureScenario,
                'key': '{0}_series9'.format(project.key),
                'scope': project.schema(),
                'name': 'Series 9',
                'description': '{0} Future Scenario Series9 for {1}'.format('2050', project.name),
                'year': 2050,
                'behavior': get_behavior('future_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Future')]
            },
        ]).matching_keys(region_key=region_keys, project_key=project.key if project else project_keys, key=scenario_keys).\
           matching_scope(class_scope=class_scope)

