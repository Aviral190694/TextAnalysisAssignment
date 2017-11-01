import os
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from os import listdir
from os.path import isfile, join
from sklearn.feature_extraction.text import TfidfVectorizer
import glob
from sklearn.metrics.pairwise import linear_kernel


def find_similar(tfidf_matrix, index, top_n = 5):
  cosine_similarities = linear_kernel(tfidf_matrix[index:index+1], tfidf_matrix).flatten()
  related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
  return [(index, cosine_similarities[index]) for index in related_docs_indices][0:top_n]


corpus = []
for file in glob.glob("files/*.txt"):
  with open(file, "r") as paper:
    corpus.append((file, paper.read()))

onlyfiles = [f for f in listdir("files") if isfile(join("files", f))]
corpusdir = 'files/' # Directory of corpus.
root = os.getcwd()
newcorpus = PlaintextCorpusReader(corpusdir, '.*',encoding="latin-1")
print(len(onlyfiles))
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
tfidf_matrix =  tf.fit_transform([content for file, content in corpus])
print(tfidf_matrix)

print(corpus[10])
for index, score in find_similar(tfidf_matrix, 10):
  print(score,index)
