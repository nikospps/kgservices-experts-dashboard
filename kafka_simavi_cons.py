from kafka import KafkaConsumer
# from pymongo import MongoClient
from json import loads
# import mongoDB
# import jellyfish

# 87.98.133.57:65196
# 10.10.10.5:9094
bootstrap_servers = ['87.98.133.57:65196'] #Instead of 'localhost'
topicName = 'iccs_topic'
consumer = KafkaConsumer(topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,  api_version=(0, 10, 1),
                          auto_offset_reset = 'earliest',value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(message)