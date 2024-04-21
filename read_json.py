import json

filename = '/home/npeppes/experts_dashboard/all_patients.json'#to run it remotely
#"all_patients.json"

def read():
    with open(filename) as json_file:
        data = json.load(json_file)
        return data
        # print(data)
        # print(type(data))
