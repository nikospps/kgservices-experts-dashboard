from time import sleep
from json import dumps
from kafka import KafkaProducer
from faker import Faker
import json

fake = Faker()
l = []

with open('./CXB_test.json') as json_file:
    cxb = json.load(json_file)

#
# message = {
#             "scoring": {
#                     "benign_scoring": 306,
#                     "malicious_scoring": 180
#                     },
#             "pending_3ds": False,
#             "user_found": True,
#             "merchant_check": {
#                     "known": False,
#                     "new": True,
#                     "usual": False,
#                     "blank": False
#                 },
#             "merchant_type_check": {
#                     "known": False,
#                     "new": True,
#                     "usual": False,
#                     "blank": False
#                 },
#             "merchant_country_check": {
#                     "known": False,
#                     "new": True,
#                     "usual": False,
#                     "blank": False,
#                     "transaction_periods": {
#                             "timezone_22_1": 0,
#                             "timezone_2_5": 0,
#                             "timezone_6_9": 0,
#                             "timezone_10_13": 2,
#                             "timezone_14_15": 0,
#                             "timezone_16_19": 0,
#                             "timezone_20_21": 0
#                         }
#                     },
#             "geo_ip": {
#                     "ip": "",
#                     "city": "Pamplona",
#                     "country": "Spain",
#                     "iso": "ES",
#                     "time_zone": "Europe/Madrid",
#                     "continent": "Europe",
#                     "latitude": "42.8182",
#                     "longitude": "-1.636",
#                     "accuracy_radius": 50,
#                     "asn": 197829,
#                     "asn_organisation": "",
#                     "connection_type": "Corporate",
#                     "postal_code": 31080,
#                     "is_anonymous_proxy": False,
#                     "is_satellite_provider": False
#                     },
#             "customerid": {
#                     "nif": "National ID (text)",
#                     "sau": 9725019678271,
#                     "nummid": 367011759,
#                     "usuclo": 967827100,
#                     "e":"",
#                     "carpeta": 73929906
#                     },
#             "merchanInfo": {
#                     "merchantType": 5942,
#                     "merchantCountryCode": 724,
#                     "merchantName": "",
#                     "merchantRiskIndicator": 0,
#                     },
#             "browserInfo": {
#                     "browserLanguage": "es-ES",
#                     "browserIp": "",
#                     "browserUseragent": ""
#                     },
#             "traRiskIndicator": 0,
#             "purchaseInfo": {
#                     "purchaseAmount": 32.71,
#                     "purchaseCurrency": 978,
#                     "cumulativeAmount": 0
#                     },
#             "operation": {
#                     "pan": "404700******1090",
#                     "cardHolderName": "",
#                     "cardHolderEmails": "",
#                     "homePhone": "",
#                     "mobilePhone": "",
#                     "billAddress": "",
#                     "billAddrCity": "",
#                     "billAddrPostcode": "",
#                     "billAddrCountry": "",
#                     "shipAddress": "",
#                     "shipAddrCity": "",
#                     "shipAddrPostCode": "",
#                     "shipAddrCountry": ""
#                     },
#             "panInfo": {
#                     "id": "147021-404700-1",
#                     "contrato": 147021,
#                     "plastico": 1,
#                     "enterprise": "CXB",
#                     "cardType": "P",
#                     "createDate": 2019052,
#                     "limitCard": 9870,
#                     "affinity": "GN",
#                     "bin": 404700
#                     },
#             "aliases": {
#                     "address": "",
#                     "city": 31,
#                     "postcode": 15126,
#                     "country": "",
#                     "numMobile": "",
#                     "email": "",
#                     "auth": ""
#                     }
# }

# l.append(message)

# # Tamper 3 of 10 sent messages from the sensors
# l[0]['id'] = '068/09_0681.png'
# l[3]['id'] = '068/07_068.png'
# l[9]['id'] = '068/09fds_068.png'

producer = KafkaProducer(bootstrap_servers=['147.102.40.97:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(len(cxb)):
    # data = {'number' : e, 'type':'alert'}
    producer.send('signature', value=cxb[e])
    print(cxb[e])
    # sleep(5)

# For REST API just for Asynchronous Purposes
# for i in range(len(lam)):
#     print(lam[i]['id'])