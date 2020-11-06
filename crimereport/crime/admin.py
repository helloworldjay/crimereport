from django.contrib import admin
from .models import Congressperson # Region

# Register your models here.
@admin.register(Congressperson)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'district', 'crimes', 'photo', 'elected_num']

# @admin.register(Region)
# class UserAdmin(admin.ModelAdmin):
#     # list_display = ['id','city', 'district', 'detail']
#     pass

# @admin.register(City)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id','name']
# @admin.register(District)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id','name']
# @admin.register(Detail)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id','name']