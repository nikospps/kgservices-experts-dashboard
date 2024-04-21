from pymongo import MongoClient
import datetime

def g4s():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['commmon'] #connect to specific collection(table)
    return collection

#collection = g4s()
#cursor = collection.find({})

#for n in cursor:
#    print(n)
