from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class Farmland(Feature):
    city = models.CharField(max_length=50, null=False)
    county = models.CharField(max_length=50, null=False)
    update_year = models.IntegerField(null=False)
    polygon_fy = models.CharField(max_length=50, null=False)


    class Meta(object):
        abstract = True
        app_label = 'main'
