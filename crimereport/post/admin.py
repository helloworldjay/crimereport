from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    display_list = ['author','title','photo','text','created','updated']
    readonly_fields = ('created', 'updated')