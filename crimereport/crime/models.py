from django.db import models

class Region(models.Model):
    city = models.CharField(blank=False, null = False, max_length=50) #지역구 시
    district = models.CharField(blank=True, null = True, max_length=50) #지역구 구
    detail = models.CharField(blank=True, null = True, max_length=50) #지역구 갑/을/병
    
    
    def __str__(self):
        return f'{self.city} | {self.district} | {self.detail}'

class Congressperson(models.Model):
    name = models.CharField(max_length=50)
    city= models.ForeignKey('crime.Region',on_delete=models.CASCADE) #지역구   
    crimes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img',blank=True)
    elected_num = models.IntegerField(default=0)
    party = models.CharField(max_length=50)

class Newspaper(models.Model):
    photo = models.ImageField(upload_to='img',blank=True)
