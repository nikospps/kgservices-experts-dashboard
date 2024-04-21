import json
import pandas as pd
import io
import codecs

# Opening JSON file
f = open('CXB_data_sample.json', )

with open('CXB_test.json') as json_file:
    data = json.load(json_file)

json_data = {
            "scoring": {
                    "benign_scoring": 306,
                    "malicious_scoring": 180
                    },
            "pending_3ds": False,
            "user_found": True,
            "merchant_check": {
                    "known": False,
                    "new": True,
                    "usual": False,
                    "blank": False
                },
            "merchant_type_check": {
                    "known": False,
                    "new": True,
                    "usual": False,
                    "blank": False
                },
            "merchant_country_check": {
                    "known": False,
                    "new": True,
                    "usual": False,
                    "blank": False,
                    "transaction_periods": {
                            "timezone_22_1": 0,
                            "timezone_2_5": 0,
                            "timezone_6_9": 0,
                            "timezone_10_13": 2,
                            "timezone_14_15": 0,
                            "timezone_16_19": 0,
                            "timezone_20_21": 0
                        }
                    },
            "geo_ip": {
                    "ip": "",
                    "city": "Pamplona",
                    "country": "Spain",
                    "iso": "ES",
                    "time_zone": "Europe/Madrid",
                    "continent": "Europe",
                    "latitude": "42.8182",
                    "longitude": "-1.636",
                    "accuracy_radius": 50,
                    "asn": 197829,
                    "asn_organisation": "",
                    "connection_type": "Corporate",
                    "postal_code": 31080,
                    "is_anonymous_proxy": False,
                    "is_satellite_provider": False
                    },
            "customerid": {
                    "nif": "National ID (text)",
                    "sau": 9725019678271,
                    "nummid": 367011759,
                    "usuclo": 967827100,
                    "e":"",
                    "carpeta": 73929906
                    },
            "merchanInfo": {
                    "merchantType": 5942,
                    "merchantCountryCode": 724,
                    "merchantName": "",
                    "merchantRiskIndicator": 0,
                    },
            "browserInfo": {
                    "browserLanguage": "es-ES",
                    "browserIp": "",
                    "browserUseragent": ""
                    },
            "traRiskIndicator": 0,
            "purchaseInfo": {
                    "purchaseAmount": 32.71,
                    "purchaseCurrency": 978,
                    "cumulativeAmount": 0
                    },
            "operation": {
                    "pan": "404700******1090",
                    "cardHolderName": "",
                    "cardHolderEmails": "",
                    "homePhone": "",
                    "mobilePhone": "",
                    "billAddress": "",
                    "billAddrCity": "",
                    "billAddrPostcode": "",
                    "billAddrCountry": "",
                    "shipAddress": "",
                    "shipAddrCity": "",
                    "shipAddrPostCode": "",
                    "shipAddrCountry": ""
                    },
            "panInfo": {
                    "id": "147021-404700-1",
                    "contrato": 147021,
                    "plastico": 1,
                    "enterprise": "CXB",
                    "cardType": "P",
                    "createDate": 2019052,
                    "limitCard": 9870,
                    "affinity": "GN",
                    "bin": 404700
                    },
            "aliases": {
                    "address": "",
                    "city": 31,
                    "postcode": 15126,
                    "country": "",
                    "numMobile": "",
                    "email": "",
                    "auth": ""
                    }
}

data = json.dumps(json_data)
print(data)

# Read a JSON file
with open('G4S_data_sample.json') as json_file:
    data = json.load(json_file)
    print(data['G4S_message1'][0]["Driver's personal device"])

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
    if data[i]['aliases']['numMobile'] == '6900000003':
        print(data[i]['aliases']['email'])
    # print(data['CXB_data_sample'][0]['scoring'][0]['benign_scoring'])

data = data['CXB_data_sample']

type(data)

for n in range(len(data)):
    print(data[n])

df = pd.DataFrame.from_dict(data)

# Closing file
f.close()

