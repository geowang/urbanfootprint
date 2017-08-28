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

__author__ = 'calthorpe_associates'


class CpadHoldings(Feature):
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    unit_name = models.CharField(max_length=100, null=True, blank=True)
    access_type = models.CharField(max_length=100, null=True, blank=True)
    acres = models.DecimalField(max_digits=10, decimal_places=2)
    county = models.CharField(max_length=100, null=True, blank=True)
    agency_level = models.CharField(max_length=100, null=True, blank=True)
    agency_website = models.CharField(max_length=300, null=True, blank=True)
    site_website = models.CharField(max_length=300, null=True, blank=True)
    layer = models.CharField(max_length=100, null=True, blank=True)
    management_agency = models.CharField(max_length=100, null=True, blank=True)
    label_name = models.CharField(max_length=100, null=True, blank=True)
    ownership_type = models.CharField(max_length=100, null=True, blank=True)
    site_name = models.CharField(max_length=100, null=True, blank=True)
    alternate_site_name = models.CharField(max_length=100, null=True, blank=True)
    land_water = models.CharField(max_length=100, null=True, blank=True)
    specific_use = models.CharField(max_length=100, null=True, blank=True)
    hold_notes = models.CharField(max_length=320, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    designation_agency = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    primary_purpose = models.CharField(max_length=100, null=True, blank=True)
    apn = models.CharField(max_length=100, null=True, blank=True)
    holding_id = models.CharField(max_length=100, null=True, blank=True)
    unit_id = models.CharField(max_length=100, null=True, blank=True)

    superunit = models.CharField(max_length=100, null=True, blank=True)
    agency_id = models.CharField(max_length=100, null=True, blank=True)
    mng_ag_id = models.CharField(max_length=100, null=True, blank=True)
    al_av_parc = models.CharField(max_length=100, null=True, blank=True)
    date_revised = models.CharField(max_length=100, null=True, blank=True)
    src_align = models.CharField(max_length=100, null=True, blank=True)
    src_attr = models.CharField(max_length=100, null=True, blank=True)
    d_acq_yr = models.CharField(max_length=100, null=True, blank=True)


    class Meta(object):
        abstract = True
        app_label = 'main'

