from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.

def index(request):
    return HttpResponse("This would be the about page")

def about_me(request):
    return HttpResponse("This would be the about me page")


