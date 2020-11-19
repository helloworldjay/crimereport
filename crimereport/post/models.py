from django.db import models
from django.conf import settings
from accounts.models import Profile
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
