import nltk
import string
import os
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

import nltk.data

#############
first = True
############

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
parCount = 0
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
    parCount+=1
    print "========================== paragraph: " + str(parCount) + " sentences " + str(sentCount)+ " - " + (str(sentCount+len(sentences)-1))
    c = sentCount
    sentCount += len(sentences)
    
    for sent in sentences:
        print "==============="
        print (sent, c)
        c+=1
    #if first:
    #    print sentences[0]
    #else:
    #    print sentences[len(sentences)-1]

