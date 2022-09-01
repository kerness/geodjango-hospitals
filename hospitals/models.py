from unittest import mock
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

class Hospital(models.Model):
    name = models.CharField(("Hospital Name"), max_length=100)
    lon = models.FloatField(("Longitude"))
    lat = models.FloatField(("Latitude"))
    fid = models.IntegerField(("Field ID"))
    beds = models.IntegerField(("Bed Numbers"), default=1)
    province_name = models.CharField(("Province"), max_length=100)
    province_code = models.CharField(("Province Code"), max_length=1)
    geom = models.PointField(srid=4326)

    def __str__(self) -> str:
        return self.name