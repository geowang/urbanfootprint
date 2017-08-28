/*
 * UrbanFootprint v1.5
 * Copyright (C) 2016 Calthorpe Analytics
 *
 * This file is part of UrbanFootprint version 1.5
 *
 * UrbanFootprint is distributed under the terms of the GNU General
 * Public License version 3, as published by the Free Software Foundation. This
 * code is distributed WITHOUT ANY WARRANTY, without implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
 * Public License v3 for more details; see <http://www.gnu.org/licenses/>.
 */



FootprintScagDm.ScagDmDelegate = Footprint.DefaultDelegate.extend({

    /***
     * Indicate that this is a data manager site so that we show/hide certain parts of the app
     */
    isDataManager: YES,

    dbEntityKeyToFeatureRecordType: function() {
        return SC.Object.create({
            existing_land_use_parcels_2016: FootprintScagDm.ScagExistingLandUseParcelFeature,
            general_plan_parcels: FootprintScagDm.ScagGeneralPlanParcelFeature,
            tier2_taz: FootprintScagDm.ScagTier2TazFeature,
            scenario_planning_zones: FootprintScagDm.ScagScenarioPlanningZones,
            entitlement_parcels_2016: FootprintScagDm.ScagEntitlementParcelFeature,
            city_boundary: FootprintScagDm.ScagJurisdictionBoundary,
            bike_lane: FootprintScagDm.ScagBikeLaneFeature,
            census_tracts: FootprintScagDm.ScagCensusTractsFeature,
            farmland: FootprintScagDm.ScagFarmlandFeature,
            region_sphere_of_influence: FootprintScagDm.ScagRegionSphereOfInfluenceFeature,
            endangered_species: FootprintScagDm.ScagEndangeredSpeciesFeature,
            habitat_conservation_areas: FootprintScagDm.ScagEndangeredSpeciesFeature,
            cpad_holdings: FootprintScagDm.ScagCpadHoldingsFeature,
            flood_zones: FootprintScagDm.ScagFloodZonesFeature,
            sea_level_rise: FootprintScagDm.ScagSeaLevelRiseFeature,
            transit_priority_areas: FootprintScagDm.ScagTransitPriorityAreasFeature,
            major_transit_stops: FootprintScagDm.ScagMajorTransitStopsFeature,
            high_quality_transit_areas: FootprintScagDm.ScagHighQualityTransitAreasFeature,
            high_quality_transit_corridors: FootprintScagDm.ScagHighQualityTransitCorridorsFeature,
            existing_land_use_parcels_2012: FootprintScagDm.ScagExistingLandUseParcelFeature,

        }, sc_super())
    }.property('parentDelegate').cacheable(),

    defaultsControllers: function() {
        return SC.Object.create({
            existing_land_use_parcels_2016: FootprintScagDm.scagExistingLandUseParcelFeatureDefaultController
        }, sc_super())
    }.property('parentDelegate').cacheable(),

    loadingRegionStateClass: function() {
        return SC.objectForPropertyPath('FootprintScagDm.LoadingRegionScagDmState')
    }.property().cacheable()

});
