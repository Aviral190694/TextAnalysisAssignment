import os
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("files") if isfile(join("files", f))]
corpusdir = 'files/' # Directory of corpus.
root = os.getcwd()
newcorpus = PlaintextCorpusReader(corpusdir, '.*',encoding="latin-1")
print(len(onlyfiles))

fhand = open('stopWords.txt', 'r')
stopWords = fhand.read()
stopWords = stopWords.split('\n')

is_noun = lambda pos: pos[:2] == 'NN'
is_adject = lambda pos: pos[:2] == 'JJ'


for file in onlyfiles:
    print(file)
    text = newcorpus.words(file)
    print(nltk.pos_tag(text))
    print(len(text))
    filename = root + "/coupusFiles/" + file
    print(filename)
    f = open(filename, 'w')
    for words in text:
     print(is_noun(words)
            #      if is_noun(words):
#        if words.lower() not in stopWords:
#          f.write(words)
#          f.write("\n")
#      if is_adject(words):
#         if words.lower() not in stopWords:
#         f.write(words)
#         f.write("\n")
