import requests
import json
from datetime import datetime
from jwt_auditrail import token

def auditrail(alert):
  url = "https://ensuresec.solutions.iota.org/api/v0.1/channels/logs/00e636f21cdc8349efb252998e4606b64550c568bbf79be78c5b29e334e40f600000000000000000:10925fe5aae3a79cfe62fc8d?api-key=94F5BA49-12B6-4E45-A487-BF91C442276D"
  payload = json.dumps({"type": "Communication Monitor Ordering System","payload": alert})
  headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  # print(response.text)
  return response.text

# order = [{"orderID": 3918124922,"status": "delivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]#Initial record stored for testing purposes
#order = [{"orderID": 3918124930,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")},
#         {"orderID": 3918124931,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")},
#         {"orderID": 3918124932,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]
#for n in order:
#  auditrail(n)
#  print('Order Already Stored')
#print('Storing Processes Already Finished')

# order = [{"orderID": 3918124922,"status": "delivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]
# #,
# #          {"orderID": 3918124921,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")},
# #          {"orderID": 3918124922,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]
# for alert in order:
#   auditrail(alert)
#   print('Order Already Stored')
# print('Storing Processes Already Finished')
