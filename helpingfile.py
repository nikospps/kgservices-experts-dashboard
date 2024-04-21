
# Init Kafka Producer
def kafkaprod():
    bootstrap_servers = ['localhost:9092']
    # KAFKA_VERSION = (2, 7)
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)  # , api_version=KAFKA_VERSION)
    if producer:
        print('Connection Established')
    else:
        print('Connection Error')
    return producer

def kafkaprodsend(prod,msg,topicName = 'test'):
    ack = prod.send(topicName, msg)
    metadata = ack.get()
    if (metadata.topic):
        print(metadata.topic)
        print(metadata.partition)
        print('Kafka works properly')
    else:
        print('An error occured')

# Read MongoDB Function - latest record
def read_mongo(collection):
    for num in collection.find():
        # print(num)
        return num

# Read MongoDB Function - latest record
def read_mongo_all(collection):
    l = []
    for num in collection.find():
        l.append(num)
        # print(num)
        return l

# Write a specific dodument to MongoDB using Write Function
def write_mongo(jsondata,collection):
    collection.insert_one(jsondata)

# Write many doduments to MongoDB using Write Function: as bulkdata, a list of dictionaries will be used for bulk insert
def write_mongo(bulkdata):
    collection.insert_many(bulkdata)

# Init Mongo Connection
def init_mongo():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client.list_database_names()
    if db:
        print('Connection Established with Mongo')
    else:
        print('An error occured')
    return client

# List the available list of DB names in Mongo
def getMongoDBs():
    client = init_mongo()
    return (client.list_database_names())

# Initializae Connection with a specific Mongo DB
def connMongoDB(DB='testdb'):
    client = init_mongo()
    db = client[DB]
    if db:
        print(db.list_collection_names())
    else:
        print('Connection Issue')
    return db

# Connect to specific (available) collection topic
def collectionMongo(db,Collect='shifts'):
    collection = db[Collect] #connect to specific collection(table)
    return collection

# Connect to Default MySQL Database - Real Time Connection
def realtimeconnectionDef():
    # enter your server IP address/domain name
    HOST = "147.102.40.53"  # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = "MANTIS"
    # this is the user you create
    USER = "cnl"
    # user password
    PASSWORD = "Pa$$w0rd!"
    # port
    PORT = 9687
    # connect to MySQL server
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, port=PORT, user=USER, password=PASSWORD)
        print("Connected to:", db_connection.get_server_info())
    except Error as e:
        print(e)
    return db_connection

# Print the available DBs in Real Time DB/MySQL - Default DBs
def printDbsDef(db_connection):
    mycursor = db_connection.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

# Print the available Tables in Real Time DB/MySQL - Default Tables
def printtablesDef(db_connection):
    mycursor = db_connection.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

# Retrieve 'Real Time' Results for MySQL/Real Time DB, in dict/JSON format
def realtimeresults(db_connection):
    mycursor = db_connection.cursor()
    mycursor.execute("SELECT * FROM product")
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    results_json_data = []
    for result in myresult:
        results_json_data.append(dict(zip(row_headers, result)))
        # return json.dumps(results_json_data)
    return results_json_data

# Reconvert string to dict using dict
def stringtodict():
    # import json
    import yaml
    # s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
    h = "{'_id': ObjectId('6013e6c72d14cc7c09d2f8e5'), 'carplate': 'ZXX-9811', 'date_from': '2/10/2019', 'date_to': '3/10/2019', 'km_start': 182777, 'km_stop': 183511, 'passenger_ID': '2458', 'shift_name': 'P', 'time_from': '22:00', 'time_to': '06:00'}"
    # json_acceptable_string = h.replace("'", "\"")
    # d = json.loads(h)
    yaml.load(h)

# Send Real Time Data Through Kafka for Analysis Purposes
def realtimekafka(results_json_data,producer):
    for i in results_json_data:
        msg = str.encode(str(i))
        if kafkaprodsend(producer, msg):
            print('Message Send')
        # else:
        #     print('An Error Occured')
    # print(len(i))


# # 'mysql+pymysql://cnl:Pa$$w0rd!@147.102.40.53:9687/MANTIS'
# try:
#     with connect(
#         host="147.102.40.53",
#         port = "9687",
#         user="cnl",
#         password="Pa$$w0rd!",
#     ) as connection:
#         print(connection)
# print(collection)
# col1 = collection.find()[11]['carPlate']
# print(collection.find()[10]['carPlate'])#return car plate for first element = PPS-8001
# print(collection.find()[0]['carplate'])#just by reading the first element of the newly created mongo for mantis project (14/4/2020)
########Its the read_mongo function
# cursor = collection.find({})
#
# def tes():
#     for document in cursor:
#         if document['carplate'] != 'NO-PLATE':
#           return(document)
#         else:
#             print('empty')
#
# for n in cursor:
#     print(n)
#
# # tes()
#
# t = collection.find({"carPlate": "ZXX-9811", "timeStamp": "03072020_125254"})
#
# kafkaprodsend(producer,msg=str.encode(t))
#
# for i in t:
#     if "03072020" in t['timeStamp']:
#         print(i)
#
# import pandas as pd
# import time
# df = pd.DataFrame(list(t))
# df['id']
#
# def export_data():
#     name = get_data()
#     df2 = pd.DataFrame.from_records(name)
#     t = time.localtime()
#     timestamp = time.strftime('%b-%d-%Y_%H%M', t)
#     # BACKUP_NAME = ("Rest_" + timestamp)#SOS
#     # df2.to_csv(BACKUP_NAME+'.csv')#SOS
#     mantis_backup = ("MantisBackUp_" + timestamp)
#     df2.to_csv(mantis_backup + '.csv')
#
#
# myquery = { "id": 1 }
#
# res = collection.find(myquery)
#
# # len(cursor)
#
# test = read_mongo()
#
# collection.find()[0]['carPlate']
#
# # Create query(-ies) in order to insert one and many data elements into the collection
# post_query = {"name":"nikos",
#         "age":32,
#         "Job":"ICCS"}
#
# post_query = {"name":"teo",
#         "age":30,
#         "Job":"ICCS"}
#
# post_query = {
#     "SpeedObd": 0,
#     "accuracy": 51.029,
#     "altitude": 63,
#     "bearing": 0,
#     "engineRunTime": 0,
#     "engineTemp": 32,
#     "fuelLevel": 0,
#     "fuelType": 0,
#     "intakeTemp": 0,
#     "lat": 38.1861,
#     "lon": 21.7,
#     "pendingTrouble": "False",
#     "relThrottle": 0,
#     "rpm": 3293,
#     "speedGps": 0,
#     "timeStamp": "29102019_153725",
#     "vinNumber": 2,
#     "carPlate": "IHZ-3302"
#   }
#
# collection.insert_one(post_query)
#
# # Delete a specific document from a mongo db using a Specific query
# myQuery = {'passenger_ID': '1358'}
# myQuery = {'author': 'Mike'}
# myQuery = {'pendingTrouble': 'False-Trying'}
#
# collection.delete_one(myQuery)
#
# # Delete all documents from a specific collection
# collection.delete_many({})
#
# # Execute functions
# read_mongo()
# ########################################################################################################################
# import json
# from collections import OrderedDict
#
# id = '203'
#
# with open('data,json') as data_file:
#     data = json.load(data_file, object_pairs_hook=OrderedDict)
#     for key, value in data.items():
#         print(key)
#         id_value = value['payload']['price']
#         if id in id_value: # check first if id is present
#             pack = id_value[id]
#             print(pack) #pack should be returning the value of the key '203'
# ########################################################################################################################
# ########################################################################################################################
# ###########################################Find the Total Shift of the Driver###########################################
# from datetime import datetime
#
# date = {
#   "car_template": "ZXX9811",
#   "date": "1/10/2019",
#   "klm_start": 182767,
#   "kml_stop": 183007,
#   "passenger_ID": 1358,
#   "shift_name": "A",
#   "time_from":"14.00",
#   "time_to":"22.00"
# }
#
# a = date['time_from']
# b = date['time_to']
# time1 = datetime.strptime(a,"%H.%M") # convert string to time
# time2 = datetime.strptime(b,"%H.%M")
# diff = time2 -time1
# total_time = diff.total_seconds()/3600    # seconds to hour
#
# # type(diff.total_seconds()/3600)
#
#
# date = {
#     "carplate": "ZXX9811",
#     "date": "2/10/2019",
#     "km_start": 182777,
#     "km_stop": 183511,
#     "passenger_ID": "2458",
#     "shift_name": "\u03a0",
#     "time_from": "06:00",
#     "time_to": "14:00"
#   }
#
# import regex as re
# greek=date['shift_name']
# unicodedata.decomposition(precomposed)