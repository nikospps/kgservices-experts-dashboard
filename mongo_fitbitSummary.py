from pymongo import MongoClient
import datetime

def fitbitsummary():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['fitbitsummary'] #connect to specific collection(table)
    return collection

# a= {
#   "calories_bmr" : 1659.0,
#   "calories_out" : 2534.0,
#   "elevation" : 9.14,
#   "fairly_active_minutes" : 5.0,
#   "floors" : 3.0,
#   "lightly_active_minutes" : 246.0,
#   "marginal_calories" : 502.0,
#   "sedentary_minutes" : 820.0,
#   "steps" : 5780.0,
#   "very_active_minutes" : 5.0,
#   "start_date" : 1656979200000,
#   "end_date" : 1656979200000,
#   "distances" : [ {
#     "activity" : "sedentaryActive",
#     "distance" : 0.0
#   }, {
#     "activity" : "lightlyActive",
#     "distance" : 3.72
#   }, {
#     "activity" : "loggedActivities",
#     "distance" : 0.0
#   }, {
#     "activity" : "veryActive",
#     "distance" : 0.22
#   }, {
#     "activity" : "tracker",
#     "distance" : 4.08
#   }, {
#     "activity" : "moderatelyActive",
#     "distance" : 0.13
#   }, {
#     "activity" : "total",
#     "distance" : 4.08
#   } ],
#   "patient_uuid" : "8152c89c-00d0-4694-84ef-6ef3d1c70463"
# }
#
# collection = fitbitsummary()
#
# collection.insert_one(a)
#
# cursor = collection.find({})
#
# for n in cursor:
#   print(n)
#
# from datetime import datetime
#
# timestamp = 1545730073
# dt_obj = datetime.fromtimestamp(1545730083)
#
# print("date_time:", dt_obj)