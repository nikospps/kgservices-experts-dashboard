from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import mongoDB
import jellyfish

bootstrap_servers = ['147.102.40.97:9092'] #Instead of 'localhost'
topicName = 'sensorid'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'earliest',enable_auto_commit = True,max_poll_interval_ms=5000,
                          max_poll_records=1,value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(message)
# monitor = mongoDB.coll()
# mongoDB.read_mongo(monitor)

# consumer = KafkaConsumer(
#     'test',
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      group_id='group1',
#      value_deserializer=lambda x: loads(x.decode('utf-8')))

# for message in consumer:
#     sen1 = 'GB27OYHS75904402691560'
#     # y = message.value.decode()
#     message = message.value
#     if (jellyfish.jaro_similarity(sen1, message['id']) != 1.0):
#         monitor.insert_one(message)
#         print('Alerting! Possible Tampering on the SensorID')
#         # print(y)
#     else:
#         print('Information Flow is ok')

# for message in consumer:
#     print(message)
    # monitor.insert_one(message)
    # print('Number {} added!'.format(message))#['number'], message['type']))#, collection))


# from faker import Faker
#
# fake = Faker()
# l = []
#
# for i in range(10):
#     message = {
#         'id': 'GB27OYHS75904402691560',
#         'source' : fake.ipv4_private(),
#         'detail' : fake.hostname()
#     }
#     l.append(message)