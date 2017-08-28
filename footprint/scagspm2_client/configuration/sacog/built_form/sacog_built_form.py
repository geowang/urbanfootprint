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
from footprint.client.configuration.sacog.built_form.sacog_land_use_definition import SacogLandUseDefinition
from footprint.client.configuration.sacog.built_form.sacog_land_use import SacogLandUse
from footprint.client.configuration.utils import resolve_fixture
from footprint.main.lib.functions import merge
from footprint.main.models.config.region import Region
from footprint.main.models.built_form.urban.building_type import BuildingType
from footprint.main.models.built_form.urban.urban_placetype import UrbanPlacetype
from footprint.main.models.built_form.agriculture.crop_type import CropType
from footprint.main.models.built_form.built_form import update_or_create_built_form_medium
from footprint.main.utils.fixture_list import FixtureList
from django.conf import settings


RUCS_CROPTYPE_COLORS = {
    'Alfalfa': '#5A975A',
    'Alfalfa Rotation': '#33D685',
    'Almond': '#EEEECD',
    'Asparagus': '#759533',
    'Avocado': '#778E33',
    'Bean Dried': '#993300',
    'Blackberries': '#470047',
    'Blueberries': '#3333CC',
    'Broccoli': '#007A00',
    'Cherry': '#CC0052',
    'Corn For/FOD': '#FFFF00',
    'Diversified Farm-Fruit Trees': '#6B4724',
    "Diversified Farm-Fruit Trees, Vegetables": '#A6917C',
    'Diversified Farm-Vegetables': '#A37547',
    'Dried Bean': '#993300',
    'Fallow': '#B28F00',
    'Grape, Wine': '#6B0024',
    'No Data': '#CDCDCD',
    'Oats for/FOD': '#CCCCA3',
    'Pasture': '#B8E65C',
    'Prunes': '#895C89',
    'Rangeland': '#DBBF4D',
    'Rice Rotation': '#F5E0CC',
    'Safflower': '#FF9900',
    'Seed Rotation': '#E6CCFF',
    'Sorghum for/FOD': '#CC3300',
    'Squash': '#FFFF71',
    'Tomato Rotation': '#E60000',
    'Uncultivated Ag': '#474747',
    'Uncultivated Non-Ag': '#9b9b9b',
    'Walnuts': '#473119',
    'Wheat': '#FFCC00',
}

class SacogBuiltFormFixture(BuiltFormFixture):
    def built_forms(self):
        def construct_sacog_land_uses():

            land_use_symbology_fixture = resolve_fixture(
                "presentation",
                "land_use_symbology",
                LandUseSymbologyFixture,
                settings.CLIENT)
            land_use_lookup = land_use_symbology_fixture.land_use_color_lookup()

            return map(
                lambda land_use_definition: SacogLandUse.objects.update_or_create(
                    key='sac_lu__' + slugify(land_use_definition.land_use).replace('-', '_'),
                    defaults=dict(
                        creator=get_user_model().objects.get(username='admin'),
                        updater=get_user_model().objects.get(username='admin'),

                        name=land_use_definition.land_use,
                        land_use_definition=land_use_definition,
                        medium=update_or_create_built_form_medium(
                            'sacog_land_use_%s' % land_use_definition.land_use[30:],
                            land_use_lookup.get(land_use_definition.land_use, None)
                        )
                    ))[0],
                SacogLandUseDefinition.objects.all())

        return merge(
            self.parent_fixture.built_forms(client=settings.CLIENT),
            self.parent_fixture.built_forms(),
            dict(sacog_land_use=construct_sacog_land_uses()))
             #TODO determine the utility of this condition : #if isinstance(self.config_entity, Region) else {}
        # )

    def tag_built_forms(self, built_forms_dict):
        self.parent_fixture.tag_built_forms(built_forms_dict),
        # Give client built_forms a default tag if they don't have any tag yet
        # for built_form in built_forms_dict['sacog_land_use']:
        #     if built_form.tags.count() == 0:
        #         tag, created, updated = Tag.objects.update_or_create(
        #             tag=built_form.land_use_definition.land_use or 'Unsorted')
        #         built_form.tags.add(tag)

    def built_form_sets(self):
        return self.parent_fixture.built_form_sets() + FixtureList([
            # dict(
            #     scope=Region,
            #     key='sacog_buildings',
            #     name='SACOG Buildings',
            #     description='Built Forms for SACOG',
            #     attribute='building_attribute_set',
            #     client='sacog',
            #     clazz=Building,
            # ),
            dict(
                scope=Region,
                key='sacog_building_type',
                attribute='building_attribute_set',
                name='SACOG Buildingtypes',
                description='Built Forms for SACOG',
                client='sacog',
                clazz=BuildingType,
            ),
            dict(
                scope=Region,
                key='sacog_urban_placetype',
                name='SACOG Placetypes',
                attribute='building_attribute_set',
                description='Built Forms for SACOG',
                client='sacog',
                clazz=UrbanPlacetype,
            ),
            dict(
                scope=Region,
                key='sacog_rucs',
                name='RUCS Types',
                attribute='agriculture_attribute_set',
                description='SACOG RUCS types',
                client=False,
                clazz=CropType,
            ),
        ]).matching_scope(class_scope=self.config_entity and self.config_entity.__class__)
