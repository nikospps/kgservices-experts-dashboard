import json
import jellyfish
# driversid_list = ['XFGRJYHN1235MM','XFGRJYHN5678MM','XFGRZSEN9012MM','XFGRZSEN5247MM']#we can retrieve it manually
#
# with open('G4S_test.json') as json_file:
#     data = json.load(json_file)

def tampering(data,driversid_list):
    comparison_results = []
    nontampered_sensors = []
    tampered_sensors = []
    tamperflag = True
    for n in range(len(data)):
        for m in range(len(driversid_list)):
            # print(jellyfish.jaro_similarity(data[n]["Driver's personal device"]['driverID'], driversid_list[m]))
            comparison_results.append(jellyfish.jaro_similarity(data[n]["fleetTracker"]['driverID'], driversid_list[m]))
        # comparison_results.append('stop')
        for c in range(len(comparison_results)):
            if (comparison_results[c] == float(1)):
                tamperflag = False
                nontampered_sensors.append(data[n]["fleetTracker"]['driverID'])
                # print(tamperflag, data[n]["Driver's personal device"]['driverID'])
        comparison_results = []
        tamperflag = True

    for n in range(len(data)):
        if (data[n]["fleetTracker"]['driverID'] not in nontampered_sensors):
            tampered_sensors.append(data[n]["fleetTracker"]['driverID'])
            # print(data[n]["Driver's personal device"]['driverID'])

    return (nontampered_sensors,tampered_sensors)

def compare(str1,str2):
    cmp = jellyfish.jaro_similarity(str1, str2)
    return cmp
# for m in range(len(data[n]["Driver's personal device"])):
#     print(data[n]["Driver's personal device"]['driverID'])

# nt = tampering(data)

# float("37.97935862891567")