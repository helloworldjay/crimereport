from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('postList/',views.postList, name='postList'),
    path('postList/<int:post_id>/',views.detailPost, name='detailPost'),
    path('postList/<int:post_id>/input_comment/',views.input_comment, name='input_comment'),
]
