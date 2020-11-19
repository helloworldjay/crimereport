from django.shortcuts import render
from django.views.generic import ListView
from crimereport.crime import models
# Create your views here.


def postList(request):
    return render(request, 'post/postList.html', {})

class postList(ListView):
    paginate_by = 2
