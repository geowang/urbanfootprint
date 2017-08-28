from django.conf import settings
from footprint.client.configuration.default.config_entity.default_config_entities import ConfigEntityMediumKey
from footprint.client.configuration.default.config_entity.default_project import project_key
from footprint.client.configuration.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.main.models.geospatial.behavior import Behavior
from footprint.main.models.category import Category
from footprint.main.models.config.scenario import BaseScenario
from footprint.main.models.geospatial.behavior import BehaviorKey

from footprint.main.utils.fixture_list import FixtureList


__author__ = 'calthorpe_associates'


class ScagOrangeCountyConfigEntitiesFixture(ConfigEntitiesFixture):
    def projects(self, region=None, region_keys=None, project_keys=None, class_scope=None):

        # Phase 3 all jurisdictions get a project
        jurisdictions = ["Laguna Hills", "Westminster", "Anaheim", "La Habra", "Orange", "Buena Park", "Dana Point",
                          "Huntington Beach", "Fountain Valley", "San Juan Capistrano", "Laguna Beach", "Garden Grove",
                          "Laguna Niguel", "Rancho Santa Margarita", "Aliso Viejo", "Santa Ana", "Laguna Woods",
                          "Yorba Linda", "Los Alamitos", "La Palma", "Seal Beach", "Mission Viejo", "Stanton",
                          "Unincorporated", "Newport Beach", "Villa Park", "Cypress", "Brea", "San Clemente",
                          "Fullerton", "Lake Forest", "Placentia", "Irvine", "Costa Mesa", "Tustin"]

        # build with no projects for easier deployments
        # jurisdictions = []

        # Phase 2 limited set of projects
        jurisdictions = ["Irvine", "Mission Viejo"]

        configurations = map(lambda jurisdiction_name: {
            'key': project_key(jurisdiction_name),
            'import_key': jurisdiction_name.lower().replace(' ', '_'),
            'name': jurisdiction_name,
            'description': "City of %s" % jurisdiction_name,
            'base_year': 2014,
            'region_key': 'orange_county',
            'media': [
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate(jurisdiction_name.lower().replace(' ', '_') + '_logo'),
                                  name='%s Logo' % jurisdiction_name,
                                  url='/static/client/{0}/logos/{1}_logo.png'.format(settings.CLIENT, jurisdiction_name.lower().replace(' ', '_')))
                ],
        }, jurisdictions)

        # supporting a legacy build with the hand-typed keys used there
        for c in configurations:
            if c['name'] == 'Irvine':
                c['key'] = 'irv'
                c['media'] = [
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('irvine_logo'), name='Irvine Logo',
                                  url='/static/client/{0}/logos/cityofirvine.png'.format(settings.CLIENT))
                ]
            if c['name'] == 'Mission Viejo':
                c['key'] = 'mv'

        # return configurations
        return FixtureList(configurations).matching_keys(region_keys=region_keys, key=project_keys).matching_scope(class_scope=class_scope)


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




