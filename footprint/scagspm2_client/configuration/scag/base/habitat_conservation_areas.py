from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class HabitatConservationAreas(Feature):
    name = models.CharField(max_length=50, null=False)
    hcp = models.CharField(max_length=50, null=False)
    nccp = models.CharField(max_length=50, null=False)
    stage = models.CharField(max_length=50, null=False)

    class Meta(object):
        abstract = True
        app_label = 'main'
