from django.conf import settings

from footprint.client.configuration.default.config_entity.default_config_entities import ConfigEntityMediumKey
from footprint.client.configuration.default.config_entity.default_project import project_key
from footprint.client.configuration.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.main.models.category import Category
from footprint.main.models.config.scenario import BaseScenario
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.utils.fixture_list import FixtureList


__author__ = 'calthorpe_associates'


class ScagLaCountyConfigEntitiesFixture(ConfigEntitiesFixture):
    def projects(self, region=None, region_keys=None, project_keys=None, class_scope=None):
        # all the jurisdictions in LA County
        # jurisdictions = ["Alhambra", "San Marino", "Signal Hill", "Diamond Bar", "Redondo Beach", "Montebello", "Sierra Madre",  "Bell", "Bradbury", "San Gabriel", "West Covina", "Rancho Palos Verdes", "Palos Verdes Estates", "Long Beach", "Carson", "Azusa", "West Hollywood", "South Pasadena", "Rolling Hills", "Huntington Park", "San Dimas", "Covina", "South Gate", "Los Angeles", "Vernon", "Gardena", "Pico Rivera", "Monrovia", "Avalon", "Walnut", "Santa Fe Springs", "Westlake Village", "Artesia", "Hawaiian Gardens", "Hidden Hills", "Commerce", "La Puente", "Inglewood", "Bell Gardens", "Santa Monica", "Monterey Park", "Agoura Hills", "Manhattan Beach", "Compton", "Cerritos", "Lakewood", "Palmdale", "Temple City", "Lynwood", "Baldwin Park", "Downey", "Norwalk", "Lomita", "Santa Clarita", "Cudahy", "Lawndale", "Lancaster", "Industry", "Hermosa Beach", "Beverly Hills"]
        
        # phase 3 has a limited set of jurisdicitons in LA
        jurisdictions = ["Lakewood", "Torrance", "Hermosa Beach", "Los Angeles"]

        # # build with no projects for easier deployments
        # jurisdictions = []

        configurations = map(lambda jurisdiction_name: {
            'key': project_key(jurisdiction_name),
            'import_key': jurisdiction_name.lower().replace(' ', '_'),
            'name': jurisdiction_name,
            'description': "City of %s" % jurisdiction_name,
            'base_year': 2014,
            'region_key': 'la_county',
            'media': [
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate(jurisdiction_name.lower().replace(' ', '_') + '_logo'),
                                  name='%s Logo' % jurisdiction_name,
                                  url='/static/client/{0}/logos/{1}_logo.png'.format(settings.CLIENT, jurisdiction_name.lower().replace(' ', '_')))
                ],
        }, jurisdictions)

        # supporting a legacy build with the hand-typed keys used there
        for c in configurations:
            if c['name'] == 'Torrance':
                c['key'] = 'trnce'
            if c['name'] == 'Lakewood':
                c['key'] = 'lkwd'
            if c['name'] == 'Hermosa Beach':
                c['key'] = 'hrbch'
            if c['name'] == 'Los Angeles':
                c['key'] = 'la'

        return configurations

    def scenarios(self, project=None, region_keys=None, project_keys=None, scenario_keys=None, class_scope=None):

        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return FixtureList([
            {
                'class_scope': BaseScenario,
                'key': '{0}_master'.format(project.key),
                'scope': project.schema(),
                'name': 'Master',
                'description': '{0} master layers {1}'.format('2014', project.name),
                'year': 2014,
                'behavior': get_behavior('base_master_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='base_year')]
            },
            {
                'class_scope': BaseScenario,
                'key': '{0}_draft'.format(project.key),
                'scope': project.schema(),
                'name': 'Draft',
                'description': '{0} draft editable layers {1}'.format('2014', project.name),
                'year': 2014,
                'behavior': get_behavior('base_draft_scenario'),
                'selections': dict(),
                'categories': [Category(key='category', value='Base Year Drafts')]

            }]).matching_keys(region_key=region_keys, project_key=project.key if project else project_keys, key=scenario_keys).\
           matching_scope(class_scope=class_scope)





