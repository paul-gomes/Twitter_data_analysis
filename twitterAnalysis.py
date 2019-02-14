# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:11:40 2019

@author: Anik Paul Gomes
"""

from twitter_keys_paul import consumer_key, consumer_secret, access_token, access_secret
import matplotlib.pyplot as plt
import tweepy
import pickle
import numpy as np

#Setting up Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

'''
To get more than 20 statues, we would have to do pagination.
In order to perform pagination we must supply a page/cursor 
parameter with each of our requests. Cursor object makes it 
easy to handle all the pagination work behind the scene.
'''

#pickling the tweets for 3 different accounts - Messi, Ronaldo, Neymer

'''
#caching tweets for messi
messi_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="imessi").items(3000):
    messi_tweet_to_cache.append(status)     
     
with open('messi.pkl', 'wb') as f:
    pickle.dump(messi_tweet_to_cache, f)
    

#caching tweets for ronaldo    
ronaldo_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="Cristiano").items(3000):
    ronaldo_tweet_to_cache.append(status)     
     
with open('ronaldo.pkl', 'wb') as f:
    pickle.dump(ronaldo_tweet_to_cache, f)

print(len(ronaldo_tweet_to_cache))
    

   
#caching tweets for neymer
neymer_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="neymarjr").items(3000):
    neymer_tweet_to_cache.append(status)     
     
with open('neymer.pkl', 'wb') as f:
    pickle.dump(neymer_tweet_to_cache, f)
    
print(len(neymer_tweet_to_cache))
    
''' 

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


#Sentimental analysis on 3 different twitter accounts








































'''

#CALCULATING TWITTER RATIO FOR MESSI, RONALDO, NEYMER






for status in tweepy.Cursor(api.user_timeline, id="imessi").items(1):
    print(status.text)
    retweets = status.retweet_count
    likes = status.favorite_count
    replies_count = 0
    status_id = status.id
    
    # fetching all the reply
    for reply in tweepy.Cursor(api.search, q='@imessi', since_id = status_id).items():
        print(reply.text)
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if (reply.in_reply_to_status_id_str == status.id_str):
                #print(reply.author.screen_name, "", reply.text, )
                print("-------------------------------------")
                replies_count += 1
                
    print(retweets, likes, replies_count) 
        
    print("-------------------------------------")
    
'''