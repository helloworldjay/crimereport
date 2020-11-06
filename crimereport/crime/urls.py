from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('crime', views.CongressViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.CongressListView.as_view(), name='congresslist'),
    path('<str:district>/', views.CongressDetailView.as_view(), name='congressdetail'),
]
