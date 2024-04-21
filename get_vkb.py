import requests

#at = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZVVEyN183a3Jtck5qcEFfRE5USzRvai1tNmVYZnlzOE9MYjUyUnlsdU9RIn0.eyJleHAiOjE3MDYwMjgwNzgsImlhdCI6MTcwNjAwNjQ3OCwianRpIjoiNTIxM2JhYjUtOWY2Yy00MjRhLTk4ZGItZWNjYWFhMWRjZjY5IiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FMQU1FREEiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYmQwODE2ZmEtZTY1MS00MjcxLWI0NTItZmJkMDM1NDBmMjcxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiSUFNIiwic2Vzc2lvbl9zdGF0ZSI6ImUwOGI0ZWMwLThmYzYtNDFiZi05NDQzLTIzYjgzM2NiNzRkYiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtYWxhbWVkYSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IklBTSI6eyJyb2xlcyI6WyJzZXJ2aWNlIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJlMDhiNGVjMC04ZmM2LTQxYmYtOTQ0My0yM2I4MzNjYjc0ZGIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZ3JvdXAtbmFtZXMiOlsic2VydmljZXMiXSwicm9sZXMiOlsic2VydmljZSJdLCJuYW1lIjoiSUNDUyBTZXJ2aWNlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IiLCJnaXZlbl9uYW1lIjoiSUNDUyIsImZhbWlseV9uYW1lIjoiU2VydmljZSIsImVtYWlsIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IifQ.hCuTSEj2pebuZ-19YS6vfOlN-JYTUESrsF2KeG0gtX5ZDEW9Q-fuMNWCuXC2XqWvepedA_FZkThnsncAqJVr-82imXALZGe3EIT39NGl0WSE_YylDXnrkM4JbLAxfjER9_kc_n_PfP0dLxLBlGjXYheUu9Fuh6Ji_wpOeY8OSA_4EoVqTWROeJPMAl0hk69T1rEAmjcp_Kuy1vwm32locZO_jcwteJkq8e-_UHrkgiu-EjNcr2nPK7eFJx6J_gr_7KnMsvOtWs7YFGo4yTND4HS40EZhEA4gNSaWUAyjl3CseJcE8XHgmM3snAl_k2a7QF1UIW-aEtBUd7ZjQEgKSw"

def get_vkb(access_token):
    url = "https://semkg.alamedaproject.eu:4567/vkb/get"
    header = 'Bearer ' + access_token
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    response = requests.request("GET", url, headers=headers, data=payload,verify='/etc/ssl/certs/ca-certificates.crt')
    # print(response.text)
    a=response.json()
    return a

# # Connect and retrieve data from KG API in order to update the existing one in Alameda Cloud
# vs = get_vs()
# # Connect to specific collection of the Alameda Cloud
# collection=mongo_meaa.meaa()
# # #
# b= collection.find()#find all the documents on the existing collection
# len(list(b))#count the number of the existing instances in the cursor of the current Mongo collection
# # #Update the already existing data instances
# for n in b:
#     print(n['observationID'])
