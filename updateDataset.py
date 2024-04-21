import requests

def generategraph():
    # Script Responsible for saving locally an already stored, in fuseki, dataset, into a specific format (owl,ttl,n3)
    # Read a remote semantic (fuseki) file with credentials
    response = requests.get('http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/query',
                            auth=('magneto', 'M4gnetoDS1'))
    response = requests.get('http://10.5.0.204:3030/magneto_inst/data', auth=('magneto', 'M4gnetoDS1'))
    # response = requests.get('http://10.5.0.204:3030/test/data', auth=('magneto','M4gnetoDS1'))
    # response = requests.get('http://10.5.0.204:3030/magneto_model/data', auth=('magneto','M4gnetoDS1'))
    # response = requests.get('http://147.102.7.169:3030/MAGNETO/data')
    # response = requests.get('http://10.5.0.204:3030/magneto/data', auth=('magneto','M4gnetoDS1'))

    response.text

    f = open('/usr/local/etc/res/Datasets/Victims.ttl', 'w')
    f.write(response.text)
    f.close()