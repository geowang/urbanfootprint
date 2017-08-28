# coding=utf-8
# UrbanFootprint-California (v1.0), Land Use Scenario Development and Modeling System.
#
# Copyright (C) 2012 Calthorpe Analytics
#
# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Contact: Joe DiStefano (joed@calthorpe.com), Calthorpe Analytics.
# Firm contact: 2095 Rose Street Suite 201, Berkeley CA 94709.
# Phone: (510) 548-6800. Web: www.calthorpe.com
from footprint.main.managers.geo_inheritance_manager import GeoInheritanceManager
from footprint.main.models.built_form.client_land_use_definition import ClientLandUseDefinition

__author__ = 'calthorpe_associates'

from django.db import models

class ScagLandUseDefinition(ClientLandUseDefinition):
    objects = GeoInheritanceManager()
    land_use_description = models.CharField(max_length=100, null=True, blank=True)
    land_use_type = models.CharField(max_length=100, null=True, blank=True)
    # The id imported from Scag
    land_use = models.IntegerField(null=False)

    @property
    def label(self):
        return self.land_use_description

    class Meta(object):
        abstract = False
        app_label = 'main'
