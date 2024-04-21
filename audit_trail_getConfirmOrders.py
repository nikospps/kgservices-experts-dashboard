import requests
from jwt_auditrail import token

def auditrailconforders():
    url = "https://ensuresec.solutions.iota.org/api/v0.1/channels/logs/53236e504df2858916b970a2094da4666aed94c19d9cf501e0bb58b1d0ee6a700000000000000000:ed84c32793de12f49eb2ec8b?api-key=94F5BA49-12B6-4E45-A487-BF91C442276D"
    payload = ""
    headers = {
        'Authorization': token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    a = response.json()
    return a

def existingconforderids():
    existing=auditrailconforders()
    results=[]
    for n in range(len(existing)):
        results.append(existing[n]['log']['payload']['orderID'])
    return results

# b=auditrailconforders()
# t1=[]
# t2=[]
# for n in w:
#     if((n['log']['payload']['orderID']) and (n['log']['payload']['status']=='undelivered')):
#         print(str(n['log']['payload']['orderID'])+' is '+n['log']['payload']['status'])
#     else:
#         print('Was finally delivered')

