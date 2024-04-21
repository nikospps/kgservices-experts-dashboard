import json
import pandas as pd
import io
import codecs

# Opening JSON file
f = open('ecommerce.json', )

with open('ecommerce.json') as json_file:
    data = json.load(json_file)

json_data = [
    {
        "flag": "message1",
        "type": "driver",
        "driverID": "mdtanp26046909ta",
        "drivername": "theo",
        "driversurname": "alex",
        "dateTimeUTC": "2021-10-15T18:18:58"
    },
    {
        "flag": "message1",
        "type": "driver",
        "driverID": "mdtanp26046909ta",
        "drivername": "theo",
        "driversurname": "alex",
        "dateTimeUTC": "2021-10-15T18:18:58"
    },
    {
        "flag": "message1",
        "type": "driver",
        "driverID": "mdtanp02026919np",
        "drivername": "manos",
        "driversurname": "daskalis",
        "dateTimeUTC": "2021-10-16T16:17:53"
    },
    {
        "flag": "message1",
        "type": "driver",
        "driverID": "mdtanp29106909ta",
        "drivername": "george",
        "driversurname": "kout",
        "dateTimeUTC": "2021-10-21T15:18:58"
    }
]

data = json.dumps(json_data)
print(data)

# Read a JSON file
with open('G4S_data_sample.json') as json_file:
    data = json.load(json_file)
    print(data['G4S_message1'][0]["Driver's personal device"])

for n in range(len(data)):
    print(data[n]["Driver's personal device"])

# Write JSON file
with codecs.open('data.json', 'w', 'utf8') as f:
    f.write(json.dumps(json_data, sort_keys=False, ensure_ascii=False))#in order NOT to sort the keys alphabetically

# returns JSON object as
# a dictionary
data = json.load(f)
len(data)
# Iterating through the json
# list
for i in range(len(data)):
    if (data[i]['flag'] == 'message2'):
        print(data[i])

data = data['CXB_data_sample']

type(data)

for n in data:
    if(data['flag']=='message2'):
        print(n)

df = pd.DataFrame.from_dict(data)

# Closing file
f.close()

