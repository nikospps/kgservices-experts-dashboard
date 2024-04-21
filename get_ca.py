import requests

def get_ca(access_token):
    url = "https://semkg.alamedaproject.eu:4567/ca/get"
    header = 'Bearer ' + access_token
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify='/etc/ssl/certs/ca-certificates.crt')
    #verify=False)
    # print(response.text)
    a=response.json()
    return a

# ca=get_ca()
#
# for i in range(len(ca)):
#     print(ca[i])
