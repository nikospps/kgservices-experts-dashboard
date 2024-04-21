from flask import Flask, jsonify, render_template, Response, request
import get_ca
import get_meaa
import get_vs
import get_fer
import get_ga
import get_sa
import get_wcs
import itertools
import pandas as pd
from kafka import KafkaConsumer
from flask_kafka import FlaskKafka
import sys
import jellyfish
import mongoDB
import mongo_meaa
import mongo_fitbitSleep
import mongo_fitbitSummary
import mongo_fitbitHeartTimeline
import mongo_ca
import mongo_meaaDB
import json
import pandas as pd
import os
from pymongo import MongoClient
import kafka_testcons2
import pickle
import numpy as np
from datetime import datetime
import timestamp_conversion
from flask_cors import CORS, cross_origin
#from IAM import add_quote
import get_wellics_daily
import get_wellics_sleep
from IAM import users_profiles,login,add_quote,status,cross_correlation #, access_token
import IAM
import patients_lists
import patients_filter
from get_allPatients import get_latestPatients
import get_alert
#import read_json

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
user_profile = IAM.users_profiles("iccs-service@cn.ntua.gr","dFpiyRclN2nS6ES63ubIOifGuJdwvZia5fcnqPq6")
access_token = IAM.access_token("iccs-service@cn.ntua.gr","dFpiyRclN2nS6ES63ubIOifGuJdwvZia5fcnqPq6")
get_lp = get_latestPatients(access_token)
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
#app.logger.disabled = True
#log.disabled = True

#meaa=get_meaa.get_meaa() #in order to provide somehow real-time capabilities to this endpoint due to huge amount of data
#filename = '/home/nikospps/Projects_Codes_Development/communication_monitor_new/outlier_model.sav'#to run it locally
#filename = '/home/npeppes/experts_dashboard/all_patients.json'#to run it remotely
#patients = read_json()
# load the trained isolation forest model for outlier detection from disk
# loaded_model = pickle.load(open(filename, 'rb'))
# Select Communication Monitor Collection from the MongoDB - NOT Used at the moment
# monitor = mongoDB.coll()#example for sensorid fusion
# monitor1 = mongoDB.coll1()#example for digital signature fusion
#Fitbit Daily Summary
fism_init = get_wellics_daily.get_fbdaily(access_token)
nkua = []
fism = []
suub = []
#append fitbit_daily to nkua
for n in fism_init:
    result1 = patients_filter.patients_filter([n], patients_lists.list_nkua)
    if (result1 == True):
        nkua.append(n)
#append fitbit_daily to fism
for m in fism_init:
    result2 = patients_filter.patients_filter([m], patients_lists.list_fism)
    if (result2 == True):
        fism.append(m)
#append fitbit_daily to suub
for l in fism_init:
    result3 = patients_filter.patients_filter([l], patients_lists.list_suub)
    if (result3 == True):
        suub.append(l)
#Fitbit Sleep
fbsleep = get_wellics_sleep.get_fbsleep(access_token)
nkua_sleep = []
fism_sleep = []
suub_sleep = []
#append fitbit_sleep to nkua
for n1 in fbsleep:
    result1a = patients_filter.patients_filter([n1], patients_lists.list_nkua)
    if (result1a == True):
        nkua_sleep.append(n1)
#append fitbit_sleep to fism
for m1 in fbsleep:
    result2a = patients_filter.patients_filter([m1], patients_lists.list_fism)
    if (result2a == True):
        fism_sleep.append(m1)
#append fitbit_sleep to suub
for l1 in fbsleep:
    result3a = patients_filter.patients_filter([l1], patients_lists.list_suub)
    if (result3a == True):
        suub_sleep.append(l1)
########################################################################################################################
########################################################################################################################
@app.route('/')
@cross_origin()
def index():
    return 'Welcome to Experts Dashboard'
########################################################################################################################
########################################################################################################################
@app.route('/userprofiles')
@cross_origin()
def userprofiles():
    message = []
    newMessage = {
            'ID': user_profile['id'],
            'firstName': user_profile['firstName'],
            'lastName': user_profile['lastName'],
            'email': user_profile['email'],
            'emailVerified': user_profile['emailVerified'],
            'accessToken': access_token
            # 'roles': user_profile['roles'],
            # 'groups': user_profile['groups']
        }
    message.append(newMessage)
    # ca.clear()
    return jsonify(message)
########################################################################################################################
########################################################################################################################
@app.route('/delmeaa')
@cross_origin()
def delmeaa():
    collection = mongo_meaa.meaa()
    collection.delete_many({})
    # mongoDB.delete_all(monitor1)
    return 'MEAA Collection was Deleted'
########################################################################################################################
#################################################LP Services############################################################
@app.route('/lp', methods=['GET'])
@cross_origin()
def lp():
    message = []
    for n in get_lp:
        newMessage = {
            'UserID': n['id'],
            'email': n['email'],
            'firstName': n['firstName'],
            'lastName': n['lastName']
        }
        message.append(newMessage)

    return jsonify(message)
#################################################CA Services############################################################
@app.route('/ca1', methods=['GET'])
@cross_origin()
def ca1():
    ca=get_ca.get_ca(access_token)
    message = []
    for n in ca:
        if ('userID' not in n):
            continue
        else:
            newMessage = {
                #'ID_observation': n["observationID"],
                'ID_user': n["userID"],
                'message': n['message'],
                'source': n["source"],
                'negative_mood(%)': n["results"][0]['score'],
                'neutral_mood(%)': n["results"][1]['score'],
                'positive_mood(%)': n["results"][2]['score'],
                'timestamp': n["timestamp"]
            }
            message.append(newMessage)

    # ca.clear()
    return jsonify(message)
#################################################CA Services############################################################
@app.route('/ca', methods=['GET'])
@cross_origin()
def ca():
    ca=get_ca.get_ca(access_token)
    message = []
    for n in ca:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    newMessage = {
                        # 'ID_observation': n["observationID"],
                        'Email_user': l['email'],
                        'ID_user': n["userID"],
                        'message': n['message'],
                        'source': n["source"],
                        'negative_mood(%)': n["results"][0]['score'],
                        'neutral_mood(%)': n["results"][1]['score'],
                        'positive_mood(%)': n["results"][2]['score'],
                        'timestamp': n["timestamp"]
                    }
                    message.append(newMessage)
    # ca.clear()
    return jsonify(message)
#################################################CA NKUA################################################################
@app.route('/ca_nkua', methods=['GET'])
@cross_origin()
def ca_nkua():
    ca=get_ca.get_ca(access_token)
    message = []
    for n in ca:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_nkua)
                    if(result==True):
                        newMessage = {
                            # 'ID_observation': n["observationID"],
                            'Email_user': l['email'],
                            #'ID_user': n["userID"],
                            'message': n['message'],
                            'source': n["source"],
                            'organization': 'NKUA',
                            'negative_mood(%)': n["results"][0]['score'],
                            'neutral_mood(%)': n["results"][1]['score'],
                            'positive_mood(%)': n["results"][2]['score'],
                            'timestamp': n["timestamp"]
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
#################################################CA FISM################################################################
@app.route('/ca_fism', methods=['GET'])
@cross_origin()
def ca_fism():
    ca=get_ca.get_ca(access_token)
    message = []
    for n in ca:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_fism)
                    if(result==True):
                        newMessage = {
                            # 'ID_observation': n["observationID"],
                            'Email_user': l['email'],
                            #'ID_user': n["userID"],
                            'message': n['message'],
                            'source': n["source"],
                            'organization': 'FISM',
                            'negative_mood(%)': n["results"][0]['score'],
                            'neutral_mood(%)': n["results"][1]['score'],
                            'positive_mood(%)': n["results"][2]['score'],
                            'timestamp': n["timestamp"]
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
#################################################CA SUUB################################################################
@app.route('/ca_suub', methods=['GET'])
@cross_origin()
def ca_suub():
    ca=get_ca.get_ca(access_token)
    message = []
    for n in ca:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_suub)
                    if(result==True):
                        newMessage = {
                            # 'ID_observation': n["observationID"],
                            'Email_user': l['email'],
                            #'ID_user': n["userID"],
                            'message': n['message'],
                            'source': n["source"],
                            'organization': 'SUUB',
                            'negative_mood(%)': n["results"][0]['score'],
                            'neutral_mood(%)': n["results"][1]['score'],
                            'positive_mood(%)': n["results"][2]['score'],
                            'timestamp': n["timestamp"]
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/mongoca', methods=['GET'])
@cross_origin()
def mongoca():
    collection = mongo_ca.ca()
    ca = collection.find()
    message = []
    for n in ca:
        newMessage = {
            '_UserID': n['user_id'],
            'source': n["source"],
            'mood_Positive (%)': n['observations'][0]['sentiment_scores'][0]['sentiment_score'],
            'mood_Neutral (%)': n['observations'][0]['sentiment_scores'][1]['sentiment_score'],
            'mood_Negative (%)': n['observations'][0]['sentiment_scores'][2]['sentiment_score'],
            'mood_explanation': n['observations'][0]['explanation'],
            'timestamp': n['observations'][0]['timestamp']
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/meaa', methods=['GET'])
@cross_origin()
def meaa():
    meaa=get_meaa.get_meaa(access_token)
    message = []
    for n in meaa:
        if ('user_id' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['user_id']):
                    pass
                else:
                    newMessage = {
                        'Email_user': l['email'],
                        # 'ID_observation': n["observationID"],
                        'ID_user': n['user_id'],
                        'questionnaireID': n['questionnaireID'],
                        'source': n["source"],
                        'overallSentiment': n['overallSentiment'],
                        'overallScore': n['overallScore'],
                        'timestamp': timestamp_conversion.conv(n['sessionStarted'])
                        # 'negative_mood (%)': n["results"][0]['score'],
                        # 'neutral_mood (%)': n["results"][1]['score'],
                        # 'positive_mood (%)': n["results"][3]['score'],
                        # 'other_mood (%)': n["results"][2]['score'],
                        # 'timestamp': timestamp_conversion.conv(n['sessionStarted']),
                    }
                    message.append(newMessage)
    # ca.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/meaa2', methods=['GET'])
@cross_origin()
def meaa2():
    #meaa=get_meaa.get_meaa()#This command is supposed to work for real time interaction with SemKG in case we don't have timeouts
    collection = mongo_meaaDB.meaaDB()
    meaa  = collection.find({})
    message = []
    #collection = mongo_meaa.meaa()
    #meaa = collection.find()
    message = []
    for n in meaa:
        newMessage = {
            #'ID_observation': n["observationID"],
            'ID_user': n['user_id'],
            'questionnaireID': n['questionnaireID'],
            'source': n["source"],
            'overallSentiment': n['overallSentiment'],
            'overallScore': n['overallScore'],
            'timestamp': timestamp_conversion.conv(n['sessionStarted'])
            #'negative_mood (%)': n["results"][0]['score'],
            #'neutral_mood (%)': n["results"][1]['score'],
            #'positive_mood (%)': n["results"][3]['score'],
            #'other_mood (%)': n["results"][2]['score'],
            #'timestamp': timestamp_conversion.conv(n['sessionStarted']),
        }
        message.append(newMessage)

    # meaa.clear()
    return jsonify(message)
#################################################MEAA NKUA##############################################################
@app.route('/meaa_nkua', methods=['GET'])
@cross_origin()
def meaa_nkua():
    meaa = get_meaa.get_meaa(access_token)
    message = []
    for n in meaa:
        if ('user_id' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['user_id']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_nkua)
                    if(result==True):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_observation': n["observationID"],
                            #'ID_user': n['user_id'],
                            'questionnaireID': n['questionnaireID'],
                            'source': n["source"],
                            'overallSentiment': n['overallSentiment'],
                            'overallScore': n['overallScore'],
                            'organization': 'NKUA',
                            'timestamp': timestamp_conversion.conv(n['sessionStarted'])
                            # 'negative_mood (%)': n["results"][0]['score'],
                            # 'neutral_mood (%)': n["results"][1]['score'],
                            # 'positive_mood (%)': n["results"][3]['score'],
                            # 'other_mood (%)': n["results"][2]['score'],
                            # 'timestamp': timestamp_conversion.conv(n['sessionStarted']),
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
#################################################MEAA FISM##############################################################
@app.route('/meaa_fism', methods=['GET'])
@cross_origin()
def meaa_fism():
    meaa = get_meaa.get_meaa(access_token)
    message = []
    for n in meaa:
        if ('user_id' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['user_id']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_fism)
                    if(result==True):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_observation': n["observationID"],
                            #'ID_user': n['user_id'],
                            'questionnaireID': n['questionnaireID'],
                            'source': n["source"],
                            'overallSentiment': n['overallSentiment'],
                            'overallScore': n['overallScore'],
                            'organization': 'FISM',
                            'timestamp': timestamp_conversion.conv(n['sessionStarted'])
                            # 'negative_mood (%)': n["results"][0]['score'],
                            # 'neutral_mood (%)': n["results"][1]['score'],
                            # 'positive_mood (%)': n["results"][3]['score'],
                            # 'other_mood (%)': n["results"][2]['score'],
                            # 'timestamp': timestamp_conversion.conv(n['sessionStarted']),
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
#################################################MEAA FISM##############################################################
@app.route('/meaa_suub', methods=['GET'])
@cross_origin()
def meaa_suub():
    meaa = get_meaa.get_meaa(access_token)
    message = []
    for n in meaa:
        if ('user_id' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['user_id']):
                    pass
                else:
                    result = patients_filter.patients_filter([n],patients_lists.list_suub)
                    if(result==True):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_observation': n["observationID"],
                            #'ID_user': n['user_id'],
                            'questionnaireID': n['questionnaireID'],
                            'source': n["source"],
                            'overallSentiment': n['overallSentiment'],
                            'overallScore': n['overallScore'],
                            'organization': 'SUUB',
                            'timestamp': timestamp_conversion.conv(n['sessionStarted'])
                            # 'negative_mood (%)': n["results"][0]['score'],
                            # 'neutral_mood (%)': n["results"][1]['score'],
                            # 'positive_mood (%)': n["results"][3]['score'],
                            # 'other_mood (%)': n["results"][2]['score'],
                            # 'timestamp': timestamp_conversion.conv(n['sessionStarted']),
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/meaa1', methods=['GET'])
@cross_origin()
def meaa1():
    meaa=get_meaa.get_meaa(access_token)#This command is supposed to work for real time interaction with SemKG in case we don't have timeouts
    #collection = mongo_meaaDB.meaaDB()
    #meaa  = collection.find({})
    message = []
    #collection = mongo_meaa.meaa()
    #meaa = collection.find()
    #message = []
    for n in meaa:
        newMessage = {
            #'ID_observation': n["observationID"],
            'ID_user': n['user_id'],
            'questionnaireID': n['questionnaireID'],
            'source': n["source"],
            'overallSentiment': n['overallSentiment'],
            'overallScore': n['overallScore'],
            'timestamp': timestamp_conversion.conv(n['sessionStarted'])
            #'negative_mood (%)': n["results"][0]['score'],
            #'neutral_mood (%)': n["results"][1]['score'],
            #'positive_mood (%)': n["results"][3]['score'],
            #'other_mood (%)': n["results"][2]['score'],
            #'timestamp': timestamp_conversion.conv(n['sessionStarted']),
        }
        message.append(newMessage)

    # meaa.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/meaareal', methods=['GET'])
@cross_origin()
def meaareal():
    #meaa=get_meaa.get_meaa()#This command is supposed to work for real time interaction with SemKG in case we don't have timeouts
    collection = mongo_meaaDB.meaaDB()
    meaa  = collection.find({})
    message = []
    #collection = mongo_meaa.meaa()
    #meaa = collection.find()
    message = []
    for n in meaa:
        newMessage = {
            #'ID_observation': n["observationID"],
            'ID_user': n['user_id'],
            'questionnaireID': n['questionnaireID'],
            'source': n["source"],
            'overallSentiment': n['overallSentiment'],
            'overallScore': n['overallScore'],
            'timestamp': n['sessionStarted']
            #'negative_mood (%)': n["results"][0]['score'],
            #'neutral_mood (%)': n["results"][1]['score'],
            #'positive_mood (%)': n["results"][3]['score'],
            #'other_mood (%)': n["results"][2]['score'],
            #'timestamp': timestamp_conversion.conv(n['sessionStarted']),
        }
        message.append(newMessage)

    # meaa.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/meaaiso', methods=['GET'])
@cross_origin()
def meaaiso():
    #meaa=get_meaa.get_meaa()
    args = request.args
    order = args.get('order', type=str) # the order/userID received from the specific argument for the current select>
    # order1 = str(order)
    collection = mongo_meaa.meaa()
    meaa = collection.find()
    message = []
    for n in meaa:
        if(n['userID']==order):
            newMessage = {
                #'ID_observation': n["observationID"],
                'ID_user': n['userID'],
                'order':order,
                'source': n["source"],
                'negative_mood (%)': n["results"][0]['score'],
                'neutral_mood (%)': n["results"][1]['score'],
                'positive_mood (%)': n["results"][3]['score'],
                'other_mood (%)': n["results"][2]['score'],
                'timestamp': n["timestamp"],
            }
            message.append(newMessage)
        else:
            pass

    # meaa.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/vs', methods=['GET'])
@cross_origin()
def vs():
    vs=get_vs.get_vs(access_token)
    message = []
    for n in vs:
        if ('message' not in n):
            continue
        else:
            newMessage = {
                'observationID': n["observationID"],
                'userID': n['userID'],
                'message': n['message'],
                'source': n["source"],
                'duration': n['duration'],
                'timestamp': n["timestamp"],
            }
            message.append(newMessage)

    # ca.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/fer', methods=['GET'])
@cross_origin()
def fer():
    fer=get_fer.get_fer(access_token)
    message = []
    for n in fer:
        newMessage = {
            #'ID_observation': n["observationID"],
            'ID_user': n['userID'],
            'source': n["source"],
            'Mood_Angry': n["results"][0]['score'],
            'Mood_Happy': n["results"][1]['score'],
            'Mood_Neutral': n["results"][2]['score'],
            'Mood_Sad': n["results"][3]['score'],
            'timestamp': n["timestamp"],
        }
        message.append(newMessage)
    # fer.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/ga', methods=['GET'])
@cross_origin()
def ga():
    ga=get_ga.get_ga(access_token)
    message = []
    for n in ga:
        newMessage = {
            #'ID_observation': n["observationID"],
            '_UserID': n['userID'],
            'source': n["source"],
            'gait_class_Walking': n["results"][0]['score'],
            'gait_class_Jogging': n["results"][1]['score'],
            'gait_clas__Walking_upstairs': n["results"][2]['score'],
            'gait_class__Walking_downstairs': n["results"][3]['score'],
            'gait_class__Sitting': n["results"][4]['score'],
            'gait_class__Standing': n["results"][5]['score'],
            'timestamp': n["timestamp"],
        }
        message.append(newMessage)
    # fer.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/sa', methods=['GET'])
@cross_origin()
def sa():
    sa=get_sa.get_sa(access_token)
    message = []
    for n in sa:
        if ('userId' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userId']):
                    pass
                else:
                    newMessage = {
                        'Email_user': l['email'],
                        'source': n["source"],
                        'result_wakeupDuration': n["sleepResults"][0]['score'],
                        'result_remSleepduration': n["sleepResults"][3]['score'],
                        'result_sleepEfficiency': n["sleepResults"][7]['score'],
                        'result_nbRemEpisodes': n["sleepResults"][11]['score'],
                        'result_deepSleepDuration': n["sleepResults"][14]['score'],
                        'result_SleepScore': n["sleepResults"][23]['score'],
                        'timestamp_start': n["start_date"],
                        'timestamp_end': n['end_date']
                    }
                    message.append(newMessage)
    # ca.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/sa1', methods=['GET'])
@cross_origin()
def sa1():
    sa=get_sa.get_sa(access_token)
    message = []
    for n in sa:
        newMessage = {
            #'ID_observation': n["observationID"],
            'ID_user': n['userId'],
            'source': n["source"],
            'result_wakeupDuration': n["sleepResults"][0]['score'],
            'result_remSleepduration': n["sleepResults"][3]['score'],
            'result_sleepEfficiency': n["sleepResults"][7]['score'],
            'result_nbRemEpisodes': n["sleepResults"][11]['score'],
            'result_deepSleepDuration': n["sleepResults"][14]['score'],
            'result_SleepScore': n["sleepResults"][23]['score'],
            'timestamp_start': n["start_date"],
            'timestamp_end': n['end_date']
        }
        message.append(newMessage)
    # fer.clear()
    return jsonify(message)
################################################WCS Services############################################################
@app.route('/wcs', methods=['GET'])
@cross_origin()
def wcs():
    wcs=get_wcs.get_wcs(access_token)
    message = []
    for n in wcs:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    newMessage = {
                        'Email_user': l['email'],
                        #'ID_questionnaire': n["questionnaireID"],
                        'ID_user': n['userID'],
                        'source': n["source"],
                        'title': n['title'],
                        'mood': n['scores'][0]['mood'],
                        'score': n['scores'][0]['score'],
                        # 'score_Cognitive': n["scores"][0]['score'],
                        # 'score_Physical': n["scores"][2]['score'],
                        # 'score_Psychological': n["scores"][3]['score'],
                        # 'score_Total': n["scores"][1]['score'],
                        'disease': n["disease"],
                        'abbreviation': n["abbreviation"],
                        'timestamp': str(n["timestamp"].split('.')[0]),  # timestamp_conversion.conv(n["timestamp"]),
                        'partner': n['partner']
                    }
                    message.append(newMessage)
    # ca.clear()
    return jsonify(message)
################################################WCS NKUA################################################################
@app.route('/wcs_nkua', methods=['GET'])
@cross_origin()
def wcs_nkua():
    wcs=get_wcs.get_wcs(access_token)
    message = []
    for n in wcs:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    if(n['partner']=='NKUA'):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_questionnaire': n["questionnaireID"],
                            #'ID_user': n['userID'],
                            'source': n["source"],
                            'title': n['title'],
                            'mood': n['scores'][0]['mood'],
                            'score': n['scores'][0]['score'],
                            # 'score_Cognitive': n["scores"][0]['score'],
                            # 'score_Physical': n["scores"][2]['score'],
                            # 'score_Psychological': n["scores"][3]['score'],
                            # 'score_Total': n["scores"][1]['score'],
                            'disease': n["disease"],
                            'abbreviation': n["abbreviation"],
                            'timestamp': str(n["timestamp"].split('.')[0]),
                            # timestamp_conversion.conv(n["timestamp"]),
                            'partner': 'NKUA'
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
################################################WCS FISM################################################################
@app.route('/wcs_fism', methods=['GET'])
@cross_origin()
def wcs_fism():
    wcs=get_wcs.get_wcs(access_token)
    message = []
    for n in wcs:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    if(n['partner']=='FISM'):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_questionnaire': n["questionnaireID"],
                            #'ID_user': n['userID'],
                            'source': n["source"],
                            'title': n['title'],
                            'mood': n['scores'][0]['mood'],
                            'score': n['scores'][0]['score'],
                            # 'score_Cognitive': n["scores"][0]['score'],
                            # 'score_Physical': n["scores"][2]['score'],
                            # 'score_Psychological': n["scores"][3]['score'],
                            # 'score_Total': n["scores"][1]['score'],
                            'disease': n["disease"],
                            'abbreviation': n["abbreviation"],
                            'timestamp': str(n["timestamp"].split('.')[0]),
                            # timestamp_conversion.conv(n["timestamp"]),
                            'partner': 'FISM'
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
################################################WCS SUUB################################################################
@app.route('/wcs_suub', methods=['GET'])
@cross_origin()
def wcs_suub():
    wcs=get_wcs.get_wcs(access_token)
    message = []
    for n in wcs:
        if ('userID' not in n):
            pass
        else:
            for l in get_lp:
                if (l['id'] != n['userID']):
                    pass
                else:
                    if(n['partner']=='SUUB'):
                        newMessage = {
                            'Email_user': l['email'],
                            # 'ID_questionnaire': n["questionnaireID"],
                            #'ID_user': n['userID'],
                            'source': n["source"],
                            'title': n['title'],
                            'mood': n['scores'][0]['mood'],
                            'score': n['scores'][0]['score'],
                            # 'score_Cognitive': n["scores"][0]['score'],
                            # 'score_Physical': n["scores"][2]['score'],
                            # 'score_Psychological': n["scores"][3]['score'],
                            # 'score_Total': n["scores"][1]['score'],
                            'disease': n["disease"],
                            'abbreviation': n["abbreviation"],
                            'timestamp': str(n["timestamp"].split('.')[0]),
                            # timestamp_conversion.conv(n["timestamp"]),
                            'partner': 'SUUB'
                        }
                        message.append(newMessage)
                    else:
                        pass
    # ca.clear()
    return jsonify(message)
#####################################################################################################################>
@app.route('/wcs1', methods=['GET'])
@cross_origin()
def wcs1():
    wcs=get_wcs.get_wcs(access_token)
    message = []
    for n in wcs:
        newMessage = {
            'ID_questionnaire': n["questionnaireID"],
            'ID_user': n['userID'],
            'source': n["source"],
            'title': n['title'],
            'mood': n['scores'][0]['mood'],
            'score': n['scores'][0]['score'],
            #'score_Cognitive': n["scores"][0]['score'],
            #'score_Physical': n["scores"][2]['score'],
            #'score_Psychological': n["scores"][3]['score'],
            #'score_Total': n["scores"][1]['score'],
            'disease': n["disease"],
            'abbreviaation': n["abbreviation"],
            'timestamp': str(n["timestamp"].split('.')[0]), #timestamp_conversion.conv(n["timestamp"]),
            'partner': n['partner']
        }
        message.append(newMessage)
    # fer.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/fbsleep', methods=['GET'])
@cross_origin()
def fbsleep():
    collection = mongo_fitbitSleep.fitbitsleep()
    fbsleep = collection.find()
    message = []
    for n in fbsleep:
        newMessage = {
            'awakeCount': n['awake_count'],
            'awakeDuration': n['awake_duration'],
            'awakeningsCount': n['awakenings_count'],
            'duration': n['duration'],
            'efficiency': n['efficiency'],
            'isMainSleep': int(n['is_main_sleep']),
            #'logId': n['log_id'],
            'minutesAfterWakeup': n['minutes_after_wakeup'],
            'minutesAsleep':n['minutes_awake'],
	    'minutesToFallAsleep':n['minutes_to_fall_asleep'],
	    'restlessCount': n['restless_count'],
	    'restlessDuration': n['restless_duration'],
	    'timeInBed': n['time_in_bed'],
            'deep': n['deep'],
            'light': n['light'],
            'wake': n['wake'],
            'rem':n['rem'],
            '_Patient_uuid': n['employee_uuid'],
            'dateOfSleep': n['date_of_sleep'],
            'startTime': n['start_time'],
            'endTime': n['end_time']
        }
        message.append(newMessage)

    # meaa.clear()
    return jsonify(message)
########################################################################################################################
@app.route('/fbsleep_nkua', methods=['GET'])
@cross_origin()
def fbsleep_nkua():
    # fbsleep = get_wellics_sleep.get_fbsleep(access_token)
    message = []
    for n in nkua_sleep:
        newMessage = {
            'awakeCount': n['awakeCount'],
            'awakeDuration': n['awakeDuration'],
            'awakeningsCount': n['awakeningsCount'],
            'duration': n['duration'],
            'efficiency': n['efficiency'],
            'email': n['email'],
            'isMainSleep': int(n['mainSleep']),
            #'logId': n['logId'],
            'minutesAsleep': n['minutesAsleep'],
            'minutesAwake': n['minutesAwake'],
            'minutesAfterWakeup': n['minutesAfterWakeup'],
	    'minutesToFallAsleep':n['minutesToFallAsleep'],
	    'restlessCount': n['restlessCount'],
	    'restlessDuration': n['restlessDuration'],
	    'timeInBed': n['timeInBed'],
            'deep': n['deep'],
            'light': n['light'],
            'wake': n['wake'],
            'rem':n['rem'],
            'dateOfSleep': n['dateOfSleep'],
            'startTime': n['startTime'],
            'endTime': n['endTime'],
            'organization': 'NKUA'
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/fbsleep_fism', methods=['GET'])
@cross_origin()
def fbsleep_fism():
    # fbsleep = get_wellics_sleep.get_fbsleep(access_token)
    message = []
    for n in fism_sleep:
        newMessage = {
            'awakeCount': n['awakeCount'],
            'awakeDuration': n['awakeDuration'],
            'awakeningsCount': n['awakeningsCount'],
            'duration': n['duration'],
            'efficiency': n['efficiency'],
            'email': n['email'],
            'isMainSleep': int(n['mainSleep']),
            #'logId': n['logId'],
            'minutesAsleep': n['minutesAsleep'],
            'minutesAwake': n['minutesAwake'],
            'minutesAfterWakeup': n['minutesAfterWakeup'],
	    'minutesToFallAsleep':n['minutesToFallAsleep'],
	    'restlessCount': n['restlessCount'],
	    'restlessDuration': n['restlessDuration'],
	    'timeInBed': n['timeInBed'],
            'deep': n['deep'],
            'light': n['light'],
            'wake': n['wake'],
            'rem':n['rem'],
            'dateOfSleep': n['dateOfSleep'],
            'startTime': n['startTime'],
            'endTime': n['endTime'],
            'organization': 'FISM'
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/fbsleep_suub', methods=['GET'])
@cross_origin()
def fbsleep_suub():
    # fbsleep = get_wellics_sleep.get_fbsleep(access_token)
    message = []
    for n in suub_sleep:
        newMessage = {
            'awakeCount': n['awakeCount'],
            'awakeDuration': n['awakeDuration'],
            'awakeningsCount': n['awakeningsCount'],
            'duration': n['duration'],
            'efficiency': n['efficiency'],
            'email': n['email'],
            'isMainSleep': int(n['mainSleep']),
            'logId': n['logId'],
            'minutesAsleep': n['minutesAsleep'],
            'minutesAwake': n['minutesAwake'],
            'minutesAfterWakeup': n['minutesAfterWakeup'],
	    'minutesToFallAsleep':n['minutesToFallAsleep'],
	    'restlessCount': n['restlessCount'],
	    'restlessDuration': n['restlessDuration'],
	    'timeInBed': n['timeInBed'],
            'deep': n['deep'],
            'light': n['light'],
            'wake': n['wake'],
            'rem':n['rem'],
            'dateOfSleep': n['dateOfSleep'],
            'startTime': n['startTime'],
            'endTime': n['endTime'],
            'organization': 'SUUB'
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/fbsummary', methods=['GET'])
@cross_origin()
def fitbitsummary():
    #collection = mongo_fitbitSummary.fitbitsummary()
    #meaa = collection.find()
    meaa = get_wellics_daily.get_fbdaily(access_token)
    message = []
    for n in meaa:
        newMessage = {
            'calories_bmr': n["calories_bmr"],
            'calories_out': n['calories_out'],
            'elevation': n['elevation'],
            'fairly_active_minutes': n['fairly_active_minutes'],
            'floors': n['floors'],
            'lightly_active_minutes': n['lightly_active_minutes'],
            'marginal_calories': n['marginal_calories'],
            'sedentary_minutes': n['sedentary_minutes'],
            'steps': n['steps'],
            'very_active_minutes': n['very_active_minutes'],
            'timestamp_start': n['start_date'],
            'timestamp_end': n['end_date'],
            '_Employee_email': n['email']
            #empUUID']
            #'z_sedentaryActive': n['distances'][0]['distance'],
            #'z_lightlyActive': n['distances'][1]['distance'],
            #'z_loggedActivities': n['distances'][2]['distance'],
            #'z_veryActive': n['distances'][3]['distance'],
            #'z_tracker': n['distances'][4]['distance'],
            #'z_moderatelyActive': n['distances'][5]['distance'],
            #'z_total': n['distances'][6]['distance']
        }
        message.append(newMessage)

    return jsonify(message)
#############################################FB SUMMARY NKUA############################################################
@app.route('/fbsummary_nkua', methods=['GET'])
@cross_origin()
def fitbitsummary_nkua():
    message = []
    for n in nkua:
        newMessage = {
            'calories_bmr': n["calories_bmr"],
            'calories_out': n['calories_out'],
            'elevation': n['elevation'],
            'resting_heart_rate': n['resting_heart_rate'],
            'fairly_active_minutes': n['fairly_active_minutes'],
            'floors': n['floors'],
            'lightly_active_minutes': n['lightly_active_minutes'],
            'marginal_calories': n['marginal_calories'],
            'sedentary_minutes': n['sedentary_minutes'],
            'steps': n['steps'],
            'very_active_minutes': n['very_active_minutes'],
            'timestamp_start': n['start_date'],
            'timestamp_end': n['end_date'],
            '_Employee_email': n['email'],
            'organization': 'NKUA'
        }
        message.append(newMessage)

    return jsonify(message)
#def fitbitsummary_nkua():
#    #collection = mongo_fitbitSummary.fitbitsummary()
#    #meaa = collection.find()
#    meaa = get_wellics_daily.get_fbdaily(access_token)
#    message = []
#    for n in meaa:
#        result = patients_filter.patients_filter([n], patients_lists.list_nkua)
#        if (result == True):
#            newMessage = {
#                'calories_bmr': n["calories_bmr"],
#                'calories_out': n['calories_out'],
#                'elevation': n['elevation'],
#                'fairly_active_minutes': n['fairly_active_minutes'],
#                'floors': n['floors'],
#                'lightly_active_minutes': n['lightly_active_minutes'],
#                'marginal_calories': n['marginal_calories'],
#                'sedentary_minutes': n['sedentary_minutes'],
#                'steps': n['steps'],
#                'very_active_minutes': n['very_active_minutes'],
#                'timestamp_start': n['start_date'],
#                'timestamp_end': n['end_date'],
#                '_Employee_email': n['email'],
#                'organization': 'NKUA'
#                # empUUID']
#                # 'z_sedentaryActive': n['distances'][0]['distance'],
#                # 'z_lightlyActive': n['distances'][1]['distance'],
#                # 'z_loggedActivities': n['distances'][2]['distance'],
#                # 'z_veryActive': n['distances'][3]['distance'],
#                # 'z_tracker': n['distances'][4]['distance'],
#                # 'z_moderatelyActive': n['distances'][5]['distance'],
#                # 'z_total': n['distances'][6]['distance']
#            }
#            message.append(newMessage)
#
#    return jsonify(message)
#############################################FB SUMMARY FISM############################################################
@app.route('/fbsummary_fism', methods=['GET'])
@cross_origin()
def fitbitsummary_fism():
    message = []
    for n in fism:
        newMessage = {
            'calories_bmr': n["calories_bmr"],
            'calories_out': n['calories_out'],
            'resting_heart_rate': n['resting_heart_rate'],
            'elevation': n['elevation'],
            'fairly_active_minutes': n['fairly_active_minutes'],
            'floors': n['floors'],
            'lightly_active_minutes': n['lightly_active_minutes'],
            'marginal_calories': n['marginal_calories'],
            'sedentary_minutes': n['sedentary_minutes'],
            'steps': n['steps'],
            'very_active_minutes': n['very_active_minutes'],
            'timestamp_start': n['start_date'],
            'timestamp_end': n['end_date'],
            '_Employee_email': n['email'],
            'organization': 'FISM'
        }
        message.append(newMessage)

    return jsonify(message)
#def fitbitsummary_fism():
#    #collection = mongo_fitbitSummary.fitbitsummary()
#    #meaa = collection.find()
#    meaa = get_wellics_daily.get_fbdaily(access_token)
#    message = []
#    for n in meaa:
#        result = patients_filter.patients_filter([n], patients_lists.list_fism)
#        if (result == True):
#            newMessage = {
#                'calories_bmr': n["calories_bmr"],
#                'calories_out': n['calories_out'],
#                'elevation': n['elevation'],
#                'fairly_active_minutes': n['fairly_active_minutes'],
#                'floors': n['floors'],
#                'lightly_active_minutes': n['lightly_active_minutes'],
#                'marginal_calories': n['marginal_calories'],
#                'sedentary_minutes': n['sedentary_minutes'],
#                'steps': n['steps'],
#                'very_active_minutes': n['very_active_minutes'],
#                'timestamp_start': n['start_date'],
#                'timestamp_end': n['end_date'],
#                '_Employee_email': n['email'],
#                'organization': 'FISM'
#                # empUUID']
#                # 'z_sedentaryActive': n['distances'][0]['distance'],
#                # 'z_lightlyActive': n['distances'][1]['distance'],
#                # 'z_loggedActivities': n['distances'][2]['distance'],
#                # 'z_veryActive': n['distances'][3]['distance'],
#                # 'z_tracker': n['distances'][4]['distance'],
#                # 'z_moderatelyActive': n['distances'][5]['distance'],
#                # 'z_total': n['distances'][6]['distance']
#            }
#            message.append(newMessage)
#
#    return jsonify(message)
#############################################FB SUMMARY SUUB############################################################
@app.route('/fbsummary_suub', methods=['GET'])
@cross_origin()
def fitbitsummary_suub():
    message = []
    for n in suub:
        newMessage = {
            'calories_bmr': n["calories_bmr"],
            'calories_out': n['calories_out'],
            'elevation': n['elevation'],
            'fairly_active_minutes': n['fairly_active_minutes'],
            'floors': n['floors'],
            'resting_heart_rate': n['resting_heart_rate'],
            'lightly_active_minutes': n['lightly_active_minutes'],
            'marginal_calories': n['marginal_calories'],
            'sedentary_minutes': n['sedentary_minutes'],
            'steps': n['steps'],
            'very_active_minutes': n['very_active_minutes'],
            'timestamp_start': n['start_date'],
            'timestamp_end': n['end_date'],
            '_Employee_email': n['email'],
            'organization': 'SUUB'
        }
        message.append(newMessage)

    return jsonify(message)
#def fitbitsummary_suub():
#    #collection = mongo_fitbitSummary.fitbitsummary()
#    #meaa = collection.find()
#    meaa = get_wellics_daily.get_fbdaily(access_token)
#    message = []
#    for n in meaa:
#        result = patients_filter.patients_filter([n], patients_lists.list_suub)
#        if (result == True):
#            newMessage = {
#                'calories_bmr': n["calories_bmr"],
#                'calories_out': n['calories_out'],
#                'elevation': n['elevation'],
#                'fairly_active_minutes': n['fairly_active_minutes'],
#                'floors': n['floors'],
#                'lightly_active_minutes': n['lightly_active_minutes'],
#                'marginal_calories': n['marginal_calories'],
#                'sedentary_minutes': n['sedentary_minutes'],
#                'steps': n['steps'],
#                'very_active_minutes': n['very_active_minutes'],
#                'timestamp_start': n['start_date'],
#                'timestamp_end': n['end_date'],
#                '_Employee_email': n['email'],
#                'organization': 'SUUB'
#                # empUUID']
#                # 'z_sedentaryActive': n['distances'][0]['distance'],
#                # 'z_lightlyActive': n['distances'][1]['distance'],
#                # 'z_loggedActivities': n['distances'][2]['distance'],
#                # 'z_veryActive': n['distances'][3]['distance'],
#                # 'z_tracker': n['distances'][4]['distance'],
#                # 'z_moderatelyActive': n['distances'][5]['distance'],
#                # 'z_total': n['distances'][6]['distance']
#            }
#            message.append(newMessage)
#
#    return jsonify(message)
########################################################################################################################
@app.route('/fbheartimeline', methods=['GET'])
@cross_origin()
def fbheartimeline():
    collection = mongo_fitbitHeartTimeline.fitbitheartimeline()
    meaa = collection.find()
    message = []
    for n in meaa:
        newMessage = {
            '_PatientID': n['patient_uuid'],
            'resting_heart_rate': n['resting_heart_rate'],
            'period': n['period'],
            'timestamp': n['date_time'],
            'fat_burn_minutes': n['heart_rate_zones'][0]['minutes'],
            'cardio_minutes': n['heart_rate_zones'][1]['minutes'],
            'peak_minutes': n['heart_rate_zones'][2]['minutes'],
            'out_of_range_minutes': n['heart_rate_zones'][3]['minutes'],
            'fat_burn_max': n['heart_rate_zones'][0]['max'],
            'cardio_max': n['heart_rate_zones'][1]['max'],
            'peak_max': n['heart_rate_zones'][2]['max'],
            'out_of_range_max': n['heart_rate_zones'][3]['max'],
            'fat_burn_min': n['heart_rate_zones'][0]['min'],
            'cardio_min': n['heart_rate_zones'][1]['min'],
            'peak_min': n['heart_rate_zones'][2]['min'],
            'out_of_range_min': n['heart_rate_zones'][3]['min']
        }
        message.append(newMessage)

    return jsonify(message)
########################################################################################################################
@app.route('/iam', methods=['GET'])
@cross_origin()
def IAM():
    args = request.args
    username = args.get('username', type=str) # the order/userID received from the specific argument for the current selected user
    password = args.get('password', type=str)
    status_code = status(username,password)
    message = []
    if (status_code==200):
        #acc_token = access_token(username, password)
        ### (acc_token, refresh_token) = login(username, password)  ##=====> use one of the two functions included in IAM
        #profile = users_profiles(acc_token)  ##=====>
    # for n in range(len(profile)):###This happened since there is only one record to this specific request
        newMessage = { 'status':'success',
                       #'id': profile['id'],
                       'firstName': 'user', #profile['firstName'],
                       'lastName': 'user', #profile['lastName'],
                       #'email': profile['email'],
                       #'emailVerified':profile['emailVerified'],
                       'roles':'healthcare-service-provider-user' #profile['roles'][0],
                       #'groups':profile['groups'][0]
                      }
    elif (status_code!=200):
        newMessage = {'status': 'failed',
                      }
    message.append(newMessage)

    return jsonify(message)
########################################################################################################################
########################################################################################################################
@app.route('/alert', methods=['GET'])
@cross_origin()
def alert():
    alert=get_alert.get_alert(access_token)
    message = []
    for n in alert:
       newMessage = {
           '_PatientID': n['patientID'],
           'title': n['title'],
           'message': n['message'],
           'score': n['score'],
           'timestamp': n['dateTo']
       }
       message.append(newMessage)

    return jsonify(message)
#######################################################################################################################
#@app.route('/iamtest', methods=['GET'])
#@cross_origin()
#def IAMtest():
#    args = request.args
#    username = args.get('username', type=str) # the order/userID received from the specific argument for the current selected user
#    password = args.get('password', type=str)
#    status_code = status(username,password)
#    #acc_token = access_token(username, password)
#    message = []
#    newMessage = { 'status': username,
#                   'pas': password,
#                   'sc': status_code
#                   #'ac': acc_token
#                   }

#    message.append(newMessage)

#    return jsonify(message)
########################################################################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,ssl_context=("/etc/letsencrypt/live/kgservices.cn.ntua.gr/fullchain.pem", "/etc/letsencrypt/live/kgservices.cn.ntua.gr/privkey.pem"))
