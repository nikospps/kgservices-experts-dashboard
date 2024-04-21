from time import sleep
from json import dumps
from kafka import KafkaProducer
from faker import Faker

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

n = [{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-Friendly'},
     {'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Pollutive'},{'Driver Behavior': 'Eco-Friendly'},
     {'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Pollutive'},{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-FriendlySkatoulesThodwroula'}]

n = [{'Driver Behavior': 'Twra arxizoyn ta dyskola?'}]
# # Tamper 3 of 10 sent messages from the sensors
# l[0]['id'] = 'GB27OYNPPS75904402691561'
# l[3]['id'] = 'GB27OYXPP75904402691562'
# l[9]['id'] = 'GB27OYNTP75904402691563'

producer = KafkaProducer(bootstrap_servers=['147.102.40.97:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# for n in range(1000):
#     producer.send('sensorid1', value=n)
#     print(n)

# Use it for a topic called sensorid
for e in range(len(n)):
    # data = {'number' : e, 'type':'alert'}
    producer.send('sensoridtest', value=n[e])
    print(n[e])
    # sleep(5)

# For REST API just for Asynchronous Purposes
# for i in range(len(lam)):
#     print(lam[i]['id'])