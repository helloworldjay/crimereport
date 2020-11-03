from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('crime', views.CongressViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
]
