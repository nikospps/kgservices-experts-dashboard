import requests

url = "https://ensuresec.solutions.iota.org/api/v0.1/channels/logs/9f9deaac2fba505a7cd96c73c318296656b53f8d24d576a479d3426e815bac710000000000000000:179289a6a8f4005c0cfecb7d?api-key=94F5BA49-12B6-4E45-A487-BF91C442276D"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiZGlkOmlvdGE6MnBoam9hWXVZZkhtZ2lXWHdKOUtmb0F2cW15TXN6Q3BLOXJtYXJraUZvbWsiLCJwdWJsaWNLZXkiOiI1ZXpZNHhGcFZ6YTlXcGl2OHJZVkJCMnNrcmdnTmsxVEpVblhVb0c0U2EyeSIsInVzZXJuYW1lIjoiaWNjcyIsInJlZ2lzdHJhdGlvbkRhdGUiOiIyMDIyLTAyLTAyVDExOjQwOjU4WiIsImNsYWltIjp7InR5cGUiOiJQZXJzb24iLCJuYW1lIjoiTmlrb3MgUGVwcGVzIiwiZmFtaWx5TmFtZSI6IlBlcHBlcyIsImdpdmVuTmFtZSI6Ik5pa29zIiwiYmlydGhEYXRlIjoiMTk4Ny0wMi0yMiJ9LCJyb2xlIjoiVXNlciJ9LCJpYXQiOjE2NDM5MDA5NTQsImV4cCI6MTY0NDUwNTc1NH0.nt5jw2eOaLinuR3KAPWbth4f9IYF5Ou_alTqO5dQtd4'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

a=response.json()

for n in a:
    print(n['log']['type'])
    print(n['log']['payload'])
    print('-----------------')