from pymongo import MongoClient
import datetime

def fitbitheartimeline():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['fitbitheartimeline'] #connect to specific collection(table)
    return collection

# a= {
#   "date_time" : 1656979200000,
#   "resting_heart_rate" : 66.0,
#   "period" : "ONE_DAY",
#   "heart_rate_zones" : [ {
#     "max" : 139.0,
#     "min" : 114.0,
#     "minutes" : 4.0,
#     "name" : "FAT_BURN"
#   }, {
#     "max" : 169.0,
#     "min" : 139.0,
#     "minutes" : 0.0,
#     "name" : "CARDIO"
#   }, {
#     "max" : 220.0,
#     "min" : 169.0,
#     "minutes" : 0.0,
#     "name" : "PEAK"
#   }, {
#     "max" : 114.0,
#     "min" : 30.0,
#     "minutes" : 1436.0,
#     "name" : "OUT_OF_RANGE"
#   } ],
#   "patient_uuid" : "8152c89c-00d0-4694-84ef-6ef3d1c70463"
# }

#collection = fitbitheartimeline()

# collection.insert_one(a)

#cursor = collection.find({})

#for n in cursor:
#  print(n)
