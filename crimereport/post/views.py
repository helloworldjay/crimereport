from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def dummy(request: HttpRequest) -> HttpResponse :
    return HttpResponse("hello")