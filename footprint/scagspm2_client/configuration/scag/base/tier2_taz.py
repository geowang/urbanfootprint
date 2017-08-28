from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class Tier2Taz(Feature):
    fips = models.IntegerField(null=False)
    city = models.CharField(max_length=50, null=False)
    subregion = models.CharField(max_length=50, null=False)
    subregion_id = models.IntegerField(null=False)
    county = models.CharField(max_length=50, null=False)
    county_id = models.IntegerField(null=False)
    tier2 = models.CharField(max_length=50, null=False)
    ct2 = models.CharField(max_length=50, null=False)
    pop12 = models.DecimalField(max_digits=14, decimal_places=2)
    pop20 = models.DecimalField(max_digits=14, decimal_places=2)
    pop35 = models.DecimalField(max_digits=14, decimal_places=2)
    pop40 = models.DecimalField(max_digits=14, decimal_places=2)
    hh12 = models.DecimalField(max_digits=14, decimal_places=2)
    hh20 = models.DecimalField(max_digits=14, decimal_places=2)
    hh35 = models.DecimalField(max_digits=14, decimal_places=2)
    hh40 = models.DecimalField(max_digits=14, decimal_places=2)
    emp12 = models.DecimalField(max_digits=14, decimal_places=2)
    emp20 = models.DecimalField(max_digits=14, decimal_places=2)
    emp35 = models.DecimalField(max_digits=14, decimal_places=2)
    emp40 = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta(object):
        abstract = True
        app_label = 'main'
