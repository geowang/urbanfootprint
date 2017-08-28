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
import os
from django.core.management import call_command
from django.conf import settings

from footprint.client.configuration.fixture import InitFixture
from footprint.client.configuration.demo.built_form.demo_land_use_definition import DemoLandUseDefinition
import logging
from footprint.main.models.keys.user_group_key import UserGroupKey

logger = logging.getLogger(__name__)

class DemoInitFixture(InitFixture):

    def import_database(self):
        if settings.USE_LOCAL_SAMPLE_DATA_SETS:
            #Using this instead of putting a config in settings.py because
            # django can't handle cloning the sample db in unit tests (postgis problems, I think)
            dct = dict(
        ENGINE='django.contrib.gis.db.backends.postgis',
        HOST='localhost',
        NAME='demo_urbanfootprint',
        USER='calthorpe',
        PASSWORD='Calthorpe123',
        PORT='5432'
            )
            return dict(
                host=dct['HOST'],
                database=dct['NAME'],
                user=dct['USER'],
                password=dct['PASSWORD']
            )
        else:
            return dict(
                host='10.0.0.133',
                database='demo_urbanfootprint',
                user='calthorpe',
                password='Calthorpe123'
            )



    def model_class_modules(self):
        """
            DEMO defines additional concrete model classes in the following modules
        :return:
        """
        return [
            ("built_form", "land_use_definition"),
            ("built_form", "land_use")
        ]

    def populate_models(self):
        if DemoLandUseDefinition.objects.count() == 0:
            logger.info("Loading DEMO land use definitions")
            fixture_path = os.path.join(settings.ROOT_PATH, 'footprint', 'client', 'configuration',
                                        'demo', 'built_form', 'demo_land_use_definitions.json')
            call_command('loaddata', fixture_path)
        else:
            logger.info("Skipping because of " + str(DemoLandUseDefinition.objects.count()) + " objects already there")

    def groups(self):
        return self.parent_fixture.groups()

    def users(self):
        return self.parent_fixture.users()
