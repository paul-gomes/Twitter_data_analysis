# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 03:25:53 2019
@author: Anik Paul Gomes
"""

import matplotlib.pyplot as plt
import pickle
from collections import Counter
import re


#Basic frequency distribution from words in tweets
#loading from pickel cashed file 
with open('messi.pkl', 'rb') as f:
    messi_tweets  = pickle.load(f)
    
    
with open('ronaldo.pkl', 'rb') as f:
    ronaldo_tweets  = pickle.load(f)
    
with open('neymer.pkl', 'rb') as f:
    neymer_tweets  = pickle.load(f)
    

#Messi's word frequency distribution 

#Creates 2D list. List of tweets of words.
messi_words = [tweet.text.split() for tweet in messi_tweets] 

#converting list of list into one list
messi_words = [y for x in messi_words
                   for y in x]
#Getting rid of special characters
messi_words = list(map(lambda x: re.sub("[0-9\.?@#%*,!&:/…-]", "", x).lower(), messi_words))
#Getting rid of empty string
messi_words = list(filter(None, messi_words))
                                          
#Counting the number of each words using Counter method
messi_word_frequency = Counter(messi_words) 

#top 10 words
messi_word_frequency_top10 = messi_word_frequency.most_common()[:10]
messi_word_frequency_top10 = dict(messi_word_frequency_top10)



#Ronaldo's word frequency distribution 

#Creates 2D list. List of tweets of words.
ronaldo_words = [tweet.text.split() for tweet in ronaldo_tweets] 

#converting list of list into one list
ronaldo_words = [y for x in ronaldo_words
                   for y in x]
#Getting rid of special characters
ronaldo_words = list(map(lambda x: re.sub("[0-9\.?@#%*,!&:/…-]", "", x).lower(), ronaldo_words))
#Getting rid of empty string
ronaldo_words = list(filter(None, ronaldo_words))
                                          
#Counting the number of each words using Counter method
ronaldo_word_frequency = Counter(ronaldo_words)  

#Top 10 words
ronaldo_word_frequency_top10 = ronaldo_word_frequency.most_common()[:10]
ronaldo_word_frequency_top10 = dict(ronaldo_word_frequency_top10)



#Neymer's word frequency distribution 

#Creates 2D list. List of tweets of words.
neymer_words = [tweet.text.split() for tweet in neymer_tweets] 

#converting list of list into one list
neymer_words = [y for x in neymer_words
                   for y in x]
#Getting rid of special characters
neymer_words = list(map(lambda x: re.sub("[0-9\.?@#%*,!&:/…-]", "", x).lower(), neymer_words))
#Getting rid of empty string
neymer_words = list(filter(None, neymer_words))
                                          
#Counting the number of each words using Counter method
neymer_word_frequency = Counter(neymer_words)

#Top 10 words
neymer_word_frequency_top10 = neymer_word_frequency.most_common()[:10]
neymer_word_frequency_top10 = dict(neymer_word_frequency_top10)

#plotting the lexical diversity of messi, ronaldo, neymer

#plotting messi

figureM, axM = plt.subplots()
axM.scatter(list(messi_word_frequency_top10.keys()), list(messi_word_frequency_top10.values()))
figureM.suptitle('Messi Word Frequency (Top 10)')

#plotting Ronaldo
figureR, axR = plt.subplots()
axR.scatter(list(ronaldo_word_frequency_top10.keys()), list(ronaldo_word_frequency_top10.values()))
figureR.suptitle('Ronaldo Word Frequency (Top 10)')

#plotting Neymer
figureN, axN = plt.subplots()
axN.scatter(list(neymer_word_frequency_top10.keys()), list(neymer_word_frequency_top10.values()))
figureN.suptitle('Neymer Word Frequency (Top 10)')



plt.show()
