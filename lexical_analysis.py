# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 03:18:16 2019
@author: Anik Paul Gomes
"""

import matplotlib.pyplot as plt
import pickle

#Lexical diversity calculation for 3 different twitter accounts

'''
Lexical diversity is measure of how many different words that are used in a text.
Here I will calculate lexical diversity in 3 different twitter accounts.
'''
#Lexical diversity for messi

def lexical_diversity(text):
    return round(100*len(set(text))/ len(text), 2)

messi_lexical_diversity = []
ronaldo_lexical_diversity = []
neymer_lexical_diversity = []

#messi's lexical diversity
#loading from pickel cashed file 
with open('messi.pkl', 'rb') as f:
    messi_tweets  = pickle.load(f)
        
for tweet in messi_tweets:
    messi_lexical_diversity.append(lexical_diversity(tweet.text))
    
#ronaldo's lexical diversity
with open('ronaldo.pkl', 'rb') as f:
    ronaldo_tweets  = pickle.load(f)
       
for tweet in ronaldo_tweets:
    ronaldo_lexical_diversity.append(lexical_diversity(tweet.text))

#neymer's lexical diversity

with open('neymer.pkl', 'rb') as f:
    neymer_tweets  = pickle.load(f)
        
for tweet in neymer_tweets:
    neymer_lexical_diversity.append(lexical_diversity(tweet.text))  
    

#plotting the lexical diversity of messi, ronaldo, neymer


plt.subplot(1,3, 1)
plt.plot(messi_lexical_diversity, color='green')
plt.xlabel('Each tweets')
plt.ylabel('Lexical Diversity in percentage')
plt.title('Lexical diversity in percentage for each tweet', loc='center')


plt.subplot(1,3, 2)
plt.plot(ronaldo_lexical_diversity, color='blue')
plt.xlabel('Each tweets')
plt.ylabel('Lexical Diversity in percentage')

plt.subplot(1,3, 3)
plt.plot(neymer_lexical_diversity, color='red')
plt.xlabel('Each tweets')
plt.ylabel('Lexical Diversity in percentage')


plt.show()

