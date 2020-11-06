from django.shortcuts import render
from .models import Congressperson
from .serializer import CongresspersonSerializer
from rest_framework import viewsets, mixins, generics
from django.views.generic import DetailView, ListView


#CBV

# class CongressViewSet(viewsets.ModelViewSet):
#     queryset = Congressperson.objects.all()
#     serializer_class = CongresspersonSerializer


# class CongressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Congressperson.objects.all()
#     serializer_class = CongresspersonSerializer
    
class CongressListView(ListView):
    model = Congressperson
    template_name = 'crime/index.html'
    context_object_name = "congresslist"  


    def get_queryset(self):
        return Congressperson.objects.all() 

class CongressDetailView(DetailView):
    model = Congressperson
    template_name = 'crime/index.html'
    context_object_name = "congresslist"  


    def get_queryset(self, district):
        return Congressperson.objects.get(pk=district) 

