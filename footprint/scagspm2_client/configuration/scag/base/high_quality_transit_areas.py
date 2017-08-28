from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class HighQualityTransitAreas(Feature):
    city = models.CharField(max_length=50, null=False)
    county = models.CharField(max_length=50, null=False)
    county_id = models.IntegerField(null=False)


    class Meta(object):
        abstract = True
        app_label = 'main'
