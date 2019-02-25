# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:34:52 2019
@author: Anik Paul Gomes

"""
import matplotlib.pyplot as plt
import pickle
from collections import Counter


#Finding the source of the tweets(iphone, andriod, web client)
#return clinet and number of tweets from it
def find_client(tweets):
    tweet_source = list(map(lambda x: x.source, tweets))
    return dict(Counter(tweet_source))




#loading from pickel cashed file 
with open('messi.pkl', 'rb') as f:
    messi_tweets  = pickle.load(f)

with open('ronaldo.pkl', 'rb') as f:
    ronaldo_tweets  = pickle.load(f)
    
with open('neymer.pkl', 'rb') as f:
    neymer_tweets  = pickle.load(f)
    

messi_tweet_source = find_client(messi_tweets)
print(messi_tweet_source)
ronaldo_tweet_source = find_client(ronaldo_tweets)
print(ronaldo_tweet_source) 
neymer_tweet_source = find_client(neymer_tweets)
print(neymer_tweet_source)


#plotting the tweet source of messi, ronaldo, neymer

#plotting messi

figureM, axM = plt.subplots()
axM.bar(list(messi_tweet_source.keys()), list(messi_tweet_source.values()), color="Green")
figureM.suptitle('Messi Tweet Source Frequency')
axM.set_xlabel('Tweet Source')
axM.set_ylabel('Frequency')

#plotting Ronaldo
figureR, axR = plt.subplots()
axR.bar(list(ronaldo_tweet_source.keys()), list(ronaldo_tweet_source.values()), color="Blue")
figureR.suptitle('Ronaldo Tweet Source Frequency')
axR.set_xlabel('Tweet Source')
axR.set_ylabel('Frequency')


#plotting Neymer
figureN, axN = plt.subplots()
axN.bar(list(neymer_tweet_source.keys()), list(neymer_tweet_source.values()), color="Red")
figureN.suptitle('Neymer Tweet Source Frequency')
axN.set_xlabel('Tweet Source')
axN.set_ylabel('Frequency')




plt.show()

