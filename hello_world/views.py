from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)