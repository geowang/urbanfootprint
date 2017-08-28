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
from footprint.client.configuration.scag.config_entity.scag_config_entities import ScagDbEntityKey
from footprint.main.publishing.result_initialization import ResultConfiguration, ResultLibraryKey, ResultKey, ResultSort
from footprint.main.models.config.scenario import BaseScenario
from footprint.main.utils.fixture_list import FixtureList


class ScagLaCountyResultConfigurationFixtures(ResultConfigurationFixture):


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
                    result_db_entity_key=ResultKey.SOCIOECONOMIC12,
                    source_db_entity_key=ScagDbEntityKey.JURISDICTION_BOUNDARY,

                    name='2012 Socioeconomic Totals',
                    attributes=['pop12', 'hh12', 'emp12'],
                    db_column_lookup=dict(
                        pop12='pop12',
                        hh12='hh12',
                        emp12='emp12'
                    ),
                    labels=['pop12', 'hh12', 'emp12'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(pop12) as pop12__sum, SUM(hh12) as hh12__sum, SUM(emp12) as emp12__sum FROM %({0})s'.format(ScagDbEntityKey.JURISDICTION_BOUNDARY),
                    sort_priority=ResultSort.BASE
                ),
                
                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='bar_graph',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.SOCIOECONOMIC20,
                    source_db_entity_key=ScagDbEntityKey.JURISDICTION_BOUNDARY,

                    name='2020 Socioeconomic Totals',
                    attributes=['pop12', 'hh12', 'emp12'],
                    db_column_lookup=dict(
                        pop12='pop20',
                        hh12='hh20',
                        emp12='emp20'
                    ),
                    labels=['pop20', 'hh20', 'emp20'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(pop20) as pop20__sum, SUM(hh20) as hh20__sum, SUM(emp20) as emp20__sum FROM %({0})s'.format(ScagDbEntityKey.JURISDICTION_BOUNDARY),
                    sort_priority=ResultSort.BASE
                ),
                
                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='bar_graph',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.SOCIOECONOMIC35,
                    source_db_entity_key=ScagDbEntityKey.JURISDICTION_BOUNDARY,

                    name='2035 Socioeconomic Totals',
                    attributes=['pop35', 'hh35', 'emp35'],
                    db_column_lookup=dict(
                        pop35='pop35',
                        hh35='hh35',
                        emp35='emp35'
                    ),
                    labels=['pop35', 'hh35', 'emp35'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(pop35) as pop35__sum, SUM(hh35) as hh35__sum, SUM(emp35) as emp35__sum FROM %({0})s'.format(ScagDbEntityKey.JURISDICTION_BOUNDARY),
                    sort_priority=ResultSort.BASE
                ),

                ResultConfiguration(
                    class_scope=BaseScenario,
                    result_type='bar_graph',
                    result_library_key=ResultLibraryKey.DEFAULT,
                    result_db_entity_key=ResultKey.SOCIOECONOMIC40,
                    source_db_entity_key=ScagDbEntityKey.JURISDICTION_BOUNDARY,

                    name='2040 Socioeconomic Totals',
                    attributes=['pop40', 'hh40', 'emp40'],
                    db_column_lookup=dict(
                        pop40='pop40',
                        hh40='hh40',
                        emp40='emp40'
                    ),
                    labels=['pop40', 'hh40', 'emp40'],
                    stackable=False,
                    is_stacked=False,
                    create_query=lambda result_config: 'SELECT SUM(pop40) as pop40__sum, SUM(hh40) as hh40__sum, SUM(emp40) as emp40__sum FROM %({0})s'.format(ScagDbEntityKey.JURISDICTION_BOUNDARY),
                    sort_priority=ResultSort.BASE
                )
            ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
