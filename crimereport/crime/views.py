from django.shortcuts import render
from .models import Congressperson
from .serializer import CongresspersonSerializer
from rest_framework import viewsets

#CBV

class CongressViewSet(viewsets.ModelViewSet):
    queryset = Congressperson.objects.all()
    serializer_class = CongresspersonSerializer

def test(request):
    return render(request, 'crime/blog.html', {})

def index(request):
    return render(request, 'crime/index.html', {})