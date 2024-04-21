# -*- coding: utf-8 -*-
import Distances
from Person import Person

def calculate_distances(personList):
    results = list()
    for i in range(len(personList)):
        for j in range(i+1,len(personList)):
            dist = Distances.calculate_person_similarity(personList[i], personList[j])
            results.append((personList[i],personList[j], dist))
            # print((i,j, dist))
    return results

# Calculate all the relations between nearest neighbors without the use of a predefined threshold
def calculate_nearest_neighbors(personList, threshold = 0.50):
    checkList = calculate_distances(personList)
    filteredResults = [x for x in checkList] #if x[2]>=threshold]
    return filteredResults

# Calculate all the relations between nearest neighbors with the use of a predefined threshold
def calculate_nearest_neighbors_thres(personList, threshold = 0.75):
    checkList = calculate_distances(personList)
    filteredResults = [x for x in checkList if x[2]>=threshold]
    return filteredResults

# def calculate_nearest_neighbors(personList, threshold = 0.50):
#     personSimilarities = calculate_distances(personList)
#     filteredResults = [x for x in personSimilarities if x[2]>=threshold]
#     return filteredResults


# if __name__ == '__main__':
#     # print('here')
#     # person1 = Person("", "Karl", "", "Korch", "", "", "", "", "", "", "", "", "", "", "", "")
#     # person2 = Person("", "Karl", "", "Korcht", "", "", "", "", "", "", "", "", "", "", "", "")
#     # person3 = Person("", "Dieter", "", "Kenny", "", "", "", "", "", "", "", "", "", "", "", "")
#     #
#     #
#     # personList  = list((person1, person2, person3)) # list of persons
#
#     similarities = calculate_nearest_neighbors(personList)
#     for i in range(len(similarities)):
#          newMessage = {
#             'Person1_Name': str(similarities[i][0].firstname),
#             'Person1_Surname': str(similarities[i][0].surname),
#             'Person2_Name': str(similarities[i][1].firstname),
#             'Person2_Surname': str(similarities[i][1].surname),
#             'Confidence': str(similarities[i][2])
#             }
#     print(similarities[0][2])