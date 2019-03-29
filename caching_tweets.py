# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:11:40 2019
@author: Anik Paul Gomes

"""

from twitter_keys_paul import consumer_key, consumer_secret, access_token, access_secret
import tweepy
import pickle


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


#caching tweets for messi
messi_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="imessi").items(150):
    messi_tweet_to_cache.append(status)     
     
with open('pickles/messi.pkl', 'wb') as f:
    pickle.dump(messi_tweet_to_cache, f)
    
print(len(messi_tweet_to_cache))
#caching tweets for ronaldo    
ronaldo_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="Cristiano").items(150):
    ronaldo_tweet_to_cache.append(status)     
     
with open('pickles/ronaldo.pkl', 'wb') as f:
    pickle.dump(ronaldo_tweet_to_cache, f)

print(len(ronaldo_tweet_to_cache))
    

   
#caching tweets for neymer
neymer_tweet_to_cache = []

for status in tweepy.Cursor(api.user_timeline, id="neymarjr").items(150):
    neymer_tweet_to_cache.append(status)     
     
with open('pickles/neymer.pkl', 'wb') as f:
    pickle.dump(neymer_tweet_to_cache, f)
    
print(len(neymer_tweet_to_cache))
  
 






