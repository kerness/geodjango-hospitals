from django.contrib.gis.db import models


class Boundary(models.Model):
    adm0_en = models.CharField(max_length=254)
    adm0_pcode = models.CharField(max_length=254)
    name = models.CharField(('Province Name'), max_length=254)
    pcode = models.CharField(('Province Code'), max_length=1)
    mpoly = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Boundaries'

    def __str__(self) -> str:
        return self.name
