import requests
#bearer = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZVVEyN183a3Jtck5qcEFfRE5USzRvai1tNmVYZnlzOE9MYjUyUnlsdU9RIn0.eyJleHAiOjE2ODAwMDg1MDksImlhdCI6MTY3OTk4NjkwOSwianRpIjoiMmY0NjBjYzQtNDg1Mi00ZTA0LWEyMDAtMDJkOGQ2ZmU4N2ZkIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FMQU1FREEiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYmQwODE2ZmEtZTY1MS00MjcxLWI0NTItZmJkMDM1NDBmMjcxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiSUFNIiwic2Vzc2lvbl9zdGF0ZSI6IjRkNDIyYTU1LTMyOTEtNDdjNC04NzFiLTI1NDY4ZTA0Y2RlYyIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtYWxhbWVkYSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IklBTSI6eyJyb2xlcyI6WyJzZXJ2aWNlIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiI0ZDQyMmE1NS0zMjkxLTQ3YzQtODcxYi0yNTQ2OGUwNGNkZWMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZ3JvdXAtbmFtZXMiOlsic2VydmljZXMiXSwicm9sZXMiOlsic2VydmljZSJdLCJuYW1lIjoiSUNDUyBTZXJ2aWNlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IiLCJnaXZlbl9uYW1lIjoiSUNDUyIsImZhbWlseV9uYW1lIjoiU2VydmljZSIsImVtYWlsIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IifQ.FAJcESamomnL4AL9u2dGJ7Zu0okMa477xKfglBgvaX9LiyvfyawrdSqMR-NwpZvlbu-sPewQdrUBnkeSG0eEmXJz0R21VbvFMLOzjAnbG-vQ3zy3VwmioHUE_0erpwQR5fjBNybLJYyRfN1Wttk8xWJBxhQhwf-Cg3viONeQQcBkb_wTlT4W0nRkgXiECrB5pOL1hUvraGsB0ZNgkLq4zTTuhX8l40phVkIHiGFNS7yWW8xvcp9f__hDs1ZRxCjfmCgVG2s7wtupy0uas00dIjaL4N63kUgTcAvWAZuNRI-BFZb-QtxqPWuBJRcWm4tlVY6X1QKpT0obRz9W_N94kQ"
# header = 'Bearer ' + bearer

def get_latestPatients(bearer):
    url = 'https://iam-backend.alamedaproject.eu/api/v1/user/latest-patients'
    header = 'Bearer ' + bearer
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    params = {
        'registeredAfter': '2022-01-01T00:00:00',
    }
    response = requests.request("GET", url, headers=headers, data=payload, params=params)
    # print(response.text)
    a = response.json()
    return a

# lp=get_latestPatients(bearer)

#for n in lp:
#    print(n)
