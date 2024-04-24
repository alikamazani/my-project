import phonenumbers
import folium
import target
import socket
from phonenumbers import geocoder
key = '065f1de3c6404bd79f6eea1e2d51c991'
number = input('Enter A Phone Number :')
theNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(theNumber, "en")
print(yourLocation)
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']
print(lat, long)
# وارد کردن طول و عرض جغرافیایی و دادن نام
from geopy.geocoders import Nominatim
geoLoc = Nominatim(user_agent="GetLoc")
locName = geoLoc.reverse(f"{lat}, {long}")
print(locName.address)