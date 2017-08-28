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

from footprint.client.configuration.fixture import BuiltFormFixture, LandUseSymbologyFixture
from footprint.client.configuration.scag.built_form.scag_land_use import ScagLandUse
from footprint.client.configuration.scag.built_form.scag_land_use_definition import ScagLandUseDefinition
from footprint.client.configuration.utils import resolve_fixture
from footprint.main.lib.functions import merge
from footprint.main.models.config.region import Region
from footprint.main.models.built_form.urban.building_type import BuildingType
from footprint.main.models.built_form.built_form import update_or_create_built_form_medium
from django.conf import settings
from footprint.main.utils.fixture_list import FixtureList


class ScagBuiltFormFixture(BuiltFormFixture):
    def built_forms(self):
        def construct_scag_land_uses():

            land_use_symbology_fixture = resolve_fixture(
                "presentation",
                "land_use_symbology",
                LandUseSymbologyFixture,
                settings.CLIENT)
            land_use_lookup = land_use_symbology_fixture.land_use_color_lookup()

            return map(
                lambda land_use_definition: ScagLandUse.objects.update_or_create(
                    key='scag_lu__' + slugify(land_use_definition.land_use).replace('-', '_'),
                    defaults=dict(
                        creator=get_user_model().objects.get(username='admin'),
                        updater=get_user_model().objects.get(username='admin'),

                        name=land_use_definition.land_use,
                        land_use_definition=land_use_definition,
                        medium=update_or_create_built_form_medium(
                            'scag_land_use_%s' % land_use_definition.land_use,
                            land_use_lookup.get(land_use_definition.land_use, None)
                        )
                    ))[0],
                ScagLandUseDefinition.objects.all())

        return merge(
            self.parent_fixture.built_forms(),
            dict(scag_land_use=construct_scag_land_uses()))

    def tag_built_forms(self, built_forms_dict):
        self.parent_fixture.tag_built_forms(built_forms_dict),

    def built_form_sets(self):
        return self.parent_fixture.built_form_sets() + FixtureList([
            dict(
                scope=Region,
                key='scag_land_uses',
                attribute='scag_land_use_definition',
                name='SCAG Land Uses',
                description='SCAG Land Use Codes',
                client='scag',
                clazz=BuildingType,
            ),
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
