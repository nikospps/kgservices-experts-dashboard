from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import mongoDB
import jellyfish

bootstrap_servers = ['localhost:9092']
topicName = 'signature'
consumer = KafkaConsumer (topicName, group_id = 'group1',bootstrap_servers = bootstrap_servers,
                          auto_offset_reset = 'latest',value_deserializer=lambda x: loads(x.decode('utf-8')))


# monitor1 = mongoDB.coll1()
# mongoDB.read_mongo(monitor)

# consumer = KafkaConsumer(
#     'test',
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      group_id='group1',
#      value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
#db1 = client.get_database('testdb')
db = client['testdb']
# collection = db['commmon']
#db.authenticate('admin','Pa$$w0rd!') # only if authentication is used
db.list_collection_names()
collection = db['Monitor1'] #connect to specific collection(table)


for message in consumer:
    collection.insert_one(message.value)
        # print(message.value)

    # sen1 = '068/09_068.png'
    # # y = message.value.decode()
    # message = message.value
    # if (jellyfish.jaro_similarity(sen1, message['id']) != 1.0):
    #     monitor1.insert_one(message)
    #     print('Alerting! Possible Tampering on the Driver Signature')
    #     # print(y)
    # else:
    #     print('Information Flow is ok')
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