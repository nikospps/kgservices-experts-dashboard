from SPARQLWrapper import SPARQLWrapper, JSON, DIGEST, GET
from Person import Person
import urllib.parse as urlparse
# import Distances
########################################################################################################################
# import urlparse
# url = 'http://foo.appspot.com/abc?def=ghi'
# url = 'http://dockerengine.magneto.dcom.upv.es:8080/'
# parsed = urlparse.urlparse(url)
# print(urlparse.parse_qs(parsed.query))
# print(urlparse.parse_qs(parsed.query)['def'])
########################################################################################################################
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.options import Options
#
# # enable browser logging
# d = DesiredCapabilities.CHROME
# d['loggingPrefs'] = { 'browser':'ALL' }
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
# # driver = webdriver.Chrome(desired_capabilities=d)
#
# # # load the desired webpage
# driver.get('http://dockerengine.magneto.dcom.upv.es:8080/')
#
# # print messages
# for entry in driver.get_log('browser'):
#     print(entry)
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# # enable browser logging
# d = DesiredCapabilities.FIREFOX
# d['marionette'] = False
# d['loggingPrefs'] = {'browser': 'ALL'}
# driver = webdriver.Firefox(capabilities=d)
# # load some site
# driver.get('http://foo.com')
# # print messages
# for entry in driver.get_log('browser'):
#     print entry
#
# print
#
# driver.quit()
#
# def get_series_data(browser):
#     script = 'return JSON.stringify(res[0].PeformanceData)'
#     return Clean_String(str(browser.execute_script(script)))
########################################################################################################################
# import requests
# link = "http://dockerengine.magneto.dcom.upv.es:8080/js/app.b1caab18.js"
# r = requests.get(link)
# r.text   # unparsed json output, shouldn't be garbled
# r.json() # parses json and returns a dictionary
#
# data = requests.request("GET", link)
# url = data.url
########################################################################################################################
def asyn():
    # query_endpoint = 'http://147.102.7.169:3030/MAGNETO/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    # query_endpoint = 'http://147.102.7.119:3030/test/query'
    # 'http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1')
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/MAGNETO/query'
    query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_instd00fc52c-7bca-45f0-aed6-05b03e03c2b0/query'#Homicide in Munich
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst362eb2cc-22d8-49d2-a94c-da4b7c0bc030/query'
    # query_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/test/query'  # custom made dataset due to the umlauts problem

    sparql = SPARQLWrapper(query_endpoint)

    sparql.setCredentials("magneto", "M4gnetoDS1")  # username & password
    sparql.setMethod(GET)  # Set GET Method in order to make queries

    query = """
    prefix J.0: <http://www.magneto-h2020.eu#> 
    prefix owl:   <http://www.w3.org/2002/07/owl#>
    prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    prefix xsd:   <http://www.w3.org/2001/XMLSchema#> 
    prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> 

    SELECT ?ID ?Firstname ?Lastname
    WHERE {
      ?ID rdf:type J.0:Person.
    ?ID J.0:hasPersonFirstName ?Firstname.
    ?ID J.0:hasPersonSurname	?Lastname 
    }
    """

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results
############################################Require Till Here###########################################################
########################################################################################################################
# import json
#
# with open('magneto.json', 'w') as json_file:
#     json.dump(results,json_file)
# print(results)
########################################################################################################################
#######################################Attempt Before Trials for Demo of 3rd of July####################################
# def query_human(results):
#     for result in results["results"]["bindings"]:
#         id = str(result["ID"]["value"])
#         fname = str(result["Firstname"]["value"])
#         lname = str(result["Lastname"]["value"])
#         age = str(result["Age"]["value"])
#         bname = str(result["Birthname"]["value"])
#         nname = str(result["Nickname"]["value"])
#         midname = str(result["MiddleName"]["value"])
#         birth = str(result["Birthdate"]["value"])
#         country = str(result["Country"]["value"])
#         city = str(result["City"]["value"])
#         address = str(result["Address"]["value"])
#         addressnum = str(result["AddressNumber"]["value"])
#         height = str(result["Height"]["value"])
#         weight = str(result["Weight"]["value"])
#         isdead = str(result["isDead"]["value"])
#         isinterested = (str(result["InterestedIn"]["value"]))
#         nation = str(result["Nationality"]["value"])
#         gender = str(result["Gender"]["value"])
#
#         print("{} {}, {}, was born on {}, in {}".format(fname, lname, gender, birth, country))
#
#
# if __name__ == '__main__':
#     query_human()
# ob1, ob = str(result["object"]["value"]).split('#',1)

# print("Subject: {}, Predicate: {}, Object:{}".format(su,pr,ob))
# print(name)
# print(secName)

# Distances.calculate_person_similarity(personList[0],personList[2])

##***For Demo Purposes on 3rd of July***##
##########/////////Querying in order to retrieve just the attritubes that are already provided///////////###############
########################################################################################################################
def query_Demo(results):
    id = 0
    Plist = []
    for result in results["results"]["bindings"]:
        id1, ids = str(result["ID"]["value"]).split('#', 1)#here we make two sequential splits into the str's
        id2, id = ids.split('-', 1)
        # id = str(result["ID"]["value"])
        fname = str(result["Firstname"]["value"])
        lname = str(result["Lastname"]["value"])
        # id += 1
        Plist.append(Person(id,fname,lname))

        # print(fname, lname, id)
    return Plist

# personList = query_Demo(asyn())