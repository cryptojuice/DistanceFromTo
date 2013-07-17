"""
This module uses the haversine forumla to find the distance between
two locations

Usage:

python distancebetween "New York" "California"

"""

import sys
import math
from pygeocoder import Geocoder


def haversine(lat1, lon1, lat2, lon2):
    """
    Use haversine to find distance between two coordinates
    """

    earths_radius = 6372.8
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    a = math.sin(dlat/2)**2 + math.sin(dlon/2)**2 * math.cos(lat1)\
            * math.cos(lat2)
    c = 2 * math.asin(math.sqrt(a))
    return earths_radius * c



if __name__ == '__main__':

    START = Geocoder.geocode(sys.argv[1])
    END = Geocoder.geocode(sys.argv[2])

    DKM = haversine(START.latitude, START.longitude, END.latitude,
            END.longitude)
    DMI = haversine(START.latitude, START.longitude, END.latitude, 
            END.longitude) * 0.62137

    print("Start Location: {0}\n End: location: {1}\n Distance: {2} km ({3} mi\
        les)".format(START.formatted_address, END.formatted_address
            ,round(DKM) ,round(DMI)))
