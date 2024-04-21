import requests

#b = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZVVEyN183a3Jtck5qcEFfRE5USzRvai1tNmVYZnlzOE9MYjUyUnlsdU9RIn0.eyJleHAiOjE2NzgzNzA1MTEsImlhdCI6MTY3ODM0ODkxMSwianRpIjoiNzQzYTJkNGMtMGM3NS00NGI1LWJjMTctMDBiN2Y4OGE0Y2IyIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FMQU1FREEiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYmQwODE2ZmEtZTY1MS00MjcxLWI0NTItZmJkMDM1NDBmMjcxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiSUFNIiwic2Vzc2lvbl9zdGF0ZSI6IjAzYjk2OTg1LTY2ZDAtNGJiYi05OTc3LTVlOTlhMTA1Njc0YiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtYWxhbWVkYSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IklBTSI6eyJyb2xlcyI6WyJzZXJ2aWNlIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiIwM2I5Njk4NS02NmQwLTRiYmItOTk3Ny01ZTk5YTEwNTY3NGIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZ3JvdXAtbmFtZXMiOlsic2VydmljZXMiXSwicm9sZXMiOlsic2VydmljZSJdLCJuYW1lIjoiSUNDUyBTZXJ2aWNlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IiLCJnaXZlbl9uYW1lIjoiSUNDUyIsImZhbWlseV9uYW1lIjoiU2VydmljZSIsImVtYWlsIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IifQ.PstyWXF2AjdAAdRDGxnGZzlQV-v3zgKUI0S8Oge4qDjWMuJVaFZm_0DhuwktX1pbBWDR8fEszuXwz-XLkledSsLqhmJ6vsi0AW4fWTjtE3v4f5VTxKDXANb9zKSeOJoJOXMkOzxA6odIwXeMbGE8InqF5ucUIOUxn_7uKe1j2hA0I90InLMsxnnrmsykspE2quYPTIjID9mT5ca9J0uJ7IwQWYniTYEY5d5HLXq6XuyyzmBmUhlHHN6_zvtszNrT17NWdcHQyMS8KAdAzzPwLG9kaH7_rRtWCkaPxqacu81ydcOgkCRij3TPMsk9BQiux6mspJvJAYxUvb_g-VfVJQ"

def get_fbdaily(access_token):
    url = "https://my.alameda.wellics.cloud/physical-activity-service/daily_summary"
    header = 'Bearer ' + access_token
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    response = requests.request("GET", url, headers=headers)#, data=payload)#, verify='/etc/ssl/certs/ca-certificates.crt')
    #verify=False)
    # print(response.text)
    a=response.json()
    return a

#ca=get_fbdaily(b)
#
# for i in range(len(ca)):
#     print(ca[i])
