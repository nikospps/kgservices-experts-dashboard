from owlready2 import *
import types

#onto = get_ontology("http://test.org/onto.owl")
onto = get_ontology('http://147.102.7.185:3030/MAGNETO/data').load() #with or without data append in the uri\
onto = get_ontology('http://semanticdb.magneto.dcom.upv.es:3030/magneto_inst/data').load()
onto = get_ontology('http://147.102.7.185:3030/family/data').load()
onto = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl").load()
#onto = get_ontology("http://147.102.7.180:3030/ds/data?default").load()
onto = get_ontology("http://147.102.7.180:3030/ds").load()
#onto = get_ontology("http://147.102.7.180:3030/trakis").load()
print(list(onto.classes()))
print(list(onto.object_properties()))
print(list(onto.data_properties()))
print(list(onto.individuals()))
onto.hasGenre = []
onto.search(iri = "*ds")

onto['Genre']

with onto:
    class Drug(Thing):
        pass
    class Ingredient(Thing):
        pass
    class has_for_ingredient(ObjectProperty):
        domain = [Drug]
        range = [Ingredient]
    class has_for_synonym(DataProperty):
        range = [str]
    class is_ingredient_of(ObjectProperty):
        domain = [Ingredient]
        range = [Drug]
        inverse_property = has_for_ingredient
    class has_for_cost(DataProperty, FunctionalProperty):  # Each drug has a single cost
        domain = [Drug]
        range = [float]
    class ActivePrinciple(Ingredient):
        pass
    class has_for_active_principle(has_for_ingredient):
        domain = [Drug]
        range = [ActivePrinciple]

my_drug = Drug("nikospps")
aspirin = Ingredient("aspirin")

# my_drug = Drug("teo")
acetamine = Ingredient("Acetaminophen")

my_drug.has_for_ingredient = [acetamine] # or
my_drug.has_for_ingredient.append(aspirin)

onto.save(file='test.owl')

my_drug.has_for_ingredient

aspirin.is_ingredient_of

my_drug.has_for_cost = 4.2

print(my_drug.has_for_cost)

# Getting Relation Instances
print(list(onto.has_for_active_principle.get_relations()))