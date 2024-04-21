from pymongo import MongoClient
import datetime

def fitbitsleep():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['fitbitsleep'] #connect to specific collection(table)
    return collection

# a={
#   "awakeCount" : 2.0,
#   "awakeDuration" : 6.0,
#   "awakeningsCount" : 20.0,
#   "duration" : 2.826E7,
#   "efficiency" : 88.0,
#   "isMainSleep" : True,
#   "logId" : 3.7531877E10,
#   "minutesAfterWakeup" : 0.0,
#   "minutesAsleep" : 415.0,
#   "minutesAwake" : 56.0,
#   "minutesToFallAsleep" : 0.0,
#   "restlessCount" : 18.0,
#   "restlessDuration" : 50.0,
#   "timeInBed" : 471.0,
#   "deep" : 76.0,
#   "light" : 210.0,
#   "wake" : 63.0,
#   "rem" : 122.0,
#   "dateOfSleep" : 1657065600000,
#   "startTime" : 1657061070000,
#   "endTime" : 1657089330000,
#   "patient_uuid" : ''
# }
#
# collection = fitbitsleep()
#
# # collection.insert_one(a)
#
# cursor = collection.find({})
#
# for n in cursor:
#   print(n['awakeDuration'])