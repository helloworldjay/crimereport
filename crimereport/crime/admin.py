from django.contrib import admin
from .models import Congressperson, City, District, Detail

# Register your models here.
@admin.register(Congressperson)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'constituency_city', 'constituency_district','constituency_detail','crimes', 'photo', 'elected_num']

@admin.register(City)
class UserAdmin(admin.ModelAdmin):
    list_display = ['city']
@admin.register(District)
class UserAdmin(admin.ModelAdmin):
    list_display = ['district']
@admin.register(Detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ['detail']