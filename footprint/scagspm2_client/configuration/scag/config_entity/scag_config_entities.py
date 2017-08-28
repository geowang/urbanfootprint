from footprint.client.configuration.fixture import ConfigEntitiesFixture, MediumFixture
from footprint.client.configuration.default.config_entity.default_config_entities import ConfigEntityMediumKey
from django.conf import settings
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'

from django.contrib.gis.geos import MultiPolygon, Polygon

class ScagDbEntityKey(DbEntityKey):
    #SCAG regional datasets
    FLOOD_ZONES = 'flood_zones'
    CPAD_HOLDINGS = 'cpad_holdings'
    FARMLAND = 'farmland'
    ENDANGERED_SPECIES = 'endangered_species'
    HABITAT_CONSERVATION_AREA = 'habitat_conservation_areas'
    COUNTY_BOUNDARY = 'county_boundary'
    HIGH_QUALITY_TRANSIT_AREAS = 'high_quality_transit_areas'
    HIGH_QUALITY_TRANSIT_CORRIDORS = 'high_quality_transit_corridors'
    MAJOR_TRANSIT_STOPS = 'major_transit_stops'
    TRANSIT_PRIORITY_AREAS = 'transit_priority_areas'
    SUB_REGION = 'sub_region'
    CENSUS_TRACTS = 'census_tracts'

    EXISTING_LAND_USE_PARCELS = 'existing_land_use_parcels'
    REGION_EXISTING_LAND_USE_PARCELS = 'region_existing_land_use_parcels'
    PROJECT_EXISTING_LAND_USE_PARCELS = 'project_existing_land_use_parcels'

    GENERAL_PLAN_PARCELS = 'general_plan_parcels'
    REGION_GENERAL_PLAN_PARCELS = 'region_general_plan_parcels'

    SCENARIO_PLANNING_ZONES = 'scenario_planning_zones'
    REGION_SCENARIO_PLANNING_ZONES = 'region_scenario_planning_zones'

    JURISDICTION_BOUNDARY = 'jurisdiction_boundary'
    REGION_JURISDICTION_BOUNDARY = 'region_jurisdiction_boundary'

    SPHERE_OF_INFLUENCE = 'sphere_of_influence'
    REGION_SPHERE_OF_INFLUENCE = 'region_sphere_of_influence'

    TIER2_TAZ = 'tier2_taz'
    REGION_TIER2_TAZ = 'region_tier2_taz'


class ScagConfigEntitiesFixture(ConfigEntitiesFixture):
    def regions(self, region_keys=None, class_scope=None):
        return FixtureList([
            # dict(
            #     key='orange_county',
            #     name='Orange County',
            #     description='Orange County',
            #     media=[
            #         MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('scag_logo'), name='SCAG Logo',
            #                         url='/static/client/{0}/logos/scag.png'.format(CLIENT))
            #     ],
            #     #defaulting to an Irvine view for the moment
            #     bounds=MultiPolygon([Polygon((
            #         (-117.869537353516, 33.5993881225586),
            #         (-117.869537353516, 33.7736549377441),
            #         (-117.678024291992, 33.7736549377441),
            #         (-117.678024291992, 33.5993881225586),
            #         (-117.869537353516, 33.5993881225586),
            #     ))]),
            # ),
            # dict(
            #     key='la_county',
            #     name='Los Angeles County',
            #     description='Los Angeles County',
            #     media=[
            #         MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('scag_logo'), name='SCAG Logo',
            #                         url='/static/client/{0}/logos/scag.png'.format(CLIENT))
            #     ],
            #     #defaulting to an Irvine view for the moment
            #     bounds=MultiPolygon([Polygon((
            #         (-117.869537353516, 33.5993881225586),
            #         (-117.869537353516, 33.7736549377441),
            #         (-117.678024291992, 33.7736549377441),
            #         (-117.678024291992, 33.5993881225586),
            #         (-117.869537353516, 33.5993881225586),
            #     ))]),
            # ),
            dict(
                key='or_scenarios',
                name='Orange County',
                description='Orange County',
                media=[
                    MediumFixture(key=ConfigEntityMediumKey.Fab.ricate('scag_logo'), name='SCAG Logo',
                                    url='/static/client/{0}/logos/scag.png'.format(settings.CLIENT))
                ],
                #defaulting to an Irvine view for the moment
                bounds=MultiPolygon([Polygon((
                    (-117.869537353516, 33.5993881225586),
                    (-117.869537353516, 33.7736549377441),
                    (-117.678024291992, 33.7736549377441),
                    (-117.678024291992, 33.5993881225586),
                    (-117.869537353516, 33.5993881225586),
                ))]),
            )
        ]).matching_keys(key=region_keys).matching_scope(class_scope=class_scope)


    def scenarios(self, project=None, region_keys=None, project_keys=None, scenario_keys=None, class_scope=None):

        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        return FixtureList([]).matching_keys(region_key=region_keys, project_key=project.key if project else project_keys, key=scenario_keys).\
           matching_scope(class_scope=class_scope)

