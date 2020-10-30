from django.contrib import admin
from .models import Congressperson, City, District, Detail

# Register your models here.
@admin.register(Congressperson)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'city_name', 'district_name','detail_name','crimes', 'photo', 'elected_num']

@admin.register(City)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(District)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name']
@admin.register(Detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name']