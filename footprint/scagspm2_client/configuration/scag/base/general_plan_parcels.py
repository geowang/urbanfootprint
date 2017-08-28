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
from django.contrib.gis.db import models
from footprint.main.models.geospatial.feature import Feature
from django.db.models import DateTimeField

__author__ = 'calthorpe_associates'


class GeneralPlanParcels(Feature):

    apn = models.CharField(max_length=100, null=True, blank=True)
    fips = models.IntegerField(null=True)
    scaguid12 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    density = models.DecimalField(max_digits=14, decimal_places=2)
    low = models.DecimalField(max_digits=14, decimal_places=2)
    high = models.DecimalField(max_digits=14, decimal_places=2)
    year_adopted = models.CharField(max_length=100, null=True, blank=True)
    city_gp_code = models.CharField(max_length=100, null=True, blank=True)
    zone_code = models.CharField(max_length=100, null=True, blank=True)
    scag_gp_code = models.IntegerField(null=True, blank=True)

    class Meta(object):
        abstract = True
        app_label = 'main'
