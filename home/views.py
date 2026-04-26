from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(
        'Blog do app 2')

# Create your views here.
