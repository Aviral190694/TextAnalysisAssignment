import math
import os
from math import log
from os import listdir
from os.path import isfile, join
from collections import defaultdict

DOC_COUNT = len(onlyfiles)
#building vocabulary
defaultdir = root + "\\coupusFiles\\" 

#Possible words in vocabulary
vocabulary = set()
for file in onlyfiles:
	filename = defaultdir + file
	filecontent = open(filename, 'r').read()
	words = filecontent.split('\n')
	vocabulary.update(words)

#Calculaing idf
word_idf = defaultdict(lambda:0)

for file in onlyfiles:
	filename = defaultdir + file
	filecontent = open(filename, 'r').read().lower().split('\n')
	words = set(filecontent)
	for word in words:
		word_idf[word.lower()] += 1

for word in vocabulary:
	word_idf[word] = log(DOC_COUNT/float(1+word_idf[word]))
	
#calculating tf
tfidf = defaultdict(lambda:0)

count = 0 #Naming Documents
for file in onlyfiles:
	filename = defaultdir + file
	filecontent = open(filename, 'r').read().lower().split('\n')
	tf = defaultdict(lambda:0)
	for word in filecontent:
		tf[word] += 1
	print tf
	tfidf["doc"+str(count)] = defaultdict(lambda:0)
	for key in tf:
		tfidf["doc"+str(count)][key] = tf[key]*word_idf[key]
	count = count+1
