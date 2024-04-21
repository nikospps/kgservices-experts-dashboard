from kafka import KafkaProducer
import json
from pymongo import MongoClient
import datetime
from mysql.connector import connect, Error
import mysql.connector as mysql
import json

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