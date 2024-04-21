from SPARQLWrapper import SPARQLWrapper, JSON
import requests

# update_endpoint = 'http://147.102.7.185:3030/ds/update'
# update_endpoint = 'http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/update'
update_endpoint = 'http://147.102.7.169:3030/testaki1/update'

##In the same way we use the appropriate command to execute an UPDATE instead of an INSERT command such as we do below

updateString = "PREFIX magnetomodel: <http://www.magneto-h2020.eu#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> INSERT DATA {magnetomodel:FusedPerson451 magnetomodel:hasPersonFirstName 'Antras1/Gay1' . magnetomodel:FusedPerson45 magnetomodel:hasPersonSurname 'Thodoroula/Thodoras' . magnetomodel:FusedPerson451 magnetomodel:hasServiceUserID '1/2' . magnetomodel:FusedPerson451 rdf:type magnetomodel:doulakosGeorge .}"

sparql = SPARQLWrapper(update_endpoint)

sparql.setQuery(updateString)
sparql.method = 'POST'
sparql.query()
########################################################################################################################
# Read a remote semantic (fuseki) file with credentials
response = requests.get('http://147.102.7.169:5545/fusedPersons') #, auth=('magneto','M4gnetoDS1'))

# Extracting Data in JSON format
dataL = response.json() #response.text

def ins(num):
    for i in range(len(dataL)):
        if(dataL[i]['TableId']==str(num)):
            print(dataL[i])

ins(1)
########################################################################################################################
f = open('thodoroula.owl','w')
f.write(response.text)

########################################################################################################################

