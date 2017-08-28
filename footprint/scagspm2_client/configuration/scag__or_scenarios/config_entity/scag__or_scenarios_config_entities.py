
from footprint.client.configuration.fixture import ConfigEntitiesFixture
from footprint.main.models.config.scenario import BaseScenario, FutureScenario
from django.contrib.gis.geos import MultiPolygon, Polygon
from footprint.main.utils.fixture_list import FixtureList
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior


__author__ = 'calthorpe_associates'



class ScagOrScenariosConfigEntitiesFixture(ConfigEntitiesFixture):


    def projects(self, region=None, region_keys=None, project_keys=None, class_scope=None):
        
        return FixtureList([
            {
                'key': 'or_cnty',
                'import_key': 'or_cnty',
                'name':  'Orange County',
                'description':  "Orange County Scenarios",
                'base_year': 2013,
                'region_key': 'or_scenarios',
                'media': [],
                'bounds': MultiPolygon([Polygon(
                    (
                        (-121.738056, 38.553889),
                        (-121.738056, 38.553889),
                        (-121.738056, 38.553889),
                        (-121.738056, 38.553889),
                        (-121.738056, 38.553889),
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
                'key': 'base',
                'scope': project.schema(),
                'name': 'Base Condition',
                'description': '{0} Base Condition {1}'.format('2012', project.name),
                'year': 2012,
                'selections': dict()
            },
            {
                'class_scope': FutureScenario,
                'key': 'scn_a',
                'scope': project.schema(),
                'name': 'Scenario A',
                'description': 'Future Scenario for {0}'.format(project.name),
                'year': 2050,
                'selections': dict()
            },
            {
                'class_scope': FutureScenario,
                'key': 'scn_b',
                'scope': project.schema(),
                'name': 'Scenario B',
                'description': 'Future Scenario for {0}'.format(project.name),
                'year': 2050,
                'selections': dict()
            }]).matching_keys(
                    region_key=region_keys,
                    project_key=project.key if project else None,
                    key=scenario_keys).\
                matching_scope(class_scope=class_scope)




