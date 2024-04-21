import requests
from jwt_auditrail import token

def auditrailorders():
    url = "https://ensuresec.solutions.iota.org/api/v0.1/channels/logs/00e636f21cdc8349efb252998e4606b64550c568bbf79be78c5b29e334e40f600000000000000000:10925fe5aae3a79cfe62fc8d?api-key=94F5BA49-12B6-4E45-A487-BF91C442276D"
    payload = ""
    headers = {
        'Authorization': token}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    a = response.json()
    return a

def existingorderids():
    existing=auditrailorders()
    results=[]
    for n in range(len(existing)):
        results.append(existing[n]['log']['payload']['orderID'])
    return results

# ne=existingorderids()
# if 3918124929 not in ne:
#     print('fuck')
# else:
#     print('yes, it is')
# for n in w:
#     print(n['log']['type'])
#     print(n['log']['payload'])
#     print('-----------------')

# message = []
# ord = auditrailorders()
# conf = audit_trail_getConfirmOrders.auditrailconforders()
# for m in ord:
#     for n in conf:
#         package = m['log']['payload']['status']
#         confirmed = n['log']['payload']['status']
#         if (package == confirmed):
#             newMessage = {
#                 'log_created': n['log']['created'],
#                 'type': n['log']['type'],
#                 'orderID': n['log']['payload']["orderID"],
#                 'status': n['log']['payload']['status'],
#                 'order_timestamp': n['log']['payload']['timestamp']
#             }
#             message.append(newMessage)
#         else:
#             newMessage = {
#                 'log_created': m['log']['created'],
#                 'type': m['log']['type'],
#                 'orderID': m['log']['payload']["orderID"],
#                 'status': m['log']['payload']['status'],
#                 'order_timestamp': m['log']['payload']['timestamp']
#             }
#             message.append(newMessage)
