from django.db import models

class Data(models.Model):
    group = models.IntegerField()
    lat = models.DecimalField(max_digits=200,decimal_places=20)
    lon = models.DecimalField(max_digits=200,decimal_places=20)
    color = models.CharField(max_length=200)
    ang = models.DecimalField(max_digits=200,decimal_places=20)
    radius = models.IntegerField()
