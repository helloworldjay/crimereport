from django.contrib import admin
from .models import Profile # Region

# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = []
