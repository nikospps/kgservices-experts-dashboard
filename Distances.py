# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:22:02 2019

@author: nikospps
"""

import textdistance
import fuzzy
from Person import Person
import Weights
import inspect
import re


def get_phonetic_Similarity(attribute1, attribute2, weight=[0.5,0.5]):
    dmeta = fuzzy.DMetaphone()
    
    metaphonetic1 = dmeta(attribute1)
    metaphonetic2 = dmeta(attribute2)
    
    metaphonetic1Proc = [x for x in metaphonetic1 if x is not None]
    metaphonetic2Proc = [x for x in metaphonetic2 if x is not None]
        
    metaphoneSimilarityList = list()
    for res1 in metaphonetic1Proc:
        for res2 in metaphonetic2Proc:
            metaphoneSimilarityList.append(get_text_similarity(res1, res2))
    
    if len(metaphoneSimilarityList)==0:
        metaphoneSimilarityMax = 0
    else:
        metaphoneSimilarityMax = max(metaphoneSimilarityList)
       
    nysiis1 = fuzzy.nysiis(attribute1)
    nysiis2 = fuzzy.nysiis(attribute2)
    if len(nysiis1)==0 and len(nysiis2)==0:
        nysiisSimilarity = 0
    else:
        nysiisSimilarity = get_text_similarity(nysiis1, nysiis2)
    #print(metaphoneSimilarityMax)
    #print(nysiisSimilarity)
    phoneticSimilarity = (weight[0]*metaphoneSimilarityMax + weight[1]*nysiisSimilarity)/sum(weight)

    #print("phonetic", phoneticSimilarity)
    return phoneticSimilarity

def get_text_similarity(attribute1, attribute2):
    fieldSimilarity = textdistance.jaro_winkler.similarity(attribute1, attribute2)
    return fieldSimilarity
    
def calculate_attribute_similarity(attribute1, attribute2, weight = [0.5, 0.5]):
    textSimilarity = get_text_similarity(attribute1, attribute2)
    
    cleanAttr1, cleanAttr1Len = clean_attribute(attribute1)
    cleanAttr2, cleanAttr2Len = clean_attribute(attribute2)
    
    # if the clean text does not have any words, but only symbols and digits do now
    # perform a phonetic comparison
    if (cleanAttr1Len == 0) and (cleanAttr2Len == 0):
        attribute_similarity = textSimilarity
    else:
        phoneticSimilarity = get_phonetic_Similarity(attribute1,attribute2,[0.5, 0.5])
        #print(textSimilarity)
        #print(phoneticSimilarity)
        attribute_similarity = textSimilarity*weight[0]+phoneticSimilarity*weight[1]
    
    return attribute_similarity

def calculate_person_similarity(person1, person2):
    attributes_person1 = inspect.getmembers(person1, lambda a:not(inspect.isroutine(a)))
    attributes_person2 = inspect.getmembers(person2, lambda a:not(inspect.isroutine(a)))
    attr_person1_proc = [a for a in attributes_person1 if not(a[0].startswith('__') and a[0].endswith('__'))]
    attr_person2_proc = [a for a in attributes_person2 if not(a[0].startswith('__') and a[0].endswith('__'))]
    
    similarities = dict()
    for i in range (len(attr_person1_proc)):
        if attr_person1_proc[i][0] == attr_person2_proc[i][0]:
            similarities[attr_person1_proc[i][0]] = calculate_attribute_similarity(attr_person1_proc[i][1], attr_person2_proc[i][1])
        
    # print(similarities)
    
    totalSimilarity = 0
    totalWeight = 0
    for key in similarities.keys():
        attrWeight = Weights.person_features_weights[key]
        attrSimilarity = similarities[key]*attrWeight
        totalWeight = totalWeight + attrWeight
        totalSimilarity = totalSimilarity + attrSimilarity

    return totalSimilarity/totalWeight


def clean_attribute(attribute):
    attrNoNumbers = re.sub("\d"," ", attribute)
    attrNoSymbols = re.sub("\W"," ", attrNoNumbers)
    attrOneWhiteSpace = re.sub("\s+"," ", attrNoSymbols)
    attrNoWhiteSpaces = re.sub("\s","", attrNoSymbols)
    
    return attrOneWhiteSpace, len(attrNoWhiteSpaces)
    
    
if __name__ == '__main__':
    person1 = Person("Ioannis", "John", "", 'Loumiotis', 'Greek', 'johny', "False", "", 'Male', 
                 '171', '98', '30/10/1986', 'Athens', 'Greece', '17', 'Areos')
    person2 = Person("Joannis", "John", "", 'Loumiotis', 'Greek', 'johny', "False", "", 'Male', 
             '171', '98', '30/10/1986', 'Athens', 'Greece', '17', 'Areos')
    person3 = Person("Pavlos", "Pavlitos", "", 'Kosmides', 'Greek', 'paul', "False", "", 'Male', 
                 '171', '98', '08/09/1985', 'Athens', 'Greece', '17', 'Papagou')
    person4 = Person("Ioannis", "John", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    person5 = Person("Joannis", "John", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
    person6 = Person("Karl", "", "", "Korch", "", "", "", "", "", "", "", "", "", "", "", "")
    person7 = Person("Karl", "", "", "Korcht", "", "", "", "", "", "", "", "", "", "", "", "")
    sim = calculate_person_similarity(person6, person7)
    print(sim)
