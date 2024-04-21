from json import dumps
from kafka import KafkaProducer
# import sleep

n = [{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-Friendly'},
     {'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Pollutive'},{'Driver Behavior': 'Eco-Friendly'},
     {'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Pollutive'},{'Driver Behavior': 'Eco-Friendly'},{'Driver Behavior': 'Eco-FriendlySkatoules'}]

# 87.98.133.57:65196
# 10.10.10.5:9094
producer = KafkaProducer(bootstrap_servers=['87.98.133.57:65196'],api_version=(0, 10, 1),
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

# topic called sensorid
for e in range(len(n)):
    # data = {'number' : e, 'type':'alert'}
    producer.send('iccs_topic', value=n[e])
    print(n[e])
    # sleep(5)
