from pymongo import MongoClient
import datetime

# Read MongoDB Function
def read_mongo():
    for num in collection.find():
        print(num)

# Read MongoDB for specific keys of the REST API

# Write a specific dodument to MongoDB using Write Function
def write_mongo(jsondata):
    collection.insert_one(jsondata)

# Write many doduments to MongoDB using Write Function: as bulkdata, a list of dictionaries will be used for bulk insert
def write_mongo(bulkdata):
    collection.insert_many(bulkdata)

client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
# db = client.list_database_names()
# print(db)
db = client['testdb']
# db.list_collection_names()
collection = db['Monitor1'] #connect to specific collection(table)
collection = db['commmon']
########Its the read_mongo function
cursor = collection.find({})

for n in cursor:
    print(n)
#
# cxb = []
# for document in cursor:
#     cxb.append(document)
#     # print(document)
# #
# # Delete all documents from a specific collection
collection.delete_many({})
#
# post_query = {
#     "SpeedObd": 0,
#     "accuracy": 51.029,
#     "altitude": 63,
#     "bearing": 0,
#     "engineRunTime": 0,
#     "engineTemp": 32,
#     "fuelLevel": 0,
#     "fuelType": 0,
#     "intakeTemp": 0,
#     "lat": 38.1861,
#     "lon": 21.7,
#     "pendingTrouble": "False",
#     "relThrottle": 0,
#     "rpm": 3293,
#     "speedGps": 0,
#     "timeStamp": "29102019_153725",
#     "vinNumber": 2,
#     "carPlate": "IHZ-3302"
#   }
#
# collection.insert_one(post_query)

# Delete a specific document from a mongo db using a Specific query
# myQuery = {'passenger_ID': '1358'}
# myQuery = {'author': 'Mike'}
# myQuery = {'pendingTrouble': 'False-Trying'}
#
# collection.delete_one(post_query_event)


