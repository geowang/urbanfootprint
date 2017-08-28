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
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

from footprint.client.configuration.fixture import BuiltFormFixture
from footprint.main.lib.functions import merge
from footprint.main.models.config.region import Region
from footprint.main.models.built_form.urban.building_type import BuildingType
from footprint.main.models.built_form.urban.urban_placetype import UrbanPlacetype
from django.conf import settings
from footprint.main.utils.fixture_list import FixtureList


class DemoBuiltFormFixture(BuiltFormFixture):
    def built_forms(self):
        return merge(
            self.parent_fixture.built_forms(client=settings.CLIENT),
            self.parent_fixture.built_forms())

    def tag_built_forms(self, built_forms_dict):
        self.parent_fixture.tag_built_forms(built_forms_dict),

    def built_form_sets(self):
        return self.parent_fixture.built_form_sets() + FixtureList([
            dict(
                scope=Region,
                key='demo_building_type',
                attribute='building_attribute_set',
                name='DEMO Buildingtypes',
                description='Built Forms for DEMO',
                client='demo',
                clazz=BuildingType,
            ),
            dict(
                scope=Region,
                key='demo_urban_placetype',
                name='DEMO Placetypes',
                attribute='building_attribute_set',
                description='Built Forms for DEMO',
                client='demo',
                clazz=UrbanPlacetype,
            ),
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
