from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),

    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('', include('allauth.urls')),
    path('profileedit/', views.profile_edit, name='profile_edit'),
    path('passwordedit/', views.password_edit, name='password_edit'),
    path('delete/', views.delete, name='delete'),
    path('developer/', views.developer, name="developer"),
]
