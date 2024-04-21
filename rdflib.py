import rdflib
import pprint
import os

ttl = os.open("/usr/local/etc/Datasets/Victims.ttl" | os.O_RDWR|os.O_CREAT)

g = rdflib.Graph()
result = g.parse('http://147.102.7.138:3030/magneto',format='n3')
print(len(g))

rdflib.util.guess_format()

# Add triples using store's add method
s = g.serialize(format='n3')

print(s)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))

#g.load('http://147.102.7.180:3030/ds1/data',format='n3')