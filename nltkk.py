# Python program to generate word vectors using Word2Vec 

# importing all necessary modules 
import os
import nltk
import nltk.corpus
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize 
# import warnings 
import gensim
from gensim.models import Word2Vec 

########### For download the NLTk files for window ########## 
# nltk.download()

# print(os.listdir(nltk.data.find("corpora")))
# print(brown.words())
# print(nltk.corpus.gutenberg.fileids())

hamlet = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
# print(hamlet)
for word in hamlet[:500]:
	print(word, sep=' ', end=' ')