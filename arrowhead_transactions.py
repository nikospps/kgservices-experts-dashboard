import folium
from collections import namedtuple
import numpy as np
import math
########################################################################################################################
def getArrows(locations, color='blue', size=6, n_arrows=3):
    '''
    Get a list of placed and rotated arrows or markers to be plotted

    Parameters
    locations : list of lists of latitude longitude that represent the begining and end of Line.
                    this function Return list of arrows or the markers
    '''

    Point = namedtuple('Point', field_names=['lat', 'lon'])

    # creating point from Point named tuple
    point1 = Point(locations[0][0], locations[0][1])
    point2 = Point(locations[1][0], locations[1][1])

    # calculate the rotation required for the marker.
    # Reducing 90 to account for the orientation of marker
    # Get the degree of rotation
    angle = get_angle(point1, point2) - 90

    # get the evenly space list of latitudes and longitudes for the required arrows

    arrow_latitude = np.linspace(point1.lat, point2.lat, n_arrows + 2)[1:n_arrows + 1]
    arrow_longitude = np.linspace(point1.lon, point2.lon, n_arrows + 2)[1:n_arrows + 1]

    final_arrows = []

    # creating each "arrow" and appending them to our arrows list
    for points in zip(arrow_latitude, arrow_longitude):
        final_arrows.append(folium.RegularPolygonMarker(location=points,
                                                        fill_color=color, number_of_sides=3,
                                                        radius=size, rotation=angle))
    return final_arrows

def get_angle(p1, p2):
    '''
    This function Returns angle value in degree from the location p1 to location p2

    Parameters it accepts :
    p1 : namedtuple with lat lon
    p2 : namedtuple with lat lon

    This function Return the vlaue of degree in the data type float

    Pleae also refers to for better understanding : https://gist.github.com/jeromer/2005586
    '''

    longitude_diff = np.radians(p2.lon - p1.lon)

    latitude1 = np.radians(p1.lat)
    latitude2 = np.radians(p2.lat)

    x_vector = np.sin(longitude_diff) * np.cos(latitude2)
    y_vector = (np.cos(latitude1) * np.sin(latitude2)
                - (np.sin(latitude1) * np.cos(latitude2)
                   * np.cos(longitude_diff)))
    angle = np.degrees(np.arctan2(x_vector, y_vector))

    # Checking and adjustring angle value on the scale of 360
    if angle < 0:
        return angle + 360
    return angle

def find_distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance_bw_ori_desti = radius * c
    return distance_bw_ori_desti
########################################################################################################################
# from geopy.geocoders import Nominatim
# g = Nominatim(user_agent="new")
# location = g.geocode("Via delle Robinie 120-144 Rome")
#
# print([location.latitude, location.longitude])

# import address_geolocation

# find_distance((37.98070976484463,23.779292842117954),(37.97935862891567,23.783352669822474))
#
# from geopy.distance import geodesic
#
#
# origin = (30.172705, 31.526725)  # (latitude, longitude) don't confuse
# dist = (30.288281, 31.732326)
#
# print(geodesic((37.98070976484463,23.779292842117954),(37.97935862891567,23.783352669822474)).meters)
# print(find_distance((37.98070976484463,23.779292842117954),(37.97935862891567,23.783352669822474))*1000)#in meters