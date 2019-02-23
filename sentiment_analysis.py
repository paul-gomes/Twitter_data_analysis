# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 03:20:48 2019
@author: Anik Paul Gomes
"""

import matplotlib.pyplot as plt
import pickle




#Sentimental analysis on 3 different twitter accounts

import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()



#loading from pickel cashed file 
with open('messi.pkl', 'rb') as f:
    messi_tweets  = pickle.load(f)
    
    
with open('ronaldo.pkl', 'rb') as f:
    ronaldo_tweets  = pickle.load(f)
    
with open('neymer.pkl', 'rb') as f:
    neymer_tweets  = pickle.load(f)

#Functions that does the sentimental analysis and returns postives, neutrals, negatives 
def sentiments(tweets):
    texts = [tweet.text for tweet in tweets]
    sents = [analyzer.polarity_scores(t) for t in texts]
    pos_x = [s['pos'] for s in sents]
    neu_y = [s['neu'] for s in sents]
    neg_z = [s['neg'] for s in sents]
    return pos_x, neu_y, neg_z

#plotting the sentimental analysis in a 3D graph
    
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#Messi sentiment anaylysis 
messi_pos_x, messi_neu_y, messi_neg_z = sentiments(messi_tweets)

#Ronaldo sentiment analysis
ronaldo_pos_x, ronaldo_neu_y, ronaldo_neg_z = sentiments(ronaldo_tweets)

#Neymer sentiment analysis
neymer_pos_x, neymer_neu_y, neymer_neg_z = sentiments(neymer_tweets)

ax.scatter(messi_pos_x, messi_neu_y, messi_neg_z, c ='green', marker='o')
ax.scatter(ronaldo_pos_x, ronaldo_neu_y, ronaldo_neg_z, c ='blue', marker='^')
ax.scatter(neymer_pos_x, neymer_neu_y, neymer_neg_z, c ='red', marker='o')


ax.set_xlabel('Positive')
ax.set_ylabel('Neutral')
ax.set_zlabel('Negative')
  

plt.show()
