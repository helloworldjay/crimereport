from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Congressperson
from django.views.generic import DetailView, ListView
import json
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from pathlib import Path
import os


class CongressListView(ListView):
    model = Congressperson
    template_name = 'crime/index.html'
    context_object_name = "congresslist"  

def search(request, district):
    info_object = Congressperson.objects.get(district=district)
    if info_object:
        to_json = model_to_dict(info_object)
        return JsonResponse(to_json)
