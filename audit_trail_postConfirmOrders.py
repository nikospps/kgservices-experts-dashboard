import requests
import json
from datetime import datetime
from jwt_auditrail import token

def auditrailconf(alert):
  url = "https://ensuresec.solutions.iota.org/api/v0.1/channels/logs/53236e504df2858916b970a2094da4666aed94c19d9cf501e0bb58b1d0ee6a700000000000000000:ed84c32793de12f49eb2ec8b?api-key=94F5BA49-12B6-4E45-A487-BF91C442276D"
  payload = json.dumps({"type": "Communication Monitor Ordering System","payload": alert})
  headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  # print(response.text)
  return response.text

# order = [{"orderID": 3918124922,"status": "delivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]
# #,
# #          {"orderID": 3918124921,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")},
# #          {"orderID": 3918124922,"status": "undelivered","order_timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")}]
# for alert in order:
#   auditrailconf(alert)
#   print('Order Already Stored')
# print('Storing Processes Already Finished')