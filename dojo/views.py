from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))
    return HttpResponse(result)
