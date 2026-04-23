from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home do app')

# Create your views here.
