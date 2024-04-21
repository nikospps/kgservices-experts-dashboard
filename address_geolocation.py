import json
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3
# sys.setrecursionlimit(10000)

# with open('CXB_test.json') as json_file:
#     cxb = json.load(json_file)

def reverse(dataset_name,locations=[],pan_idL=[],purchase_amountL=[],operation_shipaddressL=[]):
    geolocator = Nominatim(user_agent="nik")  # You can tryout ArcGIS or GoogleV3 APIs to compare the results
    from geopy.extra.rate_limiter import RateLimiter
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=5)
    # dataset_coord=[[37.98821911211416, 23.758954233371924], [37.97586978120721, 23.772363633371555],[37.97777989138945, 23.761976691042875],[41.882559026513526, 12.568336962324969]]
    for i in range(len(dataset_name)):
        # location = geocode(dataset_name[i]["operation"]["shipAddress"] + ' ' + dataset_name[i]["operation"]["shipAddrCity"])
        lat = float(dataset_name[i]['geo_ip']['latitude'])
        lon = float(dataset_name[i]['geo_ip']['longitude'])
        lat1 = dataset_name[i]["operation"]["ship_lat"]
        lon1 = dataset_name[i]["operation"]["ship_lon"]
        pan_id = dataset_name[i]["panInfo"]["id"]
        purchase_amount = dataset_name[i]['purchaseInfo']["purchaseAmount"]
        operation_shipaddress = dataset_name[i]["operation"]["shipAddress"] + ',' + dataset_name[i]["operation"]["shipAddrCity"] + ',' + \
                                 dataset_name[i]["operation"]["shipAddrPostCode"] + ',' + dataset_name[i]["operation"]["shipAddrCountry"]
        # locations.append([[lat, lon], [location.latitude, location.longitude]])
        locations.append([[lat, lon], [lat1, lon1]])
        pan_idL.append(pan_id)
        purchase_amountL.append(purchase_amount)
        operation_shipaddressL.append(operation_shipaddress)
    return locations, pan_idL,purchase_amountL, operation_shipaddressL