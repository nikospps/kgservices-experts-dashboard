import requests

def get_wcs(access_token):
    url = "https://semkg.alamedaproject.eu:4567/wm/get"
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

#wcs=get_wcs()
#
# for i in range(len(ca)):
#     print(ca[i])
