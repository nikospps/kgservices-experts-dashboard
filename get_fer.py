import requests

def get_fer(access_token):
    url = "https://semkg.alamedaproject.eu:4567/fer/get"
    header = 'Bearer ' + access_token
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify='/etc/ssl/certs/ca-certificates.crt')
    # print(response.text)
    a=response.json()
    return a

# # Connect and retrieve data from KG API in order to update the existing one in Alameda Cloud
#fer=get_fer()
# # Connect to specific collection of the Alameda Cloud
# collection=mongo_meaa.meaa()
# # #
# b= collection.find()#find all the documents on the existing collection
# len(list(b))#count the number of the existing instances in the cursor of the current Mongo collection
# # #Update the already existing data instances
# for n in b:
#     print(n['observationID'])

#for n in fer:
#    print(n['results'][0]['score'])
