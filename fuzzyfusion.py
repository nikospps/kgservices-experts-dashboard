from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Fuzzy String Matching is a well known problem that is built on Leivenshtein Distance.
# It calculates how similar two strings are. This can also be calculated by finding out the number
# of operations needed to transform one string to the other .e.g with the name “Barack”, one might spell it
# as “Barac”. Only one operation is needed to correct this i.e adding a K at the end.

#  this is because the fuzz.ratio() method just calculates the edit distance between some ordering of
#  the token in both input strings using the difflib.ratio
fuzz.ratio("Catherine M Gitau","Catherine Gitau")
fuzz.ratio("barack","barack")
fuzz.ratio("ASd432FGC12789","Asd432FGC12789")

import nltk
from nltk.translate import bleu
from nltk.translate.bleu_score import SmoothingFunction
smoothie = SmoothingFunction().method4

C1='nikos peppes'
C2='giwrge pepes'

print('BLEUscore:',bleu([C1], C2, smoothing_function=smoothie))

import jellyfish

jellyfish.jaro_similarity(C1,C2)

from textdistance import jaro_winkler

n = float(jaro_winkler.distance(C1,C2))

dev1 = 'gnfuv-temp-exp1-55d487b85b-5g2xh'
dev2 = 'gnfuv-temp-exp1-55d487b85b-2bl8b'
dev3 = 'gnfuv-temp-exp1-55d487b85b-xcl97'
dev4 = 'gnfuv-temp-exp1-55d487b85b-5ztk8'

devlist = [dev1, dev2, dev3, dev4]

tempdev = 'gn31fuv-temp-exp21-55d487b85b-5g2xh'

# itertools.combinations will pair each element with each other element in the iterable, but only once
import itertools
import jellyfish
# for a, b in itertools.combinations(devlist, 2):
#     compare(a, b)

mylist = range(5)
for x,y in itertools.combinations(mylist, 2):
    print(x,y)

for x,y in itertools.combinations(devlist, 2):
    # print(x,y)
    print('Similarity between sensor {} and sensor {} is equal to: {}'.format(x,y,jellyfish.jaro_similarity(x, y)))

# fuzz.(tempdev,dev1)

fuzz.ratio(dev4,tempdev)

fuzz.token_set_ratio(tempdev,dev1)
# Asd432FGC12789
#91
fuzz.partial_ratio("Catherine M. Gitau","Catherine Gitau")
#100

# this method attempts to account for similar strings that are out of order
fuzz.token_sort_ratio("Catherine Gitau M.", "Gitau Catherine")
fuzz.token_sort_ratio("Karaolh Dhmhtriou 3,Athens", "Karaoli Dimitriou 3,Athens")

#94