from pymongo import MongoClient
import datetime

def ca():
    client = MongoClient('mongodb://admin:np220287npps@147.102.40.53:27017') # Accessing authorized mongodb for a specific user - Fresh Install 14/4/2020cd /u
    db = client['testdb']
    collection = db['ca'] #connect to specific collection(table)
    return collection
#
# collection = ca()
#
# a= {
#   "user_id": "stroke-user3",
#   "source": "Conversational Agent",
#   "observations": [
#     {
#       "sentiment_scores": [
#         {
#           "sentiment_class": "Positive",
#           "sentiment_score": 2.0
#         },
#         {
#           "sentiment_class": "Neutral",
#           "sentiment_score": 17.0
#         },
#         {
#           "sentiment_class": "Negative",
#           "sentiment_score": 81.0
#         }
#       ],
#       "timestamp": "2022-05-18T16:37:34Z",
#       "explanation": "I keep confusing the words I want to say",
#       "in_dashboard": "True"
#     }
#   ]
# }

#
# collection.insert_one(a)
#
# cursor = collection.find({})
# #
# for n in cursor:
#   print(n)#['awakeDuration'])