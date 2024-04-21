from flask import  Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['MONGO_DBNAME'] = 'testdb'
#app.config['MONGO_URI'] = 'mongodb://147.102.40.53:19870/testdb'
#app.config['MONGO_URI'] = 'mongodb://147.102.40.53:27017/testdb'
#app.config['MONGO_URI'] = 'mongodb://username:password@host:port/db_name'
app.config['MONGO_URI'] = 'mongodb://admin:np220287npps@147.102.40.53:27017/testdb?authSource=admin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cnl:Pa$$w0rd!@147.102.40.53:9687/MANTIS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db's
db = SQLAlchemy(app)
mongo = PyMongo(app)
ma = Marshmallow(app)
########################################################################################################################
########################################################################################################################
@app.route('/')
def index():
    return 'Welcome to ICCS Laboratory!'
    #return render_template('index.html')
########################################################################################################################
@app.route('/events', methods=['GET'])
def get_all_events():
    framework = mongo.db.commmon

    output = []

    for q in framework.find():
        output.append({"scoring": {
        "benign_scoring": q["scoring"]["benign_scoring"],
        "malicious_scoring": q["scoring"]["malicious_scoring"]
    },
    "pending_3ds": q["pending_3ds"],
    "user_found": q["user_found"],
    "merchant_check": {
        "known": q["merchant_check"]["known"],
        "new": q["merchant_check"]["new"],
        "usual": q["merchant_check"]["usual"],
        "blank": q["merchant_check"]["blank"]
    },
    "merchant_type_check": {
        "known": q["merchant_type_check"]["known"],
        "new": q["merchant_type_check"]["new"],
        "usual": q["merchant_type_check"]["usual"],
        "blank": q["merchant_type_check"]["blank"]
    },
    "merchant_country_check": {
        "known": q["merchant_country_check"]["known"],
        "new": q["merchant_country_check"]["new"],
        "usual": q["merchant_country_check"]["usual"],
        "blank": q["merchant_country_check"]["blank"],
        "transaction_periods": {
            "timezone_22_1": q["merchant_country_check"]["transaction_periods"]["timezone_22_1"],
            "timezone_2_5": q["merchant_country_check"]["transaction_periods"]["timezone_2_5"],
            "timezone_6_9": q["merchant_country_check"]["transaction_periods"]["timezone_6_9"],
            "timezone_10_13": q["merchant_country_check"]["transaction_periods"]["timezone_10_13"],
            "timezone_14_15": q["merchant_country_check"]["transaction_periods"]["timezone_14_15"],
            "timezone_16_19": q["merchant_country_check"]["transaction_periods"]["timezone_16_19"],
            "timezone_20_21": q["merchant_country_check"]["transaction_periods"]["timezone_20_21"]
        }
    },
    "geo_ip": {
        "ip": q["geo_ip"]["ip"],
        "city": q["geo_ip"]["city"],
        "country": q["geo_ip"]["country"],
        "iso": q["geo_ip"]["iso"],
        "time_zone": q["geo_ip"]["time_zone"],
        "continent": q["geo_ip"]["continent"],
        "latitude": q["geo_ip"]["latitude"],
        "longitude": q["geo_ip"]["longitude"],
        "accuracy_radius": q["geo_ip"]["accuracy_radius"],
        "asn": q["geo_ip"]["asn"],
        "asn_organisation": q["geo_ip"]["asn_organisation"],
        "connection_type": q["geo_ip"]["connection_type"],
        "postal_code": q["geo_ip"]["postal_code"],
        "is_anonymous_proxy": q["geo_ip"]["is_anonymous_proxy"],
        "is_satellite_provider": q["geo_ip"]["is_satellite_provider"]
    },
    "customerid": {
        "nif": q["customerid"]["nif"],
        "sau": q["customerid"]["sau"],
        "nummid": q["customerid"]["nummid"],
        "usuclo": q["customerid"]["usuclo"],
        "e": q["customerid"]["e"],
        "carpeta": q["customerid"]["carpeta"]
    },
    "merchanInfo": {
        "merchantType": q["merchanInfo"]["merchantType"],
        "merchantCountryCode": q["merchanInfo"]["merchantCountryCode"],
        "merchantName": q["merchanInfo"]["merchantName"],
        "merchantRiskIndicator": q["merchanInfo"]["merchantRiskIndicator"]
    },
    "browserInfo": {
        "browserLanguage": q["browserInfo"]["browserLanguage"],
        "browserIp": q["browserInfo"]["browserIp"],
        "browserUseragent": q["browserInfo"]["browserUseragent"]
    },
    "traRiskIndicator": q["traRiskIndicator"],
    "purchaseInfo": {
        "purchaseAmount": q["purchaseInfo"]["purchaseAmount"],
        "purchaseCurrency": q["purchaseInfo"]["purchaseCurrency"],
        "cumulativeAmount": q["purchaseInfo"]["cumulativeAmount"]
    },
    "operation": {
        "pan": q["operation"]["pan"],
        "cardHolderName": q["operation"]["cardHolderName"],
        "cardHolderEmails": q["operation"]["cardHolderEmails"],
        "homePhone": q["operation"]["homePhone"],
        "mobilePhone": q["operation"]["mobilePhone"],
        "billAddress": q["operation"]["billAddress"],
        "billAddrCity": q["operation"]["billAddrCity"],
        "billAddrPostcode": q["operation"]["billAddrPostcode"],
        "billAddrCountry": q["operation"]["billAddrCountry"],
        "shipAddress": q["operation"]["shipAddress"],
        "shipAddrCity": q["operation"]["shipAddrCity"],
        "shipAddrPostCode": q["operation"]["shipAddrPostCode"],
        "shipAddrCountry": q["operation"]["shipAddrCountry"]
    },
    "panInfo": {
        "id": q["panInfo"]["id"],
        "contrato": q["panInfo"]["contrato"],
        "plastico": q["panInfo"]["plastico"],
        "enterprise": q["panInfo"]["enterprise"],
        "cardType": q["panInfo"]["cardType"],
        "createDate": q["panInfo"]["createDate"],
        "limitCard": q["panInfo"]["limitCard"],
        "affinity": q["panInfo"]["affinity"],
        "bin": q["panInfo"]["bin"]
    },
    "aliases": {
        "address": q["aliases"]["address"],
        "city": q["aliases"]["city"],
        "postcode": q["aliases"]["postcode"],
        "country": q["aliases"]["country"],
        "numMobile": q["aliases"]["numMobile"],
        "email": q["aliases"]["email"],
        "auth": q["aliases"]["auth"]
    }
})

    return jsonify(output)
########################################################################################################################
@app.route('/events', methods=['POST'])
def add_events():
    framework = mongo.db.commmon

    json = request.get_json(force=True)


    benign_scoring =  json["scoring"]["benign_scoring"],
    malicious_scoring = json["scoring"]["malicious_scoring"]
    pending_3ds = json["pending_3ds"]
    user_found= json["user_found"]
    known1= json["merchant_check"]["known"]
    new1= json["merchant_check"]["new"]
    usual1 = json["merchant_check"]["usual"]
    blank1= json["merchant_check"]["blank"]
    known2= json["merchant_type_check"]["known"]
    new2= json["merchant_type_check"]["new"]
    usual2= json["merchant_type_check"]["usual"]
    blank2= json["merchant_type_check"]["blank"]
    known3= json["merchant_country_check"]["known"]
    new3= json["merchant_country_check"]["new"]
    usual3= json["merchant_country_check"]["usual"]
    blank3= json["merchant_country_check"]["blank"]
    timezone_22_1= json["merchant_country_check"]["transaction_periods"]["timezone_22_1"]
    timezone_2_5= json["merchant_country_check"]["transaction_periods"]["timezone_2_5"]
    timezone_6_9= json["merchant_country_check"]["transaction_periods"]["timezone_6_9"]
    timezone_10_13= json["merchant_country_check"]["transaction_periods"]["timezone_10_13"]
    timezone_14_15= json["merchant_country_check"]["transaction_periods"]["timezone_14_15"]
    timezone_16_19= json["merchant_country_check"]["transaction_periods"]["timezone_16_19"]
    timezone_20_21= json["merchant_country_check"]["transaction_periods"]["timezone_20_21"]
    ip= json["geo_ip"]["ip"]
    city= json["geo_ip"]["city"]
    country= json["geo_ip"]["country"]
    iso= json["geo_ip"]["iso"]
    time_zone= json["geo_ip"]["time_zone"]
    continent= json["geo_ip"]["continent"]
    latitude= json["geo_ip"]["latitude"]
    longitude= json["geo_ip"]["longitude"]
    accuracy_radius= json["geo_ip"]["accuracy_radius"]
    asn= json["geo_ip"]["asn"]
    asn_organisation= json["geo_ip"]["asn_organisation"]
    connection_type= json["geo_ip"]["connection_type"]
    postal_code= json["geo_ip"]["postal_code"]
    is_anonymous_proxy= json["geo_ip"]["is_anonymous_proxy"]
    is_satellite_provider= json["geo_ip"]["is_satellite_provider"]
    nif= json["customerid"]["nif"]
    sau= json["customerid"]["sau"]
    nummid= json["customerid"]["nummid"]
    usuclo= json["customerid"]["usuclo"]
    e= json["customerid"]["e"]
    carpeta= json["customerid"]["carpeta"]
    merchantType= json["merchanInfo"]["merchantType"]
    merchantCountryCode= json["merchanInfo"]["merchantCountryCode"]
    merchantName= json["merchanInfo"]["merchantName"]
    merchantRiskIndicator= json["merchanInfo"]["merchantRiskIndicator"]
    browserLanguage= json["browserInfo"]["browserLanguage"]
    browserIp= json["browserInfo"]["browserIp"]
    browserUseragent= json["browserInfo"]["browserUseragent"]
    traRiskIndicator= json["traRiskIndicator"]
    purchaseAmount= json["purchaseInfo"]["purchaseAmount"]
    purchaseCurrency= json["purchaseInfo"]["purchaseCurrency"]
    cumulativeAmount= json["purchaseInfo"]["cumulativeAmount"]
    pan= json["operation"]["pan"]
    cardHolderName=json["operation"]["cardHolderName"]
    cardHolderEmails= json["operation"]["cardHolderEmails"]
    homePhone=json["operation"]["homePhone"]
    mobilePhone=json["operation"]["mobilePhone"]
    billAddress=json["operation"]["billAddress"]
    billAddrCity= json["operation"]["billAddrCity"]
    billAddrPostcode= json["operation"]["billAddrPostcode"]
    billAddrCountry= json["operation"]["billAddrCountry"]
    shipAddress= json["operation"]["shipAddress"]
    shipAddrCity= json["operation"]["shipAddrCity"]
    shipAddrPostCode= q["operation"]["shipAddrPostCode"]
    shipAddrCountry= json["operation"]["shipAddrCountry"]
    id=json["panInfo"]["id"]
    contrato=json["panInfo"]["contrato"]
    plastico= json["panInfo"]["plastico"]
    enterprise= json["panInfo"]["enterprise"]
    cardType= json["panInfo"]["cardType"]
    createDate= json["panInfo"]["createDate"]
    limitCard= json["panInfo"]["limitCard"]
    affinity= json["panInfo"]["affinity"]
    bin= json["panInfo"]["bin"]
    address=json["aliases"]["address"]
    city= json["aliases"]["city"]
    postcode= json["aliases"]["postcode"]
    country= json["aliases"]["country"]
    numMobile= json["aliases"]["numMobile"]
    email= json["aliases"]["email"]
    auth=json["aliases"]["auth"]

    framework_id = framework.insert({"scoring": {
        "benign_scoring": benign_scoring,
        "malicious_scoring": malicious_scoring
    },
    "pending_3ds": pending_3ds,
    "user_found": user_found,
    "merchant_check": {
        "known": known1,
        "new": new1,
        "usual": usual1,
        "blank": blank1
    },
    "merchant_type_check": {
        "known": known2,
        "new": new2,
        "usual": usual2,
        "blank": blank2
    },
    "merchant_country_check": {
        "known": known3,
        "new": new3,
        "usual": usual3,
        "blank": blank3,
        "transaction_periods": {
            "timezone_22_1": timezone_22_1,
            "timezone_2_5": timezone_2_5,
            "timezone_6_9": timezone_6_9,
            "timezone_10_13": timezone_10_13,
            "timezone_14_15": timezone_14_15,
            "timezone_16_19": timezone_16_19,
            "timezone_20_21": timezone_20_21
        }
    },
    "geo_ip": {
        "ip": ip,
        "city": city,
        "country": country,
        "iso": iso,
        "time_zone": time_zone,
        "continent": continent,
        "latitude": latitude,
        "longitude": longitude,
        "accuracy_radius": accuracy_radius,
        "asn": asn,
        "asn_organisation": asn_organisation,
        "connection_type": connection_type,
        "postal_code": postal_code,
        "is_anonymous_proxy": is_anonymous_proxy,
        "is_satellite_provider": is_satellite_provider
    },
    "customerid": {
        "nif": q["customerid"]["nif"],
        "sau": q["customerid"]["sau"],
        "nummid": q["customerid"]["nummid"],
        "usuclo": q["customerid"]["usuclo"],
        "e": q["customerid"]["e"],
        "carpeta": q["customerid"]["carpeta"]
    },
    "merchanInfo": {
        "merchantType": q["merchanInfo"]["merchantType"],
        "merchantCountryCode": q["merchanInfo"]["merchantCountryCode"],
        "merchantName": q["merchanInfo"]["merchantName"],
        "merchantRiskIndicator": q["merchanInfo"]["merchantRiskIndicator"]
    },
    "browserInfo": {
        "browserLanguage": q["browserInfo"]["browserLanguage"],
        "browserIp": q["browserInfo"]["browserIp"],
        "browserUseragent": q["browserInfo"]["browserUseragent"]
    },
    "traRiskIndicator": q["traRiskIndicator"],
    "purchaseInfo": {
        "purchaseAmount": q["purchaseInfo"]["purchaseAmount"],
        "purchaseCurrency": q["purchaseInfo"]["purchaseCurrency"],
        "cumulativeAmount": q["purchaseInfo"]["cumulativeAmount"]
    },
    "operation": {
        "pan": q["operation"]["pan"],
        "cardHolderName": q["operation"]["cardHolderName"],
        "cardHolderEmails": q["operation"]["cardHolderEmails"],
        "homePhone": q["operation"]["homePhone"],
        "mobilePhone": q["operation"]["mobilePhone"],
        "billAddress": q["operation"]["billAddress"],
        "billAddrCity": q["operation"]["billAddrCity"],
        "billAddrPostcode": q["operation"]["billAddrPostcode"],
        "billAddrCountry": q["operation"]["billAddrCountry"],
        "shipAddress": q["operation"]["shipAddress"],
        "shipAddrCity": q["operation"]["shipAddrCity"],
        "shipAddrPostCode": q["operation"]["shipAddrPostCode"],
        "shipAddrCountry": q["operation"]["shipAddrCountry"]
    },
    "panInfo": {
        "id": q["panInfo"]["id"],
        "contrato": q["panInfo"]["contrato"],
        "plastico": q["panInfo"]["plastico"],
        "enterprise": q["panInfo"]["enterprise"],
        "cardType": q["panInfo"]["cardType"],
        "createDate": q["panInfo"]["createDate"],
        "limitCard": q["panInfo"]["limitCard"],
        "affinity": q["panInfo"]["affinity"],
        "bin": q["panInfo"]["bin"]
    },
    "aliases": {
        "address": q["aliases"]["address"],
        "city": q["aliases"]["city"],
        "postcode": q["aliases"]["postcode"],
        "country": q["aliases"]["country"],
        "numMobile": q["aliases"]["numMobile"],
        "email": q["aliases"]["email"],
        "auth": q["aliases"]["auth"]
    }
})

    q = framework.find_one({'_id': framework_id})

    output = {"scoring": {
        "benign_scoring": q["scoring"]["benign_scoring"],
        "malicious_scoring": q["scoring"]["malicious_scoring"]
    },
    "pending_3ds": q["pending_3ds"],
    "user_found": q["user_found"],
    "merchant_check": {
        "known": q["merchant_check"]["known"],
        "new": q["merchant_check"]["new"],
        "usual": q["merchant_check"]["usual"],
        "blank": q["merchant_check"]["blank"]
    },
    "merchant_type_check": {
        "known": q["merchant_type_check"]["known"],
        "new": q["merchant_type_check"]["new"],
        "usual": q["merchant_type_check"]["usual"],
        "blank": q["merchant_type_check"]["blank"]
    },
    "merchant_country_check": {
        "known": q["merchant_country_check"]["known"],
        "new": q["merchant_country_check"]["new"],
        "usual": q["merchant_country_check"]["usual"],
        "blank": q["merchant_country_check"]["blank"],
        "transaction_periods": {
            "timezone_22_1": q["merchant_country_check"]["transaction_periods"]["timezone_22_1"],
            "timezone_2_5": q["merchant_country_check"]["transaction_periods"]["timezone_2_5"],
            "timezone_6_9": q["merchant_country_check"]["transaction_periods"]["timezone_6_9"],
            "timezone_10_13": q["merchant_country_check"]["transaction_periods"]["timezone_10_13"],
            "timezone_14_15": q["merchant_country_check"]["transaction_periods"]["timezone_14_15"],
            "timezone_16_19": q["merchant_country_check"]["transaction_periods"]["timezone_16_19"],
            "timezone_20_21": q["merchant_country_check"]["transaction_periods"]["timezone_20_21"]
        }
    },
    "geo_ip": {
        "ip": q["geo_ip"]["ip"],
        "city": q["geo_ip"]["city"],
        "country": q["geo_ip"]["country"],
        "iso": q["geo_ip"]["iso"],
        "time_zone": q["geo_ip"]["time_zone"],
        "continent": q["geo_ip"]["continent"],
        "latitude": q["geo_ip"]["latitude"],
        "longitude": q["geo_ip"]["longitude"],
        "accuracy_radius": q["geo_ip"]["accuracy_radius"],
        "asn": q["geo_ip"]["asn"],
        "asn_organisation": q["geo_ip"]["asn_organisation"],
        "connection_type": q["geo_ip"]["connection_type"],
        "postal_code": q["geo_ip"]["postal_code"],
        "is_anonymous_proxy": q["geo_ip"]["is_anonymous_proxy"],
        "is_satellite_provider": q["geo_ip"]["is_satellite_provider"]
    },
    "customerid": {
        "nif": q["customerid"]["nif"],
        "sau": q["customerid"]["sau"],
        "nummid": q["customerid"]["nummid"],
        "usuclo": q["customerid"]["usuclo"],
        "e": q["customerid"]["e"],
        "carpeta": q["customerid"]["carpeta"]
    },
    "merchanInfo": {
        "merchantType": q["merchanInfo"]["merchantType"],
        "merchantCountryCode": q["merchanInfo"]["merchantCountryCode"],
        "merchantName": q["merchanInfo"]["merchantName"],
        "merchantRiskIndicator": q["merchanInfo"]["merchantRiskIndicator"]
    },
    "browserInfo": {
        "browserLanguage": q["browserInfo"]["browserLanguage"],
        "browserIp": q["browserInfo"]["browserIp"],
        "browserUseragent": q["browserInfo"]["browserUseragent"]
    },
    "traRiskIndicator": q["traRiskIndicator"],
    "purchaseInfo": {
        "purchaseAmount": q["purchaseInfo"]["purchaseAmount"],
        "purchaseCurrency": q["purchaseInfo"]["purchaseCurrency"],
        "cumulativeAmount": q["purchaseInfo"]["cumulativeAmount"]
    },
    "operation": {
        "pan": q["operation"]["pan"],
        "cardHolderName": q["operation"]["cardHolderName"],
        "cardHolderEmails": q["operation"]["cardHolderEmails"],
        "homePhone": q["operation"]["homePhone"],
        "mobilePhone": q["operation"]["mobilePhone"],
        "billAddress": q["operation"]["billAddress"],
        "billAddrCity": q["operation"]["billAddrCity"],
        "billAddrPostcode": q["operation"]["billAddrPostcode"],
        "billAddrCountry": q["operation"]["billAddrCountry"],
        "shipAddress": q["operation"]["shipAddress"],
        "shipAddrCity": q["operation"]["shipAddrCity"],
        "shipAddrPostCode": q["operation"]["shipAddrPostCode"],
        "shipAddrCountry": q["operation"]["shipAddrCountry"]
    },
    "panInfo": {
        "id": q["panInfo"]["id"],
        "contrato": q["panInfo"]["contrato"],
        "plastico": q["panInfo"]["plastico"],
        "enterprise": q["panInfo"]["enterprise"],
        "cardType": q["panInfo"]["cardType"],
        "createDate": q["panInfo"]["createDate"],
        "limitCard": q["panInfo"]["limitCard"],
        "affinity": q["panInfo"]["affinity"],
        "bin": q["panInfo"]["bin"]
    },
    "aliases": {
        "address": q["aliases"]["address"],
        "city": q["aliases"]["city"],
        "postcode": q["aliases"]["postcode"],
        "country": q["aliases"]["country"],
        "numMobile": q["aliases"]["numMobile"],
        "email": q["aliases"]["email"],
        "auth": q["aliases"]["auth"]
    }
}

    return jsonify({'check':output})
########################################################################################################################
########################################################################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
