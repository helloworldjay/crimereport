from django.contrib.auth.views import LoginView
from importlib.resources import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),    
]
