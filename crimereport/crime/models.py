from django.db import models


class Congressperson(models.Model):
    name = models.CharField(max_length=50)   
    district = models.CharField(max_length=100, default=None)
    crimes = models.TextField(blank=True)
    photo = models.CharField(max_length=100) # image directory
    elected_num = models.IntegerField(default=0)
    party = models.CharField(max_length=50)

