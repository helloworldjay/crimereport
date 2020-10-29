from django.shortcuts import render
from .models import Congressperson
from .serializer import CongresspersonSerializer
from rest_framework import viewsets

#CBV

class CongressViewSet(viewsets.ModelViewSet):
    queryset = Congressperson.objects.all()
    serializer_class = CongresspersonSerializer
