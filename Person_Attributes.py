# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:33:19 2019

@author: nikospps
"""
#Its not a bad approach in order to define classes with specific attributes and return different instances

# class Person:
#     def __init__(self, id, birthname, firstname, middlename, surname, nationality, nickname, isdead, isInterestedIn, gender,
#                  height, weight, dateOfBirth, city, country, houseNumber, street):
#         self.id = id
#         self.birthname = birthname
#         self.firstname = firstname
#         self.middlename = middlename
#         self.surname = surname
#         self.nationality = nationality
#         self.nickname = nickname
#         self.isDead = isdead
#         self.isInterestedIn = isInterestedIn
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#         self.dateOfBirth = dateOfBirth
#         self.city = city
#         self.country = country
#         self.houseNumber = houseNumber
#         self.street = street

##***For Demo Purposes on 3rd of July***##
class Person:
    def __init__(self, id, birthname, firstname, middlename,dateOfBirth):
        self.id = id
        self.birthname = birthname
        self.firstname = firstname
        self.middlename = middlename
        self.dateOfBirth = dateOfBirth


