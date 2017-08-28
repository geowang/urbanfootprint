from django.contrib.gis.db import models

from footprint.main.models.geospatial.feature import Feature

__author__ = 'calthorpe_associates'


class EndangeredSpecies(Feature):
    species_name = models.CharField(max_length=50, null=False)
    common_name = models.CharField(max_length=50, null=False)
    elmcode = models.CharField(max_length=50, null=False)
    occnumber = models.CharField(max_length=50, null=False)

    kquadname = models.CharField(max_length=50, null=False)
    county_key = models.CharField(max_length=50, null=False)
    accuracy = models.CharField(max_length=50, null=False)

    presence = models.CharField(max_length=50, null=False)
    occtype = models.CharField(max_length=50, null=False)
    callist = models.CharField(max_length=50, null=False)

    location = models.CharField(max_length=50, null=False)
    location_details = models.CharField(max_length=50, null=False)
    ecological = models.CharField(max_length=50, null=False)

    threat = models.CharField(max_length=50, null=False)
    general = models.CharField(max_length=50, null=False)
    symbology = models.CharField(max_length=50, null=False)
    

    class Meta(object):
        abstract = True
        app_label = 'main'
