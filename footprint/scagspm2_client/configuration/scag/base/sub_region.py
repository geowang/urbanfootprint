from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class SubRegion(Feature):

    subregion = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    county_id = models.IntegerField(null=False)
    acres = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta(object):
        abstract = True
        app_label = 'main'