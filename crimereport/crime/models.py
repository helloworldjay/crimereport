from django.db import models


class Congressperson(models.Model):
    name = models.CharField(max_length=50)   
    district = models.CharField(max_length=1000, default=None)
    crimes = models.TextField(blank=True)
    penalty = models.CharField(max_length=100)
    photo = models.CharField(max_length=100) # image directory
    elected_num = models.IntegerField(default=0)
    party = models.CharField(max_length=50)

