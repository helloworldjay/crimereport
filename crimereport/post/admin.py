from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    display_list = ['user','title']