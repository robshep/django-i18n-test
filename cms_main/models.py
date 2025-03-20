from django.db import models

# Create your models here.


class Rock(models.Model):
    name = models.CharField(max_length=200)
    descr_en = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    num_holes = models.IntegerField()
