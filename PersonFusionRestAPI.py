# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:06:14 2019

@author: nikospps
"""

from flask import Flask, jsonify
import PersonsList
import kNNCalculation
import sparqltest

# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# https://stackoverflow.com/questions/6541767/python-urllib-error-attributeerror-bytes-object-has-no-attribute-read

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Person Fusion API!"

@app.route('/comparePersons')#, methods=['GET'])
def compare_persons():

    #data = request.get_data().decode('utf-8')
    #print(data)
    #data_json = json.loads(request.get_data().decode('utf-8'))
    
    #persons = PersonsList.get_persons()
    persons = sparqltest.query()
    similarities = kNNCalculation.calculate_nearest_neighbors(persons)
    
    message = list()
    for i in range(len(similarities)):
         newMessage = {
            'id': 'Myid',
            'Person1_ID': 'XX', 
            'Person1_Name': str(similarities[i][0].firstname), 
            'Person1_Surname': str(similarities[i][0].surname), 
            'Person2_ID': 'XX',
            'Person2_Name': str(similarities[i][1].firstname),
            'Person2_Surname': str(similarities[i][1].surname), 
            'Confidence': str(similarities[i][2]) 
            }
         message.append(newMessage)
  
    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5545, debug=True)