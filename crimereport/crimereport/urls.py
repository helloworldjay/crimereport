from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crime.urls')),
    path('post/',include('post.urls')),
]
