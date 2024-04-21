from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import mongoDB
import jellyfish

bootstrap_servers = ['147.102.40.97:9092']
topicName = 'signature'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'earliest',value_deserializer=lambda x: loads(x.decode('utf-8')))
client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017')  # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
db = client['testdb']
# db.list_collection_names()
collection = db['Monitor1']  # connect to specific collection(table)

for message in consumer:
    collection.insert_one(message.value)
