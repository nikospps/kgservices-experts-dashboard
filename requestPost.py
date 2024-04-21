import requests, json

url = 'http://localhost:5545/name'

data = {
    'infer': 'Person-23 hasOwnershipOf BMW X6'
  }


requests.put(url,data)

requests.put(url, data=json.dumps(data))

task = requests.put(url,data)
task = requests.post(url, data=json.dumps(data))
# json.dumps(create_row_data),
#

