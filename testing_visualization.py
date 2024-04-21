from flask import Flask, jsonify, render_template
import PersonsList
import kNNCalculation
# import sparqltest
import webbrowser
import os
# import reasoning_sub
from flask_cors import CORS, cross_origin

import subprocess

result = subprocess.Popen(['python', '-m', 'webbrowser', '-n', 'https://www.gazetta.gr'])

os.system("python -m webbrowser -n 'https://www.gazzetta.gr/'")

def execreas():
    process = subprocess.Popen(['java', '-jar', '/home/nikospps/Desktop/Jena_reasoner.jar'], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    result = stdout.decode("utf-8")
    finalres = [substring for substring in result.split('\n') if substring!='']
    return finalres


# os.system("start http://vowl.visualdataweb.org/webvowl.html")

url = 'file:///home/nikospps/Desktop/index.html'
# url1 = 'http://vowl.visualdataweb.org/webvowl.html'
# new=2
# webbrowser.open(url=url,new=1,autoraise=True)
def open():
    webbrowser.open('/home/nikospps/Desktop/index.html')
    return('ok')
if __name__ == '__main__':
    subprocess.Popen(['python', '-m', 'webbrowser', '-n', 'https://www.gazetta.gr'])
#
# app = Flask(__name__)
# CORS(app) #important feature in order for being enabled with vue
#
# @app.route('/')
# @cross_origin()
# def index():
#     return "Hello, Person Fusion API!"
#
# @app.route('/web')
# @cross_origin()
# def index1():
#     return render_template('/home/nikospps/Desktop/index.html')
#
#
# ########################################################################################################################
# # @app.route('/comparePersons', methods=['GET'])
# # @cross_origin()
# # def compare_persons():
# #     # personList = []
# #     id = 0
# #     personList = sparqltest.query()
# #     similar_objects = kNNCalculation.calculate_nearest_neighbors(personList)
#
# ########################################################################################################################
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5546, debug=True)
