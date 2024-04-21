from pymongo import MongoClient
import datetime

# Read MongoDB Function
def read_mongo(collection):
    for num in collection.find({}):
        print(num)

# Read and Return a list of MongoDB Function
def return_mongo(collection):
    l = []
    for num in collection.find():
        l.append(num)
    return l

# Read MongoDB for specific keys of the REST API

# Write a specific dodument to MongoDB using Write Function
def write_mongo(collection,jsondata):
    collection.insert_one(jsondata)

# Write many doduments to MongoDB using Write Function: as bulkdata, a list of dictionaries will be used for bulk insert
def write_mongo(collection,bulkdata):
    collection.insert_many(bulkdata)

# Delete all documents from a specific collection
def delete_all(collection):
    collection.delete_many({})

# Collection Init - We already defined the credentials of the current Database
def coll():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client.list_database_names()
    db = client['testdb']
    db.list_collection_names()
    collection = db['Monitor'] #connect to specific collection(table)
    return collection

def coll1():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client.list_database_names()
    db = client['testdb']
    db.list_collection_names()
    collection = db['Monitor1'] #connect to specific collection(table)
    return collection

# # Create a new collection into the selected database for the communication monitor
# db.create_collection('Monitor1')
########################################################################################################################
# client = MongoClient('147.102.40.53',19870)
# client = MongoClient('147.102.40.53',27017)
# client = MongoClient('mongodb://147.102.40.53:19870/testdb?ssl=true&ssl_cert_reqs=CERT_NONE') # Accessing the specific database(collection)
# client = MongoClient('mongodb://admin:Pa$$w0rd!@147.102.40.53:19870') # Accessing authorized mongodb for a specific user
# client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
#
# db = client.list_database_names()
#
# print(db)
#
# #db1 = client.get_database('testdb')
#
# # Select the desired Database from the existing
# db = client['testdb']
# #db = client['admin']
#
# # Create a new collection into the selected database for the communication monitor
# # comMon = db['monitor']
# db.create_collection('Monitor')
#
# #db.authenticate('admin','Pa$$w0rd!') # only if authentication is used
#
# # Check for existing collections into the selected db
# db.list_collection_names()
#
# # Connect to specific collection(table)
# collection = db['Monitor']
# print(collection)
# #
# # col1 = collection.find()[11]['carPlate']
# # print(collection.find()[10]['carPlate'])#return car plate for first element = PPS-8001
# # print(collection.find()[0]['carplate'])#just by reading the first element of the newly created mongo for mantis project (14/4/2020)
#
# example = {"type":"alert"}
#
# # Insert data
# rec_id1 = collection.insert_one(example)
#
# ########Its the read_mongo function
# cursor = collection.find({})
#
# def tes():
#     for document in cursor:
#         if document['carplate'] != 'NO-PLATE':
#           return(document)
#         else:
#             print('empty')
#
# for n in cursor:
#     print(n)
#
# # tes()
#
# t = collection.find({"carPlate": "ZXX-9811", "timeStamp": "03072020_125254"})
#
# for i in t:
#     if "03072020" in t['timeStamp']:
#         print(i)
#
# import pandas as pd
# import time
# df = pd.DataFrame(list(t))
# df['id']
#
# def export_data():
#     name = get_data()
#     df2 = pd.DataFrame.from_records(name)
#     t = time.localtime()
#     timestamp = time.strftime('%b-%d-%Y_%H%M', t)
#     # BACKUP_NAME = ("Rest_" + timestamp)#SOS
#     # df2.to_csv(BACKUP_NAME+'.csv')#SOS
#     mantis_backup = ("MantisBackUp_" + timestamp)
#     df2.to_csv(mantis_backup + '.csv')
#
#
# myquery = { "id": 1 }
#
# res = collection.find(myquery)
#
# # len(cursor)
#
# test = read_mongo()
#
# collection.find()[0]['carPlate']
#
# # Create query(-ies) in order to insert one and many data elements into the collection
# post_query = {"name":"nikos",
#         "age":32,
#         "Job":"ICCS"}
#
# post_query = {"name":"teo",
#         "age":30,
#         "Job":"ICCS"}
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
#
# # Delete a specific document from a mongo db using a Specific query
# myQuery = {'passenger_ID': '1358'}
# myQuery = {'author': 'Mike'}
# myQuery = {'pendingTrouble': 'False-Trying'}
#
# collection.delete_one(myQuery)
#
# # Delete all documents from a specific collection
# collection.delete_many({})
#
# # Execute functions
# read_mongo()
# ########################################################################################################################
# import json
# from collections import OrderedDict
#
# id = '203'
#
# with open('data,json') as data_file:
#     data = json.load(data_file, object_pairs_hook=OrderedDict)
#     for key, value in data.items():
#         print(key)
#         id_value = value['payload']['price']
#         if id in id_value: # check first if id is present
#             pack = id_value[id]
#             print(pack) #pack should be returning the value of the key '203'
# ########################################################################################################################
# ########################################################################################################################
# ###########################################Find the Total Shift of the Driver###########################################
# from datetime import datetime
#
# date = {
#   "car_template": "ZXX9811",
#   "date": "1/10/2019",
#   "klm_start": 182767,
#   "kml_stop": 183007,
#   "passenger_ID": 1358,
#   "shift_name": "A",
#   "time_from":"14.00",
#   "time_to":"22.00"
# }
#
# a = date['time_from']
# b = date['time_to']
# time1 = datetime.strptime(a,"%H.%M") # convert string to time
# time2 = datetime.strptime(b,"%H.%M")
# diff = time2 -time1
# total_time = diff.total_seconds()/3600    # seconds to hour
#
# # type(diff.total_seconds()/3600)
#
#
# date = {
#     "carplate": "ZXX9811",
#     "date": "2/10/2019",
#     "km_start": 182777,
#     "km_stop": 183511,
#     "passenger_ID": "2458",
#     "shift_name": "\u03a0",
#     "time_from": "06:00",
#     "time_to": "14:00"
#   }
# #
# # import regex as re
# # greek=date['shift_name']
# unicodedata.decomposition(precomposed)