# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:18:56 2019
@author: Anik Paul Gomes\

"""
from twitter_keys_paul import consumer_key, consumer_secret, access_token, access_secret
import matplotlib.pyplot as plt
import tweepy
import requests
from bs4 import BeautifulSoup

#Setting up Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Calculating twitter ration for twitter accounts -Messi, Ronaldo, Neymer

#Twitter ratio for messi
twitter_ratio_messi = []
for status in tweepy.Cursor(api.user_timeline, id="imessi").items(1000):
    print(status.text)
    retweets = status.retweet_count
    likes = status.favorite_count
    status = 'https://twitter.com/imessi/status/{}'.format(status.id)
    r = requests.get(status)
    soup = BeautifulSoup(r.text, 'html5lib')
    replies = soup.find('span', {"class": "ProfileTweet-actionCount"})
    num_replies = int(replies['data-tweet-stat-count'])
    print(retweets, likes, num_replies)
    twitter_ratio_messi.append(round((num_replies/(likes + retweets)), 3))  
    print(twitter_ratio_messi)
    print("--------------------------------------------------------------------")
        





#Using tweepy module this way does not give correct number of replies
"""
#Calculating twitter ration for twitter accounts -Messi, Ronaldo, Neymer

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
"""