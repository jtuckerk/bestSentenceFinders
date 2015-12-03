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
sentence_dict = {}
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

paragraphs = text.split("\n\n");
sentCount = 0
for par in paragraphs:
    text = par
    text = re.sub('[^\x00-\x7F]+',' ', text)
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    token_dict[file] = no_punctuation
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(token_dict.values())
    
    sentences = tokenizer.tokenize(text)
    maxNum = 0
    maxSent =""
    numInSent = 0
    maxCountInSent = 0
    for s in sentences:
        lowers = s.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict2[file] = no_punctuation
        tfs2 = tfidf.transform([no_punctuation])
        print "=========\n" + no_punctuation
        val = tfs2*tfs.T
        print val
        if val > maxNum:
            maxSent = s
            maxNum = val
            maxCountInSent = numInSent
        numInSent +=1
    print "Best: " + str(sentCount + maxCountInSent)
    sentCount += len(sentences)
