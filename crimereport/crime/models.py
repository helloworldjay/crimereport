from django.db import models

class City(models.Model):
    city = models.CharField(blank=False, null = False, max_length=50) #지역구 시

class District(models.Model):
    district = models.CharField(blank=False, null = False, max_length=50) #지역구 구

class Detail(models.Model):
    detail = models.CharField(blank=False, null = False, max_length=50) #지역구 갑/을/병

class Congressperson(models.Model):
    name = models.CharField(max_length=50)
    constituency_city = models.ForeignKey(City,on_delete=models.CASCADE, related_name="c_city") #지역구 시
    constituency_district = models.ForeignKey(District,on_delete=models.CASCADE, related_name="c_district") #지역구 구
    constituency_detail = models.ForeignKey(Detail,on_delete=models.CASCADE, related_name="c_detail") #지역구 갑/을/병
    crimes = models.TextField(blank=True)
    photo = models.ImageField(upload_to='img',blank=True)
    elected_num = models.IntegerField(default=0)
    party = models.CharField(max_length=50)

class Newspaper(models.Model):
    photo = models.ImageField(upload_to='img',blank=True)
