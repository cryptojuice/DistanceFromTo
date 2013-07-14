import sys
import math
from pygeocoder import Geocoder

def haversine(lat1, lon1, lat2, lon2):
	R = 6372.8
	dLat = math.radians(lat2-lat1)
	dLon = math.radians(lon2-lon1)
	lat1 = math.radians(lat1)
	lat2 = math.radians(lat2)

	a = math.sin(dLat/2)**2 + math.sin(dLon/2)**2 * math.cos(lat1) * math.cos(lat2)
	c = 2 * math.asin(math.sqrt(a))
	return R * c


if __name__ == '__main__':

  start = Geocoder.geocode(sys.argv[1])
  end = Geocoder.geocode(sys.argv[2])

  dkm = haversine(start.latitude, start.longitude, end.latitude, end.longitude)
  dmi = haversine(start.latitude, start.longitude, end.latitude, end.longitude) * 0.62137

  print("Start Location: {0}\n End: location: {1}\n Distance: {2} km ({3} miles)".format(start.formatted_address, end.formatted_address,round(dkm),round(dmi)))