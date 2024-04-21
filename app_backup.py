from flask import Flask, jsonify, render_template, Response, request
import itertools
import kNNCalculation
import sparqltest
import pandas as pd
from kafka import KafkaConsumer
from flask_kafka import FlaskKafka
from threading import Event
import signal
import sys
import jellyfish
import mongoDB
import json
import pandas as pd
import io
import codecs
import os
import folium
from folium import plugins
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim, ArcGIS, GoogleV3 # Geocoder APIs
import setOutliers
import arrowhead_transactions
import address_geolocation
import driversid_tampering
from geopy.distance import geodesic
from pymongo import MongoClient
import mongo_cxb
import mongo_g4s
import logger_message_dummy
import kafka_testcons2
import mongo_alertlogger
import pickle
import numpy as np
import audit_trail_getLogs
import audit_trail_getOrders
import audit_trail_postLog
import audit_trail_postOrders
import audit_trail_getConfirmOrders
import audit_trail_postConfirmOrders
from datetime import datetime
from pam_ssh import pam_ssh
import mongo_pam

sys.setrecursionlimit(10000)

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# with open('./CXB_test.json') as json_file:
#     cxb = json.load(json_file)
# client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017')  # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
# db = client['testdb']
# # db.list_collection_names()
# collection = db['Monitor1']  # connect to specific collection(table)

# with open('./G4S_data_sample.json') as json_file:
#     g4s = json.load(json_file)

driversid_list = ['XFGRJYHN1235MM','XFGRJYHN5678MM','XFGRZSEN9012MM','XFGRZSEN5247MM']

filename = '/home/npeppes/communication_monitor_new/outlier_model.sav'
# load the trained isolation forest model for outlier detection from disk
loaded_model = pickle.load(open(filename, 'rb'))

# Select Communication Monitor Collection from the MongoDB - NOT Used at the moment
# monitor = mongoDB.coll()#example for sensorid fusion
# monitor1 = mongoDB.coll1()#example for digital signature fusion
########################################################################################################################
########################################################################################################################
@app.route('/')
@cross_origin()
def index():
    return 'Welcome to Communication Monitor'
########################################################################################################################
###############################################Visualization Tool#######################################################
# Communication Monitor Visualization scenario 1
@app.route('/graph1')#1st of july
def graph1():
   return render_template('testing.html')
########################################################################################################################
###############################################Visualization Tool#######################################################
# Communication Monitor Visualization scenario 1
@app.route('/abnormalgraph')#1st of july
def abnormalgraph():
   return render_template('testing11.html')
###############################################Visualization Tool#######################################################
# Communication Monitor Visualization scenario 1
@app.route('/transactionsgraph')#1st of july
def transactionsgraph():
   return render_template('testing12.html')
########################################################################################################################
###############################################Visualization Tool#######################################################
# Communication Monitor Visualization scenario 2
@app.route('/graph2')#1st of july
def graph2():
   return render_template('testing2.html')
########################################################################################################################
#######################################SensorID Fusion Creation#########################################################
########################################################################################################################
# @app.route('/sensorid')###NOT Used YET
# @cross_origin()
# def sensorid():
#     lam = mongoDB.return_mongo(monitor)
#
#     message = []
#     for i in range(len(lam)):
#         newMessage = {
#             'name': lam[i]['id'],  # probably without using a string, as its predefined as string
#             'source': lam[i]['source'],
#             'detail': lam[i]['detail'],
#             # 'lname': l[i],
#             # 'inc': inc[i],
#             # 'confid': str(c[i])
#         }
#         message.append(newMessage)
#     lam.clear()
#     # message.clear()
#     return jsonify(message)
########################################################################################################################
@app.route('/abdet')#OLD Approach, without ML Model
@cross_origin()
def abdet():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    amount = []
    for i in range(len(cxb)):
        amount.append(float(cxb[i]['purchaseInfo']["purchaseAmount"]))

    outlier, id = setOutliers.detect_outlier(amount)
    # outlier = ['a','v']#just before change the core functionality
    message = []
    for i in range(len(outlier)):
        newMessage = {
            'pan_id': cxb[id[i]]["panInfo"]["id"],
            'operation_name': cxb[id[i]]["operation"]["cardHolderName"],
            'outlier': outlier[i]  # critical to encircle the specific id for each list element
        }
        message.append(newMessage)
    # lam.clear()
    # message.clear()
    return jsonify(message)
####################################SignatureID Fusion Creation#########################################################
########################################################################################################################
# @app.route('/signatureid')
# @cross_origin()
# def signatureid():
#     lam = mongoDB.return_mongo(monitor1)
#
#     message = []
#     for i in range(len(lam)):
#         newMessage = {
#             'name': lam[i]['id'],  # probably without using a string, as its predefined as string
#             'detail': lam[i]['detail'],
#             'origin': lam[i]['origin'],
#             # 'lname': l[i],
#             # 'inc': inc[i],
#             # 'confid': str(c[i])
#         }
#         message.append(newMessage)
#     lam.clear()
#     # message.clear()
#     return jsonify(message)
######*****Empty SensorID Mongo Collection*****#####
########################################################################################################################
@app.route('/delmongo')
@cross_origin()
def delmongo():
    mongoDB.delete_all(monitor)
    return 'Deletion Executed'
######*****Empty Driver Signature Mongo Collection*****#####
########################################################################################################################
@app.route('/delmongo1')
@cross_origin()
def delmongo1():
    mongoDB.delete_all(monitor1)
    return 'Deletion Executed'
########################################################################################################################
@app.route('/delcxb')
@cross_origin()
def delcxb():
    collection = mongo_cxb.cxb()
    collection.delete_many({})
    # mongoDB.delete_all(monitor1)
    return 'CXB Collection Deleted'
########################################################################################################################
@app.route('/delg4s')
@cross_origin()
def delg4s():
    collection = mongo_g4s.g4s()
    collection.delete_many({})
    # mongoDB.delete_all(monitor1)
    return 'G4S Collection Deleted'
########################################################################################################################
@app.route('/delalert')
@cross_origin()
def delalert():
    collection = mongo_alertlogger.alertlogger()
    collection.delete_many({})
    # mongoDB.delete_all(monitor1)
    return 'Alert Logger Collection Deleted'
########################################################################################################################
@app.route('/delpam')
@cross_origin()
def delpam():
    collection = mongo_pam.pam()
    collection.delete_many({})
    # mongoDB.delete_all(monitor1)
    return 'Pam Collection Deleted'
########################################################################################################################
###############################################Fusion Section###########################################################
########################################################################################################################
# @app.route('/compareDrivers', methods=['GET'])
# @cross_origin()
# def compare_drivers():
#     try:
#         # personList = []
#         results = sparqltest.asyn()
#         personList = sparqltest.query_Demo(results=results)
#         similar_objects = kNNCalculation.calculate_nearest_neighbors(personList)
#
#         message = []
#         for i in range(len(similar_objects)):
#             newMessage = {
#                 'TableId': str(i + 1),
#                 'Person1_ID': str(similar_objects[i][0].id),
#                 # probably without using a string, as its predefined as string
#                 'Person1_Name': similar_objects[i][0].birthname,  # firstname
#                 'Person1_Surname': str(similar_objects[i][0].firstname),  # surname
#                 'Person2_ID': similar_objects[i][1].id,  # probably without using a string, as its predefined as string
#                 'Person2_Name': str(similar_objects[i][1].birthname),
#                 'Person2_Surname': str(similar_objects[i][1].firstname),
#                 'Confidence': str(similar_objects[i][2])
#             }
#             message.append(newMessage)
#         personList.clear()  # Clear the personList in order to avoid possible iterations over persons
#         results.clear()
#         return jsonify({"message": message})
#     except:
#         return ('A character error occured')
# ########################################################################################################################
# @app.route('/similarDrivers', methods=['GET'])
# @cross_origin()
# def similar_drivers():
#     try:
#         results = sparqltest.asyn()
#         personList = sparqltest.query_Demo(results=results)
#         similar_objects = kNNCalculation.calculate_nearest_neighbors_thres(personList)
#
#         message = []
#         for i in range(len(similar_objects)):
#             newMessage = {
#                 'TableId': str(i + 1),
#                 'Person1_ID': str(similar_objects[i][0].id),
#                 # probably without using a string, as its predefined as string
#                 'Person1_Name': similar_objects[i][0].birthname,
#                 'Person1_Surname': str(similar_objects[i][0].firstname),
#                 'Person2_ID': similar_objects[i][1].id,  # probably without using a string, as its predefined as string
#                 'Person2_Name': str(similar_objects[i][1].birthname),
#                 'Person2_Surname': str(similar_objects[i][1].firstname),
#                 'Confidence': str(similar_objects[i][2])
#             }
#             message.append(newMessage)
#         personList.clear()
#         results.clear()  # Clear the personList in order to avoid possible iterations over persons
#         return jsonify({"message": message})
#     except:
#         return ('A character error occured')
# ########################################################################################################################
# @app.route('/fusedDrivers', methods=['GET'])
# @cross_origin()
# def fused_drivers():
#     try:
#         results = sparqltest.asyn()
#         personList = sparqltest.query_Demo(results)
#         similar_objects = kNNCalculation.calculate_nearest_neighbors_thres(personList)
#
#         message = []
#         for i in range(len(similar_objects)):
#             newMessage = {
#                 'TableId': str(i + 1),
#                 'Fused_Person_id': str(similar_objects[i][0].id) + '/' + similar_objects[i][1].id,
#                 'Fused_Person_Name': similar_objects[i][0].birthname + '/' + str(similar_objects[i][1].birthname),
#                 'Fused_Person_Surname': str(similar_objects[i][0].firstname) + '/' + str(
#                     similar_objects[i][1].firstname),
#                 'Confidence': str(similar_objects[i][2])
#             }
#             message.append(newMessage)
#         personList.clear()  # Clear the personList in order to avoid possible iterations over persons
#         results.clear()
#         return jsonify(message)
#     except:
#         return ('A character error occured')
########################################################################################################################
@app.route('/transactionsdepiction', methods=['GET'])
@cross_origin()
def transactionsdepiction():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)

    message = []
    for i in range(len(cxb)):
        newMessage = {
            'pan_id': cxb[i]["panInfo"]["id"],
            'benign_scoring': cxb[i]['scoring']['benign_scoring'],
            'malicious_scoring': cxb[i]['scoring']['malicious_scoring'],
            'operation_pan': cxb[i]["operation"]["pan"],
            'operation_name': cxb[i]["operation"]["cardHolderName"],
            'operation_email': cxb[i]["operation"]["cardHolderEmails"],
            'operation_billaddress': cxb[i]["operation"]["billAddress"]+','+cxb[i]["operation"]["billAddrCity"]+','+cxb[i]["operation"]["billAddrPostcode"]+','+cxb[i]["operation"]["billAddrCountry"],
            'operation_shipaddress': cxb[i]["operation"]["shipAddress"]+','+cxb[i]["operation"]["shipAddrCity"]+','+cxb[i]["operation"]["shipAddrPostCode"]+','+cxb[i]["operation"]["shipAddrCountry"],
            'merchant_type': cxb[i]['merchanInfo']["merchantType"],
            'merchant_countrycode': cxb[i]['merchanInfo']["merchantCountryCode"],
            'merchant_name': cxb[i]['merchanInfo']["merchantName"],
            'merchant_riskindicator': cxb[i]['merchanInfo']["merchantRiskIndicator"],
            'purchase_amount': cxb[i]['purchaseInfo']["purchaseAmount"],
            'purchase_currency': cxb[i]['purchaseInfo']["purchaseCurrency"],
            'customerid_nif': cxb[i]["customerid"]["nif"],
            'customerid_nummid': cxb[i]["customerid"]["nummid"]
        }
        message.append(newMessage)
    # personList.clear()  # Clear the personList in order to avoid possible iterations over persons
    # results.clear()
    # cxb.clear()
    #'geo_ip':cxb[i]['geo_ip']['latitude']+','+cxb[i]['geo_ip']['longitude'],
    #'TableId': str(i + 1),
    return jsonify(message)
########################################################################################################################
@app.route('/transactionsdepictionoutput', methods=['GET'])
@cross_origin()
def transactionsdepictionoutput():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)

    message = []
    for i in range(len(cxb)):
        newMessage = {
            'source': cxb[i]["panInfo"]["id"],
            'detail': cxb[i]["operation"]["shipAddress"]+','+cxb[i]["operation"]["shipAddrCity"]+','+cxb[i]["operation"]["shipAddrPostCode"]+','+cxb[i]["operation"]["shipAddrCountry"],
            'name': cxb[i]['purchaseInfo']["purchaseAmount"],
        }
        message.append(newMessage)
    # personList.clear()  # Clear the personList in order to avoid possible iterations over persons
    # results.clear()
    # cxb.clear()
    #'geo_ip':cxb[i]['geo_ip']['latitude']+','+cxb[i]['geo_ip']['longitude'],
    #'TableId': str(i + 1),
    return jsonify(message)
########################################################################################################################
@app.route('/sensorsdepiction', methods=['GET'])
@cross_origin()
def sensorsdepiction():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)

    message = []
    for i in range(len(g4s)):
        newMessage = {
            'driverid': g4s[i]["Driver's personal device"]["driverID"],
            'driverimei': g4s[i]["Driver's personal device"]["IMEI"],
            'plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
            'odometer': g4s[i]["Fleet Management device monitoring the delivery truck"]["odometer"],
            'speed': g4s[i]["Fleet Management device monitoring the delivery truck"]["speed"],
            'engineStatus': g4s[i]["Fleet Management device monitoring the delivery truck"]["engineStatus"],
            'ignition': g4s[i]["Fleet Management device monitoring the delivery truck"]["ignition"],
            'temperature': g4s[i]["Fleet Management device monitoring the delivery truck"]["temperature"],
            'battery': g4s[i]["Fleet Management device monitoring the delivery truck"]["battery"],
            'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/transactionsgeolocation', methods=['GET'])
@cross_origin()
def transactionsgeolocation():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    message = []
    for i in range(len(cxb)):
        newMessage = {
            'pan_id': cxb[i]["panInfo"]["id"],
            'operation_pan': cxb[i]["operation"]["pan"],
            'operation_name': cxb[i]["operation"]["cardHolderName"],
            'operation_email': cxb[i]["operation"]["cardHolderEmails"],
            'operation_billaddress': cxb[i]["operation"]["billAddress"]+','+cxb[i]["operation"]["billAddrCity"]+','+cxb[i]["operation"]["billAddrPostcode"]+','+cxb[i]["operation"]["billAddrCountry"],
            'operation_shipaddress': cxb[i]["operation"]["shipAddress"]+','+cxb[i]["operation"]["shipAddrCity"]+','+cxb[i]["operation"]["shipAddrPostCode"]+','+cxb[i]["operation"]["shipAddrCountry"],
            'merchant_type': cxb[i]['merchanInfo']["merchantType"],
            'merchant_countrycode': cxb[i]['merchanInfo']["merchantCountryCode"],
            'merchant_name': cxb[i]['merchanInfo']["merchantName"],
            'merchant_riskindicator': cxb[i]['merchanInfo']["merchantRiskIndicator"],
            'purchase_amount': cxb[i]['purchaseInfo']["purchaseAmount"],
            'purchase_currency': cxb[i]['purchaseInfo']["purchaseCurrency"],
            'customerid_nif': cxb[i]["customerid"]["nif"],
            'customerid_nummid': cxb[i]["customerid"]["nummid"]
        }
        message.append(newMessage)
    # personList.clear()  # Clear the personList in order to avoid possible iterations over persons
    # results.clear()
    #'TableId': str(i + 1),
    return jsonify(message)
########################################################################################################################
# # (OLD APPROACH) Abnormal Detection Evaluation Initial Approach with the CLASSIC outlier detection
# @app.route('/abnormaldetection', methods=['GET'])
# @cross_origin()
# def abnormaldetection():
#     # outlier,id = setOutliers.detect_outlier(TransactionAmountL)
#     collection = mongo_cxb.cxb()
#     cursor = collection.find({})
#     cxb = []
#     for document in cursor:
#         cxb.append(document)
#     amount = []
#     for i in range(len(cxb)):
#         amount.append(float(cxb[i]['purchaseInfo']["purchaseAmount"]))
#
#     outlier, id = setOutliers.detect_outlier(amount)
#     # outlier = ['a','v']#just before change the core functionality
#     message = []
#     for i in range(len(outlier)):
#         newMessage = {
#             'Id': str(i+1),
#             'pan_id': cxb[id[i]]["panInfo"]["id"],
#             'operation_name': cxb[id[i]]["operation"]["cardHolderName"],
#             'outlier': outlier[i]# critical to encircle the specific id for each list element
#         }
#         message.append(newMessage)
#     # outlier.clear()
#
#     return jsonify(message)
# Abnormal Detection Evaluation Using Isolation Forest Trained Model
@app.route('/abnormaldetection', methods=['GET'])
@cross_origin()
def abnormaldetection():
    # outlier,id = setOutliers.detect_outlier(TransactionAmountL)
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    message = []
    for i in range(len(cxb)):
        res=float(cxb[i]['purchaseInfo']["purchaseAmount"])
        result = loaded_model.predict(np.array([res]).reshape(1, 1))
        # print(result)
        if (result==-1) and ((res<20)or(res>50000)):
            newMessage = {
                'Id': str(i+1),
                'pan_id': cxb[i]["panInfo"]["id"],
                'operation_name': cxb[i]["operation"]["cardHolderName"],
                'outlier': res
            }
            message.append(newMessage)
        else:
            pass
    # outlier.clear()
    return jsonify(message)
########################################################################################################################
# Abnormal Detection Evaluation
@app.route('/abnormaldetectionoutput', methods=['GET'])
@cross_origin()
def abnormaldetectionoutput():
    # outlier,id = setOutliers.detect_outlier(TransactionAmountL)
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    # amount = []
    # for i in range(len(cxb)):
    #     amount.append(float(cxb[i]['purchaseInfo']["purchaseAmount"]))
    #
    # outlier, id = setOutliers.detect_outlier(amount)
    # # outlier = ['a','v']#just before change the core functionality
    message = []
    for i in range(len(cxb)):
        res=float(cxb[i]['purchaseInfo']["purchaseAmount"])
        result = loaded_model.predict(np.array([res]).reshape(1, 1))
        if (result==-1) and ((res<20)or(res>50000)):
            newMessage = {
                # 'Id': str(i+1),
                'source': cxb[i]["panInfo"]["id"],
                'name': cxb[i]["operation"]["cardHolderName"],
                'detail': res  # critical to encircle the specific id for each list element
            }
            message.append(newMessage)
    # outlier.clear()
    return jsonify(message)
########################################################################################################################
# @app.route('/reversegeolocation')
# def reversegeolocation():
#     g = Nominatim(user_agent="new")  # You can tryout ArcGIS or GoogleV3 APIs to compare the results
#     message = []
#     for i in range(len(cxb)):
#         location = g.geocode(cxb[i]["operation"]["shipAddress"]+' '+cxb[i]["operation"]["shipAddrCity"])
#         newMessage = {
#             'reverse_geolocation': 'Geolocation conversion from the address:' + cxb[i]["operation"]["shipAddress"]+','+cxb[i]["operation"]["shipAddrCity"]
#                                      + ' equals to latitude:' + str(location.latitude) + ' and longitude:' + str(location.longitude)
#         }
#         message.append(newMessage)
#     return jsonify(message)
########################################################################################################################
@app.route('/visualizetransactions')
def visualizetransactions():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    map = folium.Map(location=[30.180778, 17.723805], tiles='Stamen Terrain',zoom_start=3,max_zoom=50000)#,tiles='Stamen Terrain')  # 'CartoDB dark_matter' & Initialize the Map
    # marker_cluster = MarkerCluster().add_to(map)
    locations, pan_id,purchase_amount, operation_shipaddress = address_geolocation.reverse(cxb)

    for n in range(len(locations)):
        folium.PolyLine(locations=[locations[n][0], locations[n][1]], color='red').add_to(map)
        folium.Marker(location=locations[n][0], icon=folium.Icon(color='green'), popup='Order Address'+ '\t' + 'Pan_ID: ' + str(pan_id[n]) + '\t' + 'Purchase Amount: ' + str(purchase_amount[n]) + '\t' + 'Operation Ship Address: ' + operation_shipaddress[n]).add_to(map)
        folium.Marker(location=locations[n][1], icon=folium.Icon(color='blue'), popup='Ship Address'+ '\t' + 'Pan_ID: ' + str(pan_id[n]) + '\t' + 'Purchase Amount: ' + str(purchase_amount[n])).add_to(map)
        arrows = arrowhead_transactions.getArrows(locations=[locations[n][0], locations[n][1]], n_arrows=3)
        for arrow in arrows:
            arrow.add_to(map)

    cxb.clear()
    return map._repr_html_()
########################################################################################################################
@app.route('/visualizedistances')
def visualizedistances():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    map = folium.Map(location=[30.180778, 17.723805], zoom_start=3, max_zoom=1000)  # ,tiles='Stamen Terrain')
    for i in range(len(g4s)):
        dis = geodesic((float(g4s[i]["Driver's personal device"]["latitude"]),
                        float(g4s[i]["Driver's personal device"]["longitude"])),
                       (float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"]),
                        float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"]))).meters

        if (dis >= float(100)):
            lat = float(g4s[i]["Driver's personal device"]["latitude"])
            lon = float(g4s[i]["Driver's personal device"]["longitude"])
            lat1 = float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"])
            lon1 = float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"])
            folium.PolyLine(locations=[[lat,lon], [lat1,lon1]], color='red').add_to(map)
            folium.Marker(location=[lat,lon], icon=folium.Icon(color='green',icon='fa-user', prefix='fa'), popup='Driver' + '\t'+ 'DriverID:' + g4s[i]["Driver's personal device"]["driverID"]).add_to(map)
            folium.Marker(location=[lat1,lon1], icon=folium.Icon(color='blue',icon='car', prefix='fa'), popup='Truck' + '\t'+ 'Plate:' + g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"]).add_to(map)
            arrows = arrowhead_transactions.getArrows(locations=[[lat,lon], [lat1,lon1]], n_arrows=3)
            for arrow in arrows:
                arrow.add_to(map)

    g4s.clear()
    return map._repr_html_()
########################################################################################################################
@app.route('/reasoning1')#CXB rule1
def reasoning1():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    # amount = []
    # for i in range(len(cxb)):
    #     amount.append(float(cxb[i]['purchaseInfo']["purchaseAmount"]))
    #
    # outlier, id = setOutliers.detect_outlier(amount)
    message = []
    for i in range(len(cxb)):
        res = float(cxb[i]['purchaseInfo']["purchaseAmount"])
        result = loaded_model.predict(np.array([res]).reshape(1, 1))
        if(((result == -1) and ((res < 20) or (res > 50000))) and (cxb[i]['scoring']['benign_scoring']<cxb[i]['scoring']['malicious_scoring'])):
            newMessage = {
                'Id': str(i + 1),
                'pan_id': cxb[i]["panInfo"]["id"],
                'operation_name': cxb[i]["operation"]["cardHolderName"],
                'outlier': res,  # critical to encircle the specific id for each list element
                'malicious_scoring': cxb[i]['scoring']['malicious_scoring'],
                'benign_scoring': cxb[i]['scoring']['benign_scoring'],
                'Alert_message': 'The current transaction is characterized as suspicious and needs to be furtherly investigated',
                'Alert_severity': 'high'
                }
            message.append(newMessage)
        elif(((result == -1) and ((res < 20) or (res > 50000))) and (cxb[i]['scoring']['benign_scoring']>cxb[i]['scoring']['malicious_scoring'])):
            newMessage = {
                'Id': str(i + 1),
                'pan_id': cxb[i]["panInfo"]["id"],
                'operation_name': cxb[i]["operation"]["cardHolderName"],
                'outlier': res,  # critical to encircle the specific id for each list element
                'malicious_scoring': cxb[i]['scoring']['malicious_scoring'],
                'benign_scoring': cxb[i]['scoring']['benign_scoring'],
                'Alert_message': 'The current transaction could be characterized as suspicious and needs to be furtherly investigated',
                'Alert_severity': 'medium'
                }
            message.append(newMessage)
    # outlier.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning2')#CXB rule2
def reasoning2():
    collection = mongo_cxb.cxb()
    cursor = collection.find({})
    cxb = []
    for document in cursor:
        cxb.append(document)
    message = []
    for i in range(len(cxb)):
        if((cxb[i]['scoring']['benign_scoring']<cxb[i]['scoring']['malicious_scoring']) and (cxb[i]['merchant_check']['known']==False) and (cxb[i]['merchant_country_check']['known']==False)):
            newMessage = {
                'Id': str(i + 1),
                'pan_id': cxb[i]["panInfo"]["id"],
                'operation_name': cxb[i]["operation"]["cardHolderName"],
                'malicious_scoring': cxb[i]['scoring']['malicious_scoring'],
                'benign_scoring': cxb[i]['scoring']['benign_scoring'],
                'merchant_check_know': str(cxb[i]['merchant_check']['known']),
                'merchant_country_check_know':str(cxb[i]['merchant_country_check']['known']),
                'Alert_message': 'The current transaction is characterized as suspicious and needs to be furtherly investigated'
                }
            message.append(newMessage)
    # outlier.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/drivertampering')#G4S
def drivertampering():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    ntm,tm = driversid_tampering.tampering(g4s,driversid_list)

    message = []

    for j in range(len(g4s)):
        for i in range(len(tm)):
            if(tm[i]==g4s[j]["Driver's personal device"]["driverID"]):
                newMessage = {
                    'driver_id': tm[i],
                    'truck_plate': g4s[j]["Fleet Management device monitoring the delivery truck"]["plate"],
                    'timestamp': g4s[j]["Driver's personal device"]["dateTimeUTC"],
                    'lat':float(g4s[j]["Driver's personal device"]["latitude"]),
                    'lon':float(g4s[j]["Driver's personal device"]["longitude"])
            }
                message.append(newMessage)
    # outlier.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/visualizedrivertampering')#G4S
def visualizedrivertampering():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    ntm,tm = driversid_tampering.tampering(g4s,driversid_list)

    map = folium.Map(location=[30.180778, 17.723805], zoom_start=3,max_zoom=1000)  # ,tiles='Stamen Terrain')  # 'CartoDB dark_matter' & Initialize the Map
    marker_cluster = MarkerCluster().add_to(map)
    for j in range(len(g4s)):
        for i in range(len(tm)):
            if(tm[i]==g4s[j]["Driver's personal device"]["driverID"]):
                lat = float(g4s[j]["Driver's personal device"]["latitude"])
                lon = float(g4s[j]["Driver's personal device"]["longitude"])
                folium.Marker([lat, lon],popup = 'Tampering Alert' + '\t' + 'Plate: ' + g4s[j]["Fleet Management device monitoring the delivery truck"]["plate"] + '\t'+ '\t' + 'Driver ID: ' + tm[i] + '\t' + 'Timestamp:' + g4s[j]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"],
                              icon=folium.Icon(color='red', icon_color='yellow', icon='car', prefix='fa')).add_to(map)

    g4s.clear()
    return map._repr_html_()
########################################################################################################################
@app.route('/drivertamperingdetails')#G4S
def drivertamperingdetails():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    ntm, tm = driversid_tampering.tampering(g4s, driversid_list)
    message = []

    if (len(tm)!=0):
        for m in range(len(driversid_list)):
            for n in range(len(tm)):
               newMessage = {
                'tamperedid': tm[n],
                'driverid': driversid_list[m],
                'comparison_result': driversid_tampering.compare(tm[n], driversid_list[m])
               }
            message.append(newMessage)
        # outlier.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning3')#G4S rule1
def reasoning3():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        if((g4s[i]["Fleet Management device monitoring the delivery truck"]["events"]["gsmJammed"]==True) or (g4s[i]["Fleet Management device monitoring the delivery truck"]["events"]["gpsAntennaRemoval"]==True)):
            if ((g4s[i]["Fleet Management device monitoring the delivery truck"]["events"]["gsmJammed"] == True)):
                newMessage = {
                    'Alert_Issue': 'GSM Jammed',
                    'Plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                    'Imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                    'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
                }
            elif((g4s[i]["Fleet Management device monitoring the delivery truck"]["events"]["gpsAntennaRemoval"] == True)):
                newMessage = {
                    'Alert_Issue': 'GPS Antenna Removal',
                    'Plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                    'Imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                    'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
                }
            message.append(newMessage)
        else:
            pass
    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning4')#G4S rule2 - Detect possible deviations between Driver's GPS and Fleet Management GPS
def reasoning4():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        dis = geodesic((float(g4s[i]["Driver's personal device"]["latitude"]),float(g4s[i]["Driver's personal device"]["longitude"])),
                                             (float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"]),float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"]))).meters
        newMessage = {
                    'Alert_Issue': "Distance computed between Driver's Personal Device and Fleet Management Device equal to:" + str(dis) + " meters",
                    'driveid': g4s[i]["Driver's personal device"]["driverID"],
                    'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                    'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                    'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
                }
        message.append(newMessage)

    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning5')#G4S rule3 - High GPS Deviation(s)
def reasoning5():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        dis = geodesic((float(g4s[i]["Driver's personal device"]["latitude"]),float(g4s[i]["Driver's personal device"]["longitude"])),
                                             (float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"]),float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"]))).meters

        if(dis>=float(100)):
            newMessage = {
                    'Alert_Issue': "A Distance Deviation detected between Driver's Personal Device and Fleet Management",
                    'deviation': str(dis) + ' meters',
                    'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                    'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                    'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
                }
            message.append(newMessage)
    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning4b')#G4S rule2A - Detect possible deviations between Asset Tracker's GPS and Fleet Management GPS for packet theft detection
def reasoning4b():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        dis = geodesic((float(g4s[i]["Asset tracker for the pharmacy products"]["latitude"]),float(g4s[i]["Asset tracker for the pharmacy products"]["longitude"])),
                       (float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"]),float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"]))).meters
        newMessage = {
            'Alert_Issue': "Distance computed between Asset Tracker's Personal Device and Fleet Management Device equal to:" + str(dis) + " meters",
            'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
            'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
            'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
            'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
        }
        message.append(newMessage)

    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning5b')#G4S rule3A - High Asset Tracker's GPS and Fleet Management GPS Deviation(s) (over or equal to 100 meters) for packet theft detection
def reasoning5b():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        dis = geodesic((float(g4s[i]["Asset tracker for the pharmacy products"]["latitude"]),float(g4s[i]["Asset tracker for the pharmacy products"]["longitude"])),
                       (float(g4s[i]["Fleet Management device monitoring the delivery truck"]["latitude"]),float(g4s[i]["Fleet Management device monitoring the delivery truck"]["longitude"]))).meters

        if(dis>=float(100)):
            newMessage = {
                'Alert_Issue': "A Packet Theft was detected",
                'deviation': str(dis) + " meters",
                'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
                'driveid': g4s[i]["Driver's personal device"]["driverID"],
                'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
            }
            message.append(newMessage)
    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning6')#G4S rule4 - Open/Closed Door(s) and Temperature Deviation(s)
def reasoning6():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        fleet_temp = g4s[i]["Fleet Management device monitoring the delivery truck"]["temperature"]
        fridge_temp = g4s[i]["Asset tracker for the pharmacy products"]["temperature"]
        temp_diff = fleet_temp - fridge_temp
        if((g4s[i]["Fleet Management device monitoring the delivery truck"]["door"]=="opened") and (temp_diff == float(0))):
            newMessage = {
                'Alert_Issue': "An opened door was detected but there is not observed any temperature difference as it's equal to:" + str(temp_diff) + " Celcius",
                'driveid': g4s[i]["Driver's personal device"]["driverID"],
                'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
                'temp_diff':temp_diff,
                'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]

            }
            message.append(newMessage)
        elif ((g4s[i]["Fleet Management device monitoring the delivery truck"]["door"] == "opened") and (temp_diff == float(0))):
            newMessage = {
                'Alert_Issue': "An opened door was detected with temperature difference equal to:" + str(temp_diff) + " Celcius",
                'driveid': g4s[i]["Driver's personal device"]["driverID"],
                'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
                'temp_diff': temp_diff,
                'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
            }
            message.append(newMessage)
        else:
            pass
    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/reasoning7')#G4S rule5 - Closed Door(s) and Temperature Deviation(s) leads to 'Broken Truck Status' (Latest Update)
def reasoning7():
    collection = mongo_g4s.g4s()
    cursor = collection.find({})
    g4s = []
    for document in cursor:
        g4s.append(document)
    message = []
    for i in range(len(g4s)):
        fleet_temp = g4s[i]["Fleet Management device monitoring the delivery truck"]["temperature"]
        fridge_temp = g4s[i]["Asset tracker for the pharmacy products"]["temperature"]
        temp_diff = fleet_temp - fridge_temp
        if((g4s[i]["Fleet Management device monitoring the delivery truck"]["door"]=="closed") and (fridge_temp>0) and (g4s[i]["Fleet Management device monitoring the delivery truck"]["speed"]==0)):
            newMessage = {
                'Alert_Issue': "It is observed a temperature difference in the asset tracker whilst the door is still closed and the truck is immobilized",
                'fleet_device_temp': fleet_temp,
                'fridge_temp': fridge_temp,
                'driveid': g4s[i]["Driver's personal device"]["driverID"],
                'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
                'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
                'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
                'temp_diff':temp_diff,
                'truck_speed':g4s[i]["Fleet Management device monitoring the delivery truck"]["speed"],
                'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]

            }
            message.append(newMessage)
        # elif ((g4s[i]["Fleet Management device monitoring the delivery truck"]["door"] == "opened") and (temp_diff == float(0))):
        #     newMessage = {
        #         'Alert_Issue': "An opened door was detected with temperature difference equal to:" + str(temp_diff) + " Celcius",
        #         'driveid': g4s[i]["Driver's personal device"]["driverID"],
        #         'truck_plate': g4s[i]["Fleet Management device monitoring the delivery truck"]["plate"],
        #         'truck_imei': g4s[i]["Fleet Management device monitoring the delivery truck"]["IMEI"],
        #         'asset_imei': g4s[i]["Asset tracker for the pharmacy products"]["IMEI"],
        #         'temp_diff': temp_diff,
        #         'timestamp': g4s[i]["Fleet Management device monitoring the delivery truck"]["dateTimeUTC"]
        #     }
        #     message.append(newMessage)
        # else:
        #     pass
    # outlier.clear()
    # message.clear()
    return jsonify(message)
########################################################################################################################
#@app.route('/alertlogger')#Alert Logger Dummy Example
@app.route('/alertlogger')#Alert Logger Dummy Example
def alertlogger():
    collection = mongo_alertlogger.alertlogger()
    cursor = collection.find({})
    alertlogger = []
    for document in cursor:
        alertlogger.append(document)
    message = []
    for i in range(len(alertlogger)):
        newMessage = {
            'alert message':alertlogger[i]['Alert_message'],
            'partner id':alertlogger[i]['partner_id'],
            'service name':alertlogger[i]['service_name'],
            'service type':alertlogger[i]['service_type'],
            'severity level':alertlogger[i]['severity_level'],
            'asset': alertlogger[i]['asset'],
            'alert timestamp':alertlogger[i]['alert_timestamp'],
            'detection timestamp': alertlogger[i]['detection_timestamp'],
            'set of data': alertlogger[i]['set_of_data'],
            }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/kafkatorest')#Alert Logger Dummy Example
def kafkatorest():
    w=kafka_testcons2.test(server='87.98.133.57:65196',topic='iccs_topic')
    #w=kafka_testcons2.test(server='147.102.40.97:9092',topic='iccs_topic')
    #w=test(server='147.102.40.97:9092',topic='iccs_topic')
    message = []
    for i in range(len(w)):
        newMessage = {
            'message': w[i]
            #'Behavior': w[i]['Driver Behavior']
            # 'service_name': cxb[i]["service_name"],
            # 'service_type': cxb[i]["service_type"],
            # 'timestamp': cxb[i]["timestamp"],
        }
        message.append(newMessage)
    w.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/allorders', methods=['GET'])
def allorders():
    #orders=audit_trail_getOrders.auditrailorders()
    # n['log']['payload']["orderID"]
    message = []
    ord = audit_trail_getOrders.auditrailorders()
    #conf = audit_trail_getConfirmOrders.auditrailconforders()
    for m in ord:
        newMessage = {
            'log_created': m['log']['created'],
            'type': m['log']['type'],
            'orderID': m['log']['payload']["orderID"],
            'status': m['log']['payload']['status'],
            'order_timestamp': m['log']['payload']['order_timestamp']
            }
        message.append(newMessage)
    # w.clear()
    return jsonify(message) 
########################################################################################################################
@app.route('/evaluateorders', methods=['GET'])
def evaluateorders():
    # orders=audit_trail_getOrders.auditrailorders()
    # n['log']['payload']["orderID"]
    args = request.args
    order = args.get('order',type=int)#the order has been declared as an integer in the audit trail
    message = []
    ord = audit_trail_getOrders.auditrailorders()#get all stored orders
    existord=audit_trail_getOrders.existingorderids()#list for checking if the orderID already existing in any channel
    existconf = audit_trail_getConfirmOrders.existingconforderids()
    # conf = audit_trail_getConfirmOrders.auditrailconforders()
    for n in ord:
        package_ord = n['log']['payload']['orderID']
        package_status = n['log']['payload']['status']
        if(order in existconf):
            message=[]
        else:
            if ((order==package_ord) and (package_status=='undelivered')):
                newMessage = {
                    'log_created': n['log']['created'],
                    'type': n['log']['type'],
                    'orderID': n['log']['payload']["orderID"],
                    'status': 'delivered',
                    'order_timestamp': (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")
                }
                message.append(newMessage)
                audit_trail_postOrders.auditrail(message[0])#save to order channel
                audit_trail_postConfirmOrders.auditrailconf(message[0])#save to confirmation channel
            else:
                pass

    return jsonify(message)
#############################################PAM ENDOPOINTS#############################################################
########################################################################################################################
@app.route('/pamgroup', methods=['GET'])
def pamgroup():
    message=[]
    group=pam_ssh('group')
    if (group['trackerGroups']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['trackerGroups'])):
            newMessage = {
                'group': group['trackerGroups'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/pamdriver', methods=['GET'])
def pamdriver():
    message=[]
    group=pam_ssh('driver')
    if (group['trackers']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['trackers'])):
            newMessage = {
                'group': group['trackers'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/pamfleet', methods=['GET'])
def pamfleet():
    message=[]
    group=pam_ssh('fleet')
    if (group['trackers']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['trackers'])):
            newMessage = {
                'group': group['trackers'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/pamasset', methods=['GET'])
def pamasset():
    message=[]
    group=pam_ssh('asset')
    if (group['trackers']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['trackers'])):
            newMessage = {
                'group': group['trackers'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/pamevent', methods=['GET'])
def pamevent():
    message=[]
    group=pam_ssh('event')
    if (group['events']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['events'])):
            newMessage = {
                'group': group['events'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/pamroute', methods=['GET'])
def pamroute():
    message=[]
    group=pam_ssh('route')
    if (group['deliveryRoutes']==[]):
        newMessage = group
        message.append(newMessage)
    else:
        for n in range(len(group['deliveryRoutes'])):
            newMessage = {
                'group': group['deliveryRoutes'][n]
            }
            message.append(newMessage)

    return jsonify(message)
########################################################################################################################e
@app.route('/realtimepam')#Alert Logger Dummy Example
def realtimepam():
    collection = mongo_pam.pam()
    cursor = collection.find({})
    pamlist=[]
    for n in cursor:
        pamlist.append(n['data'])#["Driver's personal device"])
    message = []
    for i in range(len(pamlist)):
        newMessage = {
             'data': pamlist[i]
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
#@app.route('/search', methods=['GET'])
#def search():
#    #?order=3918124921#Valid Order
#    #You can additionally cast the value to a different type, such as int or str while getting it.
#    # You can also set a default value if the value isn't present already.
#    # args.get("name", default="", type=str)
#    # args.get("price", default=0, type=int)
#    a=audit_trail_getOrders.auditrailorders()
#    # list_of_dictionaries = [{"order": 48392489238432, "timestamp":'22/02/2022'}
#    #     ,{"order": 48392489238434, "timestamp": '21/03/2021'}]
#    #?order=3918124921-->this is a valid stored order
#    args = request.args
#    order = args.get('order',type=int)#the order has been declared as an integer in the audit trail
#    # timestamp = args.get('timestamp',default="",type=str)
#    found_values=[]
#    # for dictionary in list_of_dictionaries:
#    #Read Predefined orders
#    for n in a:
#        if (('orderID' in n['log']['payload']) and (n['log']['payload']["orderID"] == order)):
#            orda=n['log']['payload']
#            print(n['log']['payload'])
#            found_values.append(orda)
#    else:
#        print(order)
#        pass
#    if len(found_values)!=0:
#        return jsonify(found_values)
#    else:
#        nonvalid=[{"orderID": order,
#                   "status": 'Not a valid order',
#                   "timestamp": (datetime.now()).strftime("%d-%b-%Y (%H:%M:%S)")
#                   }]
#        return jsonify(nonvalid)
#        # return 'Not a valid order'
########################################################################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,ssl_context=("/etc/letsencrypt/live/communicationmonitor.cn.ntua.gr/fullchain.pem", "/etc/letsencrypt/live/communicationmonitor.cn.ntua.gr/privkey.pem"))
