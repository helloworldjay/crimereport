from django.contrib import admin
<<<<<<< HEAD
from .models import Profile # Region

# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = []
=======
from .models import Profile
# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id']
>>>>>>> 02e15822065e770fdae67f97f3289754f761b1d7
