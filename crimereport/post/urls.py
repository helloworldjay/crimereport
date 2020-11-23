from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('postlist/',views.postList, name='postlist'),
    path('postlist/<int:post_id>/',views.detailPost, name='detailpost'),
    path('postlist/<int:post_id>/input_comment/',views.input_comment, name='input_comment'),
    path('new/', views.post_new, name='post_new'),
]
