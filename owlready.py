from owlready2 import *
from owlready2.pymedtermino2.umls import *

## Creating an ontology
#onto = get_ontology("http://test.org/onto.owl")

## Load an existing ontology from a local copy=>the IRI local filename prefixed with file://

#onto = get_ontology("file:///home/nikospps/goslim_aspergillus.owl").load()

# If an URL is given, Owlready2 first searches for a local copy of the OWL file and, if not found,
# tries to download it from the Internet

#onto_path.append("/path/to/owlready/onto/")
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load()
onto = get_ontology("http://test.org/onto.owl")

## Accessing the content of an ontology
#print(onto.Pizza)
#print(onto["Pizza"])

print(list(onto.classes()))

# The IRIS pseudo-dictionary can be used for accessing an entity from its full IRI
IRIS["http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl#Pizza"]

# SImple Quiries Performance
onto.search(iri="*Topping")
onto.search(has_topping = "*")
onto.search_one(is_a = onto.Pizza)

# Metadata
print(onto.metadata)

# Saving in specific formats
onto.save(file="testing", format="rdfxml")

from owlready2 import *
import types

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
    namespace = onto

#subclasses can be created by inheriting an (already existing) ontology class
class DrugAssociation(Drug):
    pass

print(Drug.iri)
print(DrugAssociation.is_a)#generator object
print(list(Drug.subclasses()))
print(DrugAssociation.ancestors())

#The types python module can be used in order to create classes and subclassed dynamically
#with my_ontology:
#    NewClass = types.new_class("NeaClassName", (Superclass,))

my_drug = Drug("nikospps")
print(my_drug.name)
print(my_drug.iri)

unamed_drug = Drug()#here, the name is automatically generated by python with a number
print(unamed_drug.name)

for i in Drug.instances(): print(i)

assert Drug("teo") is Drug("teo")

print(onto.nikospps.has_for_active_principle)
onto.my_drug.get_properties()

####
with onto:
    class Drug1(Thing):
        pass
    class Ingredient(Thing):
        pass
    class has_for_ingredient(ObjectProperty):
        domain = [Drug1]
        range = [Ingredient]
    class has_for_synonym(DataProperty):
        range = [str]

my_drug = Drug1("teo")
acetamine = Ingredient("Acetaminophen")

my_drug.has_for_ingredient = [acetamine]

my_drug.has_for_ingredient

# In addition, the ‘domain >> range’ syntax can be used when creating property.
# It replaces the ObjectProperty or DataProperty parent Class, as follows:
with onto:
    class Drug1(Thing):
        pass
    class Ingredient(Thing):
        pass
    class has_for_ingredient(Drug1 >> Ingredient):## instead of the above syntax
        pass


my_drug = Drug1("teo")
acetamine = Ingredient("Acetaminophen")

my_drug.has_for_ingredient = [acetamine]

my_drug.has_for_ingredient

# Appending a new value or in place of an existing one.
# Owlready2 automatically add or delete RDF triples in the quadstore

codeine = Ingredient("codeine")

my_drug.has_for_ingredient.append(codeine)#****
print(my_drug.has_for_ingredient)

# The same syntax is used for Data Properties, in case we may need this transofrmation

class has_for_synonym(DataProperty):
    range = [str]

#OR
class has_for_synonym(Thing >> str):
    pass