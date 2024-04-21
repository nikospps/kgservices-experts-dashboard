from pymongo import MongoClient
import datetime
from get_meaa import get_meaa

def meaaDB():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['meaadb'] #connect to specific collection(table)
    return collection

# #Use the lines below to write data into the Mongo collection
# collection = meaaDB()
# meaa = get_meaa()
#
# for n in meaa:
#     collection.insert_one(n)
#     print(n)
#
# #Use the lines below to read the data stored into the Mongo collection
# cursor = collection.find({})
# for n in cursor:
#   print(n)
