from footprint.client.configuration.scag.base.scenario_planning_zones import ScenarioPlanningZones
from footprint.client.configuration.scag.base.county_boundary import CountyBoundary
from footprint.client.configuration.scag.base.cpad_holdings import CpadHoldings
from footprint.client.configuration.scag.base.endangered_species import EndangeredSpecies
from footprint.client.configuration.scag.base.existing_land_use_parcel import ExistingLandUseParcel
from footprint.client.configuration.scag.base.farmland import Farmland
from footprint.client.configuration.scag.base.flood_zones import FloodZones
from footprint.client.configuration.scag.base.general_plan_parcels import GeneralPlanParcels
from footprint.client.configuration.scag.base.habitat_conservation_areas import HabitatConservationAreas
from footprint.client.configuration.scag.base.high_quality_transit_areas import HighQualityTransitAreas
from footprint.client.configuration.scag.base.high_quality_transit_corridors import HighQualityTransitCorridors
from footprint.client.configuration.scag.base.jurisdiction_boundary import JurisdictionBoundary
from footprint.client.configuration.scag.base.major_transit_stops import MajorTransitStops
from footprint.client.configuration.scag.base.sphere_of_influence import SphereOfInfluence
from footprint.client.configuration.scag.base.sub_region import SubRegion
from footprint.client.configuration.scag.base.tier2_taz import Tier2Taz
from footprint.client.configuration.scag.base.transit_priority_areas import TransitPriorityAreas
from footprint.client.configuration.scag.config_entity.scag_config_entities import ScagDbEntityKey
from footprint.main.models.base.census_tract import CensusTract
from footprint.main.models.geospatial.db_entity import DbEntity
from footprint.main.models.geospatial.feature_behavior import FeatureBehavior
from footprint.main.models.base.cpad_holdings_feature import CpadHoldingsFeature
from footprint.main.models.geospatial.behavior import BehaviorKey, Behavior
from footprint.main.models.geospatial.db_entity_configuration import update_or_create_db_entity
from footprint.client.configuration.fixture import RegionFixture
from footprint.main.models.geospatial.feature_class_configuration import FeatureClassConfiguration
from footprint.main.models.geospatial.intersection import Intersection, IntersectionKey
from footprint.main.utils.fixture_list import FixtureList

__author__ = 'calthorpe_associates'



class ScagRegionFixture(RegionFixture):

    def default_remote_db_entities(self):
        """
            Add the any background imagery. This function is called from default_db_entities so it doesn't
            need to call the parent_fixture's method
        """
        return self.parent_config_entity_fixture.default_remote_db_entities()

    def default_db_entities(self):
        """
            Region specific db_entity_setups
        :param default_dict:
        :return:
        """

        config_entity = self.config_entity
        parent_region_fixture = self.parent_fixture
        default_db_entities = parent_region_fixture.default_db_entities()
        # The DbEntity keyspace. These keys have no prefix
        Key = ScagDbEntityKey
        # The Behavior keyspace
        behavior_key = BehaviorKey.Fab.ricate
        # Used to load Behaviors defined elsewhere
        get_behavior = lambda key: Behavior.objects.get(key=behavior_key(key))

        if self.config_entity.key=='scag':
            # Block the client-level region. We just want real regions
            return []

        return default_db_entities + FixtureList([
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.FLOOD_ZONES,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=FloodZones
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.ENDANGERED_SPECIES,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=EndangeredSpecies
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.CPAD_HOLDINGS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CpadHoldingsFeature
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.CPAD_HOLDINGS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CpadHoldings
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.HABITAT_CONSERVATION_AREA,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=HabitatConservationAreas
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.COUNTY_BOUNDARY,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CountyBoundary
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.HIGH_QUALITY_TRANSIT_AREAS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=HighQualityTransitAreas
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.HIGH_QUALITY_TRANSIT_CORRIDORS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=HighQualityTransitCorridors
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.MAJOR_TRANSIT_STOPS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=MajorTransitStops
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.TRANSIT_PRIORITY_AREAS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=TransitPriorityAreas
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='polygon')
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.FARMLAND,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=Farmland,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type='polygon', to_type='centroid')
                )
            )),

            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_EXISTING_LAND_USE_PARCELS,
                    feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=ExistingLandUseParcel,
                    primary_geography=True,
                    primary_key='source_id',
                    primary_key_type='int',
                    fields=dict(),
                    related_fields=dict(land_use_definition=dict(
                        single=True,
                        related_class_name='footprint.client.configuration.scag.built_form.scag_land_use_definition.ScagLandUseDefinition',
                        related_class_join_field_name='land_use',
                        source_class_join_field_name='lu12')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference')
                )
            )),

            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_GENERAL_PLAN_PARCELS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=GeneralPlanParcels,
                    primary_key='source_id',
                    primary_key_type='int',
                    fields=dict(),
                    related_fields=dict(land_use_definition=dict(
                        single=True,
                        related_class_name='footprint.client.configuration.scag.built_form.scag_land_use_definition.ScagLandUseDefinition',
                        # Use this for the resource type, since we don't want a client-specific resource URL
                        # TODO not wired up yet
                        resource_model_class_name='footprint.main.models.built_form.ClientLandUseDefinition',
                        related_class_join_field_name='land_use',
                        source_class_join_field_name='scag_gp_code')
                    )
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(join_type='attribute')
                )
            )),

            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_SCENARIO_PLANNING_ZONES,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=ScenarioPlanningZones,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),

            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_JURISDICTION_BOUNDARY,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=JurisdictionBoundary,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_SPHERE_OF_INFLUENCE,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SphereOfInfluence,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.REGION_TIER2_TAZ,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=Tier2Taz,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.CENSUS_TRACTS,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=CensusTract,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            )),
            update_or_create_db_entity(config_entity, DbEntity(
                key=Key.SUB_REGION,
                feature_class_configuration=FeatureClassConfiguration(
                    abstract_class=SubRegion,
                ),
                feature_behavior=FeatureBehavior(
                    behavior=get_behavior('reference'),
                    intersection=Intersection(from_type=IntersectionKey.POLYGON, to_type=IntersectionKey.CENTROID)
                )
            ))
        ])

