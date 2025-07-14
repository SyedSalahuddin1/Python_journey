import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.reverse("-42.7038, -24.6795", exactly_one=True, timeout=10)

if location:
    print(location.address)
else:
    print("Location not found")
