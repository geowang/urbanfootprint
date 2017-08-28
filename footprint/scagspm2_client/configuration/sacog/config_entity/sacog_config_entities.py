from footprint.client.configuration.fixture import ConfigEntitiesFixture
from footprint.main.models.config.scenario import BaseScenario, FutureScenario
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.utils.fixture_list import FixtureList
from django.contrib.gis.geos import MultiPolygon, Polygon
__author__ = 'calthorpe_associates'

class SacogConfigEntitiesFixture(ConfigEntitiesFixture):
    def project_key(self):
        return None

    def region_key(self):
        return 'sacog_region'

    def regions(self, region_keys=None, class_scope=None):
        return FixtureList([
            {
                'key': 'sacog_region',
                'name': 'SACOG Region',
                'description': 'The SACOG region',
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
                'key': 'yolo',
                'import_key': 'yolo_county',
                'name':  'Yolo County',
                'description':  "Yolo County",
                'base_year': 2013,
                'region_key': 'sacog_region',
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
                'key': 'base_condition',
                'scope': project.schema(),
                'name': 'Base Condition',
                'description': '{0} Base Scenario {1}'.format('2012', project.name),
                'year': 2012,
                'selections': dict(built_form_sets='sacog_building_type')
            },
            {
                'class_scope': FutureScenario,
                'key': 'scenario_a',
                'scope': project.schema(),
                'name': 'Scenario A',
                'description': 'Future Scenario for {0}'.format(project.name),
                'year': 2050,
                'selections': dict(built_form_sets='sacog_building_type')
            }]).matching_keys(
                    region_key=region_keys,
                    project_key=project.key if project else None,
                    key=scenario_keys).\
                matching_scope(class_scope=class_scope)

