# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:35:41 2019

@author: johnl
"""

# Retrieve the instances from ontology - TO BE IMPLEMENTED

from Person import Person
#from sparqltest import Person

def get_persons():
    person1 = Person("Ioannis", "John", "", 'Loumiotis', 'Greek', 'johny', "False", "", 'Male', 
                     '171', '98', '30/10/1986', 'Athens', 'Greece', '17', 'Areos')
    person2 = Person("Joannis", "John", "", 'Loumiotis', 'Greek', 'johny', "False", "", 'Male', 
                 '171', '98', '30/10/1986', 'Athens', 'Greece', '17', 'Areos')
    person3 = Person("Pavlos", "Pavlitos", "", 'Kosmides', 'Greek', 'paul', "False", "", 'Male', 
                     '171', '98', '08/09/1985', 'Athens', 'Greece', '17', 'Papagou')
    person4 = Person("Pavlos", "Pavltos", "", 'Kosmides', 'Greek', 'paul', "False", "", 'Male', 
                     '171', '98', '08/09/1985', 'Athens', 'Greece', '17', 'Papagou')
    person5 = Person("Ioannas", "John", "", 'Loumiotis', 'Greek', 'johny', "False", "", 'Male', 
                     '171', '98', '30/10/1986', 'Athens', 'Greece', '17', 'Areos')
    
    personList  = list((person1, person2, person3, person4, person5)) # list of persons
    
    return personList