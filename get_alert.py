import requests
#bearer = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZVVEyN183a3Jtck5qcEFfRE5USzRvai1tNmVYZnlzOE9MYjUyUnlsdU9RIn0.eyJleHAiOjE2ODE5MDkzMTAsImlhdCI6MTY4MTg4NzcxMCwianRpIjoiMzhhMTZkMjAtMDk5NC00YzM4LTkyOGEtOGQyMjUxZmI0ZjJkIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FMQU1FREEiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYmQwODE2ZmEtZTY1MS00MjcxLWI0NTItZmJkMDM1NDBmMjcxIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiSUFNIiwic2Vzc2lvbl9zdGF0ZSI6ImEzMjBkM2QxLTQ1MzYtNGIwOC1iYTg5LTk5NmJmODNkZjQxMyIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiIsImRlZmF1bHQtcm9sZXMtYWxhbWVkYSJdfSwicmVzb3VyY2VfYWNjZXNzIjp7IklBTSI6eyJyb2xlcyI6WyJzZXJ2aWNlIl19LCJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiJhMzIwZDNkMS00NTM2LTRiMDgtYmE4OS05OTZiZjgzZGY0MTMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZ3JvdXAtbmFtZXMiOlsic2VydmljZXMiXSwicm9sZXMiOlsic2VydmljZSJdLCJuYW1lIjoiSUNDUyBTZXJ2aWNlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IiLCJnaXZlbl9uYW1lIjoiSUNDUyIsImZhbWlseV9uYW1lIjoiU2VydmljZSIsImVtYWlsIjoiaWNjcy1zZXJ2aWNlQGNuLm50dWEuZ3IifQ.ALBsFz45u-ULA8s-ylCoWut5GfsA9lRP8HgO_v1wS1wLFKXREYqXOLvYaZtU6nPeAWPgzDEuoRorAmzlbsfzaWGTcLoxPDkij2MWEmG34RuU6-Pwnr0haRtxQN1FxNMfkGe1PhW-gWMJZuR5fhNSmNF5XoLeANBgzj4rRG38--zXz2frHhqRj1yDdLwjYHn38YzeAkCFVdscUpuW0JfBkJR4Gblqrbrgu7YZ22XB759Eie4h8iVKXr8t0fFGExdzVUyHFmVVpmAZWz28JO98E9UmfflCTvyvNO-4NWzQol4hIUdEqwLCNwbW1w9bxamvaurKF8x9sV941hGq8T0hpg'
# header = 'Bearer ' + bearer
def get_alert(bearer):
    url = "https://semkg.alamedaproject.eu:4567/wm/alert"
    header = 'Bearer ' + bearer
    payload={}
    # headers = {}
    headers = {
        'accept': 'application/json',
        'Authorization': header,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    a=response.json()
    return a

#alert=get_alert(bearer)
#
#for n in alert:
#    print(n)
# import json
#
# with open("all_patients.json") as json_file :
#   patients = json.load(json_file)
#
# for pat in patients:
#     for caa in ca:
#         if (pat['id']!=caa['userID']):
#             pass
#         else:
#             print('Patient detected')
#             print(caa['userID'])
#             print(pat['email'])
#             # print('patiendID did not detected')

#
# from IAM import cross_correlation
# for n in ca:
#         if ('userID' not in n):
#             continue
#         else:
#             a,c = cross_correlation(bearer,n['userID'])
#             print(n['userID'])
#             if (a==200):
#                 print(c['email'])
#             else:
#                 continue
# import datetime
# a='1990-03-21T07:33:25.025Z'.split('.')[0]
# datetime.datetime.strptime(a,"%Y-%m-%d"'T''%H:%M:%S')
