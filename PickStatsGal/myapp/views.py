from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponse

# Create your views here.

def index(request):
    ##return HttpResponse("Hello, world!")
    ##print ("Hello, world!")
    return FileResponse(open("../PickStatsGal1.jpeg", "rb"))
