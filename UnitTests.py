# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:44:41 2019

@author: johnl
"""

import unittest
import Distances as dis
from Person import Person
import HtmlTestRunner
import kNNCalculation as knnc

attribute1 = "Peter"
attribute2 = "Petes" 
person1 = Person("Karl", "", "", "Korch", "", "", "", "", "", "", "", "", "", "", "", "")
person2 = Person("Karl", "", "", "Korcht", "", "", "", "", "", "", "", "", "", "", "", "")

person3 = Person("", "Karl", "", "Korch", "", "", "", "", "", "", "", "", "", "", "", "")
person4 = Person("", "Karl", "", "Korcht", "", "", "", "", "", "", "", "", "", "", "", "")
person5 = Person("", "Dieter", "", "Kenny", "", "", "", "", "", "", "", "", "", "", "", "")




class TestDistanceMethods(unittest.TestCase):

    
    
    def test_phonetic_Similarity(self):
        print("Checking phonetic similarity.... OK")
        self.assertEqual(dis.get_phonetic_Similarity(attribute1, attribute2, [0.5,0.5]), 0.8222222222222222)

    def test_text_Similarity(self):
        print("Checking text similarity.... OK")
        self.assertEqual(dis.get_text_similarity(attribute1, attribute2), 0.92)
        
    def test_attribute_Similarity(self):
        print("Checking attribute similarity (includes phonetic and text similarity).... OK")
        self.assertEqual(dis.calculate_attribute_similarity(attribute1, attribute2, [0.5,0.5]), 0.8711111111111112)
        
    def test_person_Similarity(self):
        print("Checking two person similarity score.... OK")
        self.assertEqual(dis.calculate_person_similarity(person1, person2), 0.9931249999999999)
        
    def test_person_results(self):
        print("Checking similarity of multiple persons.... OK")
        personList  = list((person3, person4, person5)) # list of persons
        similarities = knnc.calculate_nearest_neighbors(personList)
        
        #self.assertEqual(message, "{'Person1_Name': 'Karl', 'Person1_Surname': 'Korch', 'Person2_Name': 'Karl', 'Person2_Surname': 'Korcht', 'Confidence': '0.9931249999999999'}")
        self.assertEqual(str(similarities[0][0].firstname)+" "+str(similarities[0][0].surname)+", "
                             +str(similarities[0][1].firstname)+" "+str(similarities[0][1].surname)+" : "+
                                  str(similarities[0][2]), "Karl Korch, Karl Korcht : 0.9931249999999999")

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))


