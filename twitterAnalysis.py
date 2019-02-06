# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:11:40 2019

@author: Anik Paul Gomes
"""

from twitter_keys_paul import consumer_key, consumer_secret, access_token, access_secret
import tweepy

#Setting up Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#Getting my homeline data to check authentiation is established 
my_tweets = api.home_timeline()
for tweet in my_tweets:
    print(tweet.author.screen_name)