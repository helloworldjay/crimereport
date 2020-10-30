from django.db import models

class City(models.Model):
    name = models.CharField(blank=False, null = False, max_length=50) #지역구 시

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(blank=False, null = False, max_length=50) #지역구 구

    
    def __str__(self):
        return self.name

class Detail(models.Model):
    name = models.CharField(blank=False, null = False, max_length=50) #지역구 갑/을/병

    
    def __str__(self):
        return self.name

class Congressperson(models.Model):
    name = models.CharField(max_length=50)
    city_name = models.ForeignKey('crime.City',on_delete=models.CASCADE) #지역구 시
    district_name = models.ForeignKey('crime.District',on_delete=models.CASCADE) #지역구 구
    detail_name = models.ForeignKey('crime.Detail',on_delete=models.CASCADE) #지역구 갑/을/병
    crimes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img',blank=True)
    elected_num = models.IntegerField(default=0)
    party = models.CharField(max_length=50)

class Newspaper(models.Model):
    photo = models.ImageField(upload_to='img',blank=True)
