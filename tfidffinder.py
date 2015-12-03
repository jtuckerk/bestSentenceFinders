import nltk
import string
import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

path = '/Users/tuckerkirven/Desktop/Independent Study/levelDesign1.txt'
token_dict = {}
token_dict2= {}
sentence_list = []
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


file_path = path
shakes = open(file_path, 'r')
text = shakes.read()
text = re.sub('[^\x00-\x7F]+',' ', text)
sentences = tokenizer.tokenize(text)
lowers = text.lower()
no_punctuation = lowers.translate(None, string.punctuation)
token_dict[file] = no_punctuation
        
#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

print tfs
maxNum = 0
maxSent =""
sentCount = 0
for s in sentences:
    lowers = s.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    token_dict2[file] = no_punctuation
    tfs2 = tfidf.transform([no_punctuation])
    val = tfs2*tfs.T
    sentence_list.append((sentCount,val.data,s))
    sentCount+=1

#for x,y in sorted(sentence_list,key=lambda x: x[1])[-29:]:
#    print "BEST: " + str(x) 

top5 = sorted(sentence_list,key=lambda x: x[1])[-1:]
for a in sentence_list:
    if a in top5:
        print "===========\n"
        print a
