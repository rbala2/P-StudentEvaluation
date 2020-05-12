from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def portal_home(request):
    return render(request, 'PortalHome/index.html')
