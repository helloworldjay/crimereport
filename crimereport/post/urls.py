from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('postlist/',views.postlist, name='postlist'),
    path('postlist/<int:post_id>/',views.detailpost, name='detailpost'),
    # path('postlist/<int:post_id>/inputcomment/',views.input_comment, name='inputcomment'),
]
