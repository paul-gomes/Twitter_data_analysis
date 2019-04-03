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
import pickle

#Setting up Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#Functions that adds labels at the end of each bar in a bar chart
def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.3f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.




#Calculating twitter ration for twitter accounts -Messi, Ronaldo, Neymer

"""
#Twitter ratio for messi
twitter_ratio_messi = []
for status in tweepy.Cursor(api.user_timeline, id="imessi").items(150):
    retweets = status.retweet_count
    likes = status.favorite_count
    status = 'https://twitter.com/imessi/status/{}'.format(status.id)
    r = requests.get(status)
    soup = BeautifulSoup(r.text, 'html5lib')
    replies = soup.find('span', {"class": "ProfileTweet-actionCount"})
    num_replies = int(replies['data-tweet-stat-count'])
    print(retweets, likes, num_replies)
    twitter_ratio_messi.append(round((num_replies/(likes + retweets)), 3))  
    print("--------------------------------------------------------------------")
        
print(twitter_ratio_messi)
print(len(twitter_ratio_messi))

#Pickling twitter ratio for messi
with open('pickles/twitter_ratio_messi.pkl', 'wb') as f:
    pickle.dump(twitter_ratio_messi, f)


#Twitter ratio for Ronaldo
twitter_ratio_ronaldo = []
for status in tweepy.Cursor(api.user_timeline, id="Cristiano").items(150):
    retweets = status.retweet_count
    likes = status.favorite_count
    status = 'https://twitter.com/Cristiano/status/{}'.format(status.id)
    r = requests.get(status)
    soup = BeautifulSoup(r.text, 'html5lib')
    replies = soup.find('span', {"class": "ProfileTweet-actionCount"})
    num_replies = int(replies['data-tweet-stat-count'])
    print(retweets, likes, num_replies)
    twitter_ratio_ronaldo.append(round((num_replies/(likes + retweets)), 3))  
    print("--------------------------------------------------------------------")
        
print(twitter_ratio_ronaldo)
print(len(twitter_ratio_ronaldo))

#Pickling twitter ratio for ronaldo
with open('pickles/twitter_ratio_ronaldo.pkl', 'wb') as f:
    pickle.dump(twitter_ratio_ronaldo, f)


#Twitter ratio for neymer
twitter_ratio_neymer = []
for status in tweepy.Cursor(api.user_timeline, id="neymarjr").items(150):
    retweets = status.retweet_count
    likes = status.favorite_count
    status = 'https://twitter.com/neymarjr/status/{}'.format(status.id)
    r = requests.get(status)
    soup = BeautifulSoup(r.text, 'html5lib')
    replies = soup.find('span', {"class": "ProfileTweet-actionCount"})
    num_replies = int(replies['data-tweet-stat-count'])
    print(retweets, likes, num_replies)
    twitter_ratio_neymer.append(round((num_replies/(likes + retweets)), 3))  
    print("--------------------------------------------------------------------")
        
print(twitter_ratio_neymer)
print(len(twitter_ratio_neymer))

#Pickling twitter ratio for neymer
with open('pickles/twitter_ratio_neymer.pkl', 'wb') as f:
    pickle.dump(twitter_ratio_neymer, f)

"""

#loading from pickel cashed file 
with open('pickles/twitter_ratio_messi.pkl', 'rb') as f:
    twitter_ratio_messi  = pickle.load(f)

with open('pickles/twitter_ratio_ronaldo.pkl', 'rb') as f:
    twitter_ratio_ronaldo  = pickle.load(f)
    
with open('pickles/twitter_ratio_neymer.pkl', 'rb') as f:
    twitter_ratio_neymer  = pickle.load(f)


twitter_ratio = {}

twitter_ratio["Messi"] = round((sum(twitter_ratio_messi)/ len(twitter_ratio_messi)) * 100, 4)
twitter_ratio["Ronaldo"] = round((sum(twitter_ratio_ronaldo)/ len(twitter_ratio_ronaldo)) * 100, 4)
twitter_ratio["Neymer"] = round((sum(twitter_ratio_neymer)/ len(twitter_ratio_neymer)) * 100, 4)

print(twitter_ratio)





#plotting the twitter ratio of messi, ronaldo, neymer

figure, ax = plt.subplots()
ax.bar(list(twitter_ratio.keys()), list(twitter_ratio.values()),width=0.5, )
figure.suptitle('Average Twitter Ratio')
ax.set_xlabel('Users')
ax.set_ylabel('Twitter ratio')

add_value_labels(ax)
plt.show()











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