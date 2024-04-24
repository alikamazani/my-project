from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from datetime import datetime
from .models import GetDataSynop_main

# Import Find Locations Ip,Latitude,Longitude
from geopy.geocoders import Nominatim
import socket

# Create your views here.

def getInfoSynop(request):
    
    return render(request, 'getinfo_synop.html')

def getInfoClima(request):
    # find locatin lat,lon
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("tehran")
    locationName = print(getLoc.address)
    latitudeNum = print(getLoc.latitude)
    longitudeNum = print(getLoc.longitude)
    print(locationName, latitudeNum, longitudeNum)
    # find host,ip address
    hostName = socket.gethostname()
    ipAddress = socket.gethostbyname(hostName)
    print('Host Name : {0}'.format(hostName))
    print('Host Name : {0}'.format(ipAddress))

    return render(request, 'getinfo_clima.html')

def getInfoAgric(request):
    return render(request, 'getinfo_agric.html')

