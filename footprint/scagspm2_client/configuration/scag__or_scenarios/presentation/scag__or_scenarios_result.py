# UrbanFootprint-California (v1.0), Land Use Scenario Development and Modeling System.
#
# Copyright (C) 2014 Calthorpe Analytics
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact: Joe DiStefano (joed@calthorpe.com), Calthorpe Analytics. Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709. Phone: (510) 548-6800. Web: www.calthorpe.com

from footprint.client.configuration.fixture import ResultConfigurationFixture
from footprint.main.models.geospatial.db_entity_keys import DbEntityKey
from footprint.main.publishing.result_initialization import ResultConfiguration, ResultLibraryKey, ResultKey, ResultSort
from footprint.main.models.config.scenario import BaseScenario, Scenario, FutureScenario
from footprint.main.utils.fixture_list import FixtureList


class ScagOrScenariosResultConfigurationFixtures(ResultConfigurationFixture):


    def results(self):
        """
            Used to update or create Results per ConfigEntity instance
            Returns the result library(ies) scoped for the class of self.config_entity.
            The Result will belong to the ResultLibrary specified by result_library_key
        :return:
        """
        return FixtureList(
            # Basic Core result query that summarizes increments
            self.parent_fixture.results() + [
                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='bar_graph',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.BASE_EMPLOYMENT_BY_TYPE,
                    source_db_entity_key=DbEntityKey.BASE,

                    name='Base: Employment by Sector',
                    attributes=['retail', 'office', 'industrial', 'public', 'other'],
                    db_column_lookup=dict(
                        retail='emp_ret',
                        office='emp_off',
                        industrial='emp_ind',
                        public='emp_pub',
                        other='emp_military',
                    ),
                    labels=['Retail', 'Office', 'Industrial', 'Public', 'Other'],
                    stackable=True,
                    is_stacked=False,
                    create_query=lambda result_config: self.employment_breakdown_query(DbEntityKey.BASE),
                    sort_priority=ResultSort.BASE
                ),

                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='bar_graph',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.BASE_DWELLING_UNITS_BY_TYPE,
                    source_db_entity_key=DbEntityKey.BASE,

                    name='Base: Dwelling Units by Type',
                    attributes=['single_family', 'attached', 'multifamily'],
                    db_column_lookup=dict(
                        single_family='du_detsf',
                        attached='du_attsf',
                        multifamily='du_mf'
                    ),
                    labels=['Single Family', 'Attached', 'Multifamily'],
                    stackable=True,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.BASE
                 ),

                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='bar_graph',
                    result_db_entity_key=ResultKey.INCREMENTS,
                    source_db_entity_key=DbEntityKey.INCREMENT,

                    name='Increments: All Metrics',
                    attributes=['population', 'dwelling_units', 'employment'],
                    db_column_lookup=dict(
                        population='pop',
                        dwelling_units='du',
                        employment='emp'
                    ),
                    extent_lookup=dict(
                        population=dict(min=-25000, max=25000),
                        dwelling_units=dict(min=-2500, max=2500),
                        employment=dict(min=-2500, max=2500),
                    ),
                    labels=['Population', 'Dwelling Units', 'Employment'],
                    stackable=False,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),

                # DB Entity Core result query that summarizes dwellings by type
                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='bar_graph',
                    result_db_entity_key=ResultKey.INCREMENTS_DWELLING_UNITS_BY_TYPE,
                    source_db_entity_key=DbEntityKey.INCREMENT,

                    name='Increments: Dwelling Units by Type',
                    attributes=['single_family_large_lot', 'single_family_small_lot', 'multifamily', 'attached_single_family'],
                    db_column_lookup=dict(
                        single_family_large_lot='du_detsf_ll',
                        single_family_small_lot='du_detsf_sl',
                        multifamily='du_mf',
                        attached_single_family='du_attsf',
                    ),
                    labels=['SF Large Lot', 'SF Small Lot', 'MF', 'Attached SF'],
                    stackable=False,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='bar_graph',
                    result_db_entity_key=ResultKey.END_STATE_DWELLING_UNITS_BY_TYPE,
                    source_db_entity_key=DbEntityKey.END_STATE,

                    name='End State: Dwelling Units by Type',
                    attributes=['single_family_large_lot', 'single_family_small_lot', 'multifamily', 'attached_single_family'],
                    db_column_lookup=dict(
                        single_family_large_lot='du_detsf_ll',
                        single_family_small_lot='du_detsf_sl',
                        multifamily='du_mf',
                        attached_single_family='du_attsf',
                    ),
                    labels=['SF Large Lot', 'SF Small Lot', 'MF', 'Attached SF'],
                    stackable=True,
                    is_stacked=False,
                    show_attrs_as_percents=True,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='bar_graph',
                    result_db_entity_key=ResultKey.INCREMENTS_EMPLOYMENT_BY_TYPE,
                    source_db_entity_key=DbEntityKey.INCREMENT,

                    name='Increments: Employment by Sector',
                    attributes=['retail', 'office', 'industrial', 'public', 'other'],
                    db_column_lookup=dict(
                        retail='emp_ret',
                        office='emp_off',
                        industrial='emp_ind',
                        public='emp_pub',
                        other='emp_military',
                    ),
                    labels=['Retail', 'Office', 'Industrial', 'Public', 'Other'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: self.employment_breakdown_query(DbEntityKey.INCREMENT),
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='bar_graph',
                    result_db_entity_key=ResultKey.END_STATE_EMPLOYMENT_BY_TYPE,
                    source_db_entity_key=DbEntityKey.END_STATE,

                    name='End State: Employment by Sector',
                    attributes=['retail', 'office', 'industrial', 'public', 'other'],
                    db_column_lookup=dict(
                        retail='emp_ret',
                        office='emp_off',
                        industrial='emp_ind',
                        public='emp_pub',
                        other='emp_military',
                    ),
                    labels=['Retail', 'Office', 'Industrial', 'Public', 'Other'],
                    stackable=True,
                    is_stacked=False,
                    create_query=lambda result_config: self.employment_breakdown_query(DbEntityKey.END_STATE),
                    sort_priority=ResultSort.FUTURE
                ),

                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_type='analytic_bars',
                    result_db_entity_key=ResultKey.INCREMENTS_BARS,
                    source_db_entity_key=DbEntityKey.END_STATE,

                    name='Results Increments',
                    attributes=['population', 'dwelling_units', 'employment'],
                    db_column_lookup=dict(
                        population='pop',
                        dwelling_units='du',
                        employment='emp'
                    ),
                    extent_lookup=dict(
                        population=dict(min=0, max=5000000),
                        dwelling_units=dict(min=0, max=1000000),
                        employment=dict(min=0, max=1000000)
                    ),
                    labels=['Population', 'Dwelling Units', 'Employment'],
                    stackable=False,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=FutureScenario,
                    result_library_key=ResultLibraryKey.FISCAL,
                    result_type='analytic_result',
                    result_db_entity_key=ResultKey.FISCAL,
                    source_db_entity_key=DbEntityKey.FISCAL,

                    name='Fiscal',
                    attributes=['capital_costs', 'operations_maintenance', 'revenue'],
                    db_column_lookup=dict(
                        capital_costs='residential_capital_costs',
                        operations_maintenance='residential_operations_maintenance_costs',
                        revenue='residential_revenue'
                    ),
                    labels=['capital_costs', 'operations_maintenance', 'revenue'],
                    stackable=False,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=Scenario,
                    result_type='analytic_result',
                    result_library_key=ResultLibraryKey.VMT,
                    result_db_entity_key=ResultKey.VMT,
                    source_db_entity_key=DbEntityKey.VMT,

                    name='VMT',
                    attributes=['annual_vmt', 'daily_vmt', 'daily_vmt_per_hh', 'annual_vmt_per_capita'],
                    db_column_lookup=dict(
                        annual_vmt='vmt_annual_w_trucks',
                        daily_vmt='vmt_daily_w_trucks',
                        daily_vmt_per_hh='vmt_daily_per_hh',
                        annual_vmt_per_capita='vmt_annual_per_capita'
                    ),
                    labels=['Annual VMT', 'Daily VMT', 'Daily VMT Per HH', 'Annual VMT Per Capita'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(vmt_annual_w_trucks) as annual_vmt__sum, SUM(vmt_daily_w_trucks) as daily_vmt__sum, Case when SUM(hh) > 0 then SUM(vmt_daily_w_trucks) / SUM(hh) else 0 end as daily_vmt_per_hh__sum, Case when SUM(hh) > 0 then SUM(vmt_daily_w_trucks) * 350 / SUM(hh) else 0 end as annual_vmt_per_hh__sum, Case when SUM(pop) > 0 then SUM(vmt_daily_w_trucks) * 350 / SUM(pop) else 0 end as annual_vmt_per_capita__sum, Case when SUM(pop) > 0 then SUM(vmt_daily_w_trucks) / SUM(pop) else 0 end as daily_vmt_per_capita__sum, Case when SUM(emp) > 0 then SUM(vmt_daily_w_trucks) / SUM(emp) else 0 end as daily_vmt_per_emp__sum, Case when SUM(emp) > 0 then SUM(vmt_daily_w_trucks) * 350 / SUM(emp) else 0 end as annual_vmt_per_emp__sum   FROM %({0})s'.format(DbEntityKey.VMT),
                    sort_priority=ResultSort.FUTURE
                ),
                ResultConfiguration(
                    class_scope=Scenario,
                    result_type='analytic_result',
                    result_library_key=ResultLibraryKey.ENERGY,
                    result_db_entity_key=ResultKey.ENERGY,
                    source_db_entity_key=DbEntityKey.ENERGY,

                    name='Energy',
                    attributes=['total_gas_use', 'total_electricity_use', 'residential_gas_use', 'residential_electricity_use', 'commercial_gas_use', 'commercial_electricity_use'],
                    db_column_lookup=dict(
                        total_gas_use='total_gas_use',
                        total_electricity_use='total_electricity_use',
                        residential_gas_use='residential_gas_use',
                        residential_electricity_use='residential_electricity_use',
                        commercial_gas_use='commercial_gas_use',
                        commercial_electricity_use='commercial_electricity_use'
                    ),
                    labels=['total_gas_use', 'total_electricity_use', 'residential_gas_use', 'residential_electricity_use', 'commercial_gas_use', 'commercial_electricity_use'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(total_gas_use) as total_gas_use__sum, SUM(total_electricity_use) as total_electricity_use__sum, SUM(residential_gas_use) as residential_gas_use__sum, SUM(residential_electricity_use) as residential_electricity_use__sum, SUM(commercial_gas_use) as commercial_gas_use__sum, SUM(commercial_electricity_use) as commercial_electricity_use__sum, Case when SUM(hh) > 0 then SUM(residential_gas_use) / SUM(hh) else 0 end as residenital_per_hh_gas_use__sum, Case when SUM(hh) > 0 then SUM(residential_electricity_use) / SUM(hh) else 0 end as residenital_per_hh_electricity_use__sum, Case when SUM(total_commercial_sqft) > 0 then SUM(commercial_gas_use) / SUM(emp) else 0 end as commercial_per_emp_gas_use__sum, Case when SUM(total_commercial_sqft) > 0 then SUM(commercial_electricity_use) / SUM(emp) else 0 end as commercial_per_emp_electricity_use__sum FROM %({0})s'.format(DbEntityKey.ENERGY),
                    sort_priority=ResultSort.FUTURE
                ),

                ResultConfiguration(
                    class_scope=Scenario,
                    result_type='analytic_result',
                    result_library_key=ResultLibraryKey.WATER,
                    result_db_entity_key=ResultKey.WATER,
                    source_db_entity_key=DbEntityKey.WATER,

                    name='Water',
                    attributes=['total_water_use', 'residential_water_use', 'commercial_water_use',
                                'residential_indoor_water_use', 'residential_outdoor_water_use',
                                'commercial_indoor_water_use', 'commercial_outdoor_water_use'],
                    db_column_lookup=dict(
                        total_water_use='total_water_use',
                        residential_water_use='residential_water_use',
                        commercial_water_use='commercial_water_use',
                        residential_indoor_water_use='residential_indoor_water_use',
                        residential_outdoor_water_use='residential_outdoor_water_use',
                        commercial_indoor_water_use='commercial_indoor_water_use',
                        commercial_outdoor_water_use='commercial_outdoor_water_use'
                    ),
                    labels=['total_water_use', 'residential_water_use', 'commercial_water_use',
                                'residential_indoor_water_use', 'residential_outdoor_water_use',
                                'commercial_indoor_water_use', 'commercial_outdoor_water_use'],
                    stackable=False,
                    is_stacked=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.FUTURE
                ),

                # Aggregate result from the Analytic Bars
                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='analytic_bars',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.Fab.ricate('base_bars'),
                    source_db_entity_key=DbEntityKey.BASE,

                    name='Base Results',
                    attributes=['employment', 'dwelling_units', 'population'],
                    db_column_lookup=dict(
                        employment='emp',
                        dwelling_units='du',
                        population='pop'
                    ),
                    extent_lookup=dict(
                        population=dict(min=0, max=5000000),
                        dwelling_units=dict(min=0, max=1000000),
                        employment=dict(min=0, max=1000000)
                    ),
                    labels=['Employees', 'Dwelling Units', 'Population'],
                    stackable=False,
                    create_query=self.simple_aggregate,
                    sort_priority=ResultSort.BASE
                ),

            #result configurartions for water analysis
            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.WATER,
                result_db_entity_key=ResultKey.WATER_INDOOR_OUTDOOR,
                source_db_entity_key=DbEntityKey.WATER,

                name='Water Use (gal): Indoor and Outdoor ',
                attributes=['residential_indoor_water_use', 'residential_outdoor_water_use',
                            'commercial_indoor_water_use',  'commercial_outdoor_water_use'],
                db_column_lookup=dict(
                    residential_indoor_water_use='residential_indoor_water_use',
                    residential_outdoor_water_use='residential_outdoor_water_use',
                    commercial_indoor_water_use='commercial_indoor_water_use',
                    commercial_outdoor_water_use='commercial_outdoor_water_use'
                ),
                labels=['Res-Indoor', 'Res-Outdoor', 'Com-Indoor', 'Com-Outdoor'],
                stackable=False,
                is_stacked=False,
                create_query=self.simple_aggregate,
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.WATER,
                result_db_entity_key=ResultKey.WATER_TOTAL,
                source_db_entity_key=DbEntityKey.WATER,

                name='Water Use (gal): Residential and Commercial',
                attributes=['residential_water_use', 'commercial_water_use'],
                db_column_lookup=dict(
                    residential_water_use='residential_water_use',
                    commercial_water_use='commercial_water_use'
                ),
                labels=['Residential', 'Commercial'],
                stackable=False,
                is_stacked=False,
                create_query=self.simple_aggregate,
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.WATER,
                result_db_entity_key=ResultKey.WATER_COSTS_TOTAL,
                source_db_entity_key=DbEntityKey.WATER,

                name='Water Costs ($-2014): Residential and Commercial',
                attributes=['residential_water_use', 'commercial_water_use'],
                db_column_lookup=dict(
                    residential_water_use='residential_water_use',
                    commercial_water_use='commercial_water_use'
                ),
                labels=['Residential', 'Commercial'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(residential_water_use) / 325851.431889 * 1349.0 as residential_water_use__sum, SUM(commercial_water_use) / 325851.431889 * 1349.0 as commercial_water_use__sum from %({0})s'.format(DbEntityKey.WATER),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.ENERGY,
                result_db_entity_key=ResultKey.ENERGY_TOTAL,
                source_db_entity_key=DbEntityKey.ENERGY,

                name='Energy Use (MMBTU): Residential and Commercial',
                attributes=['residential_energy_use', 'commercial_energy_use'],
                db_column_lookup=dict(
                    residential_energy_use='residential_energy_use',
                    commercial_energy_use='commercial_energy_use'
                ),
                labels=['Residential', 'Commercial'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(residential_electricity_use) * 0.0034095106405145 + sum(residential_gas_use) * 0.1 as residential_energy_use__sum, SUM(commercial_electricity_use) * 0.0034095106405145 + sum(commercial_gas_use) * 0.1 as commercial_energy_use__sum from %({0})s'.format(DbEntityKey.ENERGY),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.ENERGY,
                result_db_entity_key=ResultKey.ENERGY_RES_USE,
                source_db_entity_key=DbEntityKey.ENERGY,

                name='Energy Use (MMBTU): Residential by Type',
                attributes=['du_detsf_ll_energy_use', 'du_detsf_sl_energy_use', 'du_attsf_energy_use', 'du_mf_energy_use'],
                db_column_lookup=dict(
                    du_detsf_ll_energy_use='du_detsf_ll_energy_use',
                    du_detsf_sl_energy_use='du_detsf_sl_energy_use',
                    du_attsf_energy_use='du_attsf_energy_use',
                    du_mf_energy_use='du_mf_energy_use'
                ),
                labels=['SF Large Lot', 'SF Small Lot', 'Attached SF', 'Multifamily'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(du_detsf_ll_electricity_use) * 0.0034095106405145 + sum(du_detsf_ll_gas_use) * 0.1 as du_detsf_ll_energy_use__sum, SUM(du_detsf_sl_electricity_use) * 0.0034095106405145 + sum(du_detsf_sl_gas_use) * 0.1 as du_detsf_sl_energy_use__sum, SUM(du_attsf_electricity_use) * 0.0034095106405145 + sum(du_attsf_gas_use) * 0.1 as du_attsf_energy_use__sum, SUM(du_mf_electricity_use) * 0.0034095106405145 + sum(du_mf_gas_use) * 0.1 as du_mf_energy_use__sum from %({0})s'.format(DbEntityKey.ENERGY),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.ENERGY,
                result_db_entity_key=ResultKey.ENERGY_COM_USE,
                source_db_entity_key=DbEntityKey.ENERGY,

                name='Energy Use (MMBTU): Commercial by Type',
                attributes=['retail_energy_use', 'office_energy_use', 'public_energy_use', 'industrial_energy_use'],
                db_column_lookup=dict(
                    retail_energy_use='retail_energy_use',
                    office_energy_use='office_energy_use',
                    public_energy_use='public_energy_use',
                    industrial_energy_use='industrial_energy_use'
                ),
                labels=['Retail', 'Office', 'Public', '*Industrial'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(retail_services_electricity_use + restaurant_electricity_use + accommodation_electricity_use + other_services_electricity_use) * 0.0034095106405145 + sum(retail_services_gas_use + restaurant_gas_use + accommodation_gas_use + other_services_gas_use) * 0.1 as retail_energy_use__sum, SUM(office_services_electricity_use + medical_services_electricity_use) * 0.0034095106405145 + sum(office_services_gas_use + medical_services_gas_use) * 0.1 as office_energy_use__sum, SUM(public_admin_electricity_use + education_electricity_use) * 0.0034095106405145 + sum(public_admin_gas_use + education_gas_use) * 0.1 as public_energy_use__sum, SUM(wholesale_electricity_use + transport_warehousing_electricity_use) * 0.0034095106405145 + sum(wholesale_gas_use + transport_warehousing_gas_use) * 0.1 as industrial_energy_use__sum from %({0})s'.format(DbEntityKey.ENERGY),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.ENERGY,
                result_db_entity_key=ResultKey.ENERGY_COSTS_TOTAL,
                source_db_entity_key=DbEntityKey.ENERGY,

                name='Energy Costs ($-2014): Residential and Commercial',
                attributes=['residential_energy_cost', 'commercial_energy_cost'],
                db_column_lookup=dict(
                    residential_energy_cost='residential_energy_cost',
                    commercial_energy_cost='commercial_energy_cost'
                ),
                labels=['Residential', 'Commercial'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(residential_electricity_use) * 0.1802 + sum(residential_gas_use) * 1.203 as residential_energy_cost__sum, SUM(commercial_electricity_use) * 0.1822 + sum(commercial_gas_use) * 0.854 as commercial_energy_cost__sum from %({0})s'.format(DbEntityKey.ENERGY),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.ENERGY,
                result_db_entity_key=ResultKey.ENERGY_EMISSIONS_TOTAL,
                source_db_entity_key=DbEntityKey.ENERGY,

                name='Energy Emissions (CO2e): Residential and Commercial',
                attributes=['residential_energy_emissions', 'commercial_energy_emissions'],
                db_column_lookup=dict(
                    residential_energy_emissions='residential_energy_emissions',
                    commercial_energy_emissions='commercial_energy_emissions'
                ),
                labels=['Residential', 'Commercial'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(residential_electricity_use) * 0.69 + sum(residential_gas_use) * 11.7 as residential_energy_emissions__sum, SUM(commercial_electricity_use) * 0.69 + sum(commercial_gas_use) * 11.7 as commercial_energy_emissions__sum from %({0})s'.format(DbEntityKey.ENERGY),
                sort_priority=ResultSort.BASE
             ),

            ResultConfiguration(
                class_scope=FutureScenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.FISCAL,
                result_db_entity_key=ResultKey.FISCAL_CHART,
                source_db_entity_key=DbEntityKey.FISCAL,

                name='Fiscal ($-2012): Residential Costs/Revenue',
                attributes=['residential_capital_costs', 'residential_operations_maintenance_costs',
                            'residential_revenue'],
                db_column_lookup=dict(
                    residential_capital_costs='residential_capital_costs',
                    residential_operations_maintenance_costs='residential_operations_maintenance_costs',
                    residential_revenue='residential_revenue'
                ),
                labels=['Capital Costs', 'O&M Costs', 'Revenue'],
                stackable=False,
                is_stacked=False,
                create_query=self.simple_aggregate,
                sort_priority=ResultSort.BASE
            ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.VMT,
                result_db_entity_key=ResultKey.VMT_PER_CAPITA,
                source_db_entity_key=DbEntityKey.VMT,

                name='Annual VMT: Per Capita / Per Employee',
                attributes=['vmt_annual_per_capita', 'vmt_annual_per_emp'],
                db_column_lookup=dict(
                    vmt_annual_per_capita='vmt_annual_per_capita',
                    vmt_annual_per_emp='vmt_annual_per_emp'
                ),
                labels=['Per Capita', 'Per Employee'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(vmt_annual_w_trucks) / sum(pop) as vmt_annual_per_capita__sum, SUM(vmt_annual_w_trucks) / sum(emp) as vmt_annual_per_emp__sum from %({0})s'.format(DbEntityKey.VMT),
                sort_priority=ResultSort.BASE
            ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.VMT,
                result_db_entity_key=ResultKey.VMT_FUEL,
                source_db_entity_key=DbEntityKey.VMT,

                name='Annual Fuel Consumption (gal)',
                attributes=['annual_gallons'],
                db_column_lookup=dict(
                    annual_gallons='annual_gallons'
                ),
                labels=['Gallons'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(vmt_annual_w_trucks) / 19.4 as annual_gallons__sum from %({0})s'.format(DbEntityKey.VMT),
                sort_priority=ResultSort.BASE
            ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.VMT,
                result_db_entity_key=ResultKey.VMT_COSTS,
                source_db_entity_key=DbEntityKey.VMT,

                name='Annual Vehicle Costs ($-2014)',
                attributes=['cost_per_mile'],
                db_column_lookup=dict(
                    cost_per_mile='cost_per_mile'
                ),
                labels=['Vehicle Costs'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(vmt_annual_w_trucks) * 0.35 as cost_per_mile__sum from %({0})s'.format(DbEntityKey.VMT),
                sort_priority=ResultSort.BASE
            ),

            ResultConfiguration(
                class_scope=Scenario,
                result_type='bar_graph',
                result_library_key=ResultLibraryKey.VMT,
                result_db_entity_key=ResultKey.VMT_EMISSIONS,
                source_db_entity_key=DbEntityKey.VMT,

                name='Annual Vehicle Emissions (lbs CO2e)',
                attributes=['vehicle_emissions'],
                db_column_lookup=dict(
                    vehicle_emissions='vehicle_emissions'
                ),
                labels=['Emissions'],
                stackable=False,
                is_stacked=False,
                create_query=lambda result_config: 'SELECT SUM(vmt_annual_w_trucks) as vehicle_emissions__sum from %({0})s'.format(DbEntityKey.VMT),
                sort_priority=ResultSort.BASE
            )
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
