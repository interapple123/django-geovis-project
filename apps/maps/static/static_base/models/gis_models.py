from django.contrib.gis.db import models as models

class AlurPelayaran(models.Model):
    objectid = models.BigIntegerField()
    namobj = models.CharField(max_length=250)
    orde01 = models.BigIntegerField()
    orde02 = models.BigIntegerField()
    orde03 = models.BigIntegerField()
    orde04 = models.BigIntegerField()
    jnsrsr = models.BigIntegerField()
    stsjrn = models.BigIntegerField()
    wadmpr = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    sbdata = models.CharField(max_length=250)
    keterangan = models.CharField(max_length=250, blank=True, null=True)
    km = models.FloatField()
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.namobj

    class Meta:
        verbose_name = "Alur Pelayaran"
        verbose_name_plural = "Alur Pelayaran"
        ordering = ["objectid"]

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class KabelBawahLaut(models.Model):
    objectid = models.BigIntegerField(null=True, blank=True)
    namobj = models.CharField(max_length=250, null=True, blank=True)
    orde01 = models.BigIntegerField(null=True, blank=True)
    orde02 = models.BigIntegerField(null=True, blank=True)
    orde03 = models.BigIntegerField(null=True, blank=True)
    orde04 = models.BigIntegerField(null=True, blank=True)
    jnsrsr = models.BigIntegerField(null=True, blank=True)
    stsjrn = models.BigIntegerField(null=True, blank=True)
    wadmpr = models.CharField(max_length=250, null=True, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)
    sbdata = models.CharField(max_length=250, null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    keterangan = models.CharField(max_length=90, null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.namobj

    class Meta:
        verbose_name = "Kabel Bawah Laut"
        verbose_name_plural = "Kabel Bawah Laut"
        ordering = ["objectid"]

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Migas(models.Model):
    objectid = models.BigIntegerField(null=True, blank=True)
    namobj = models.CharField(max_length=250, null=True, blank=True)
    orde01 = models.BigIntegerField(null=True, blank=True)
    orde02 = models.BigIntegerField(null=True, blank=True)
    orde03 = models.BigIntegerField(null=True, blank=True)
    orde04 = models.BigIntegerField(null=True, blank=True)
    jnsrsr = models.BigIntegerField(null=True, blank=True)
    stsjrn = models.BigIntegerField(null=True, blank=True)
    wadmpr = models.CharField(max_length=250, null=True, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)
    sbdata = models.CharField(max_length=250, null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.namobj

    class Meta:
        verbose_name = "Migas"
        verbose_name_plural = "Migas"
        ordering = ["objectid"]
