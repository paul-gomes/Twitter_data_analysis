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








#loading from pickel cashed file 
with open('pickles/messi.pkl', 'rb') as f:
    messi_tweets  = pickle.load(f)

with open('pickles/ronaldo.pkl', 'rb') as f:
    ronaldo_tweets  = pickle.load(f)
    
with open('pickles/neymer.pkl', 'rb') as f:
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
axM.bar(list(messi_tweet_source.keys()), list(messi_tweet_source.values()),width=0.5, color="Green")
figureM.suptitle('Messi Tweet Source Frequency')
axM.set_xlabel('Tweet Source')
axM.set_ylabel('Frequency')
add_value_labels(axM)

#plotting Ronaldo
figureR, axR = plt.subplots()
axR.bar(list(ronaldo_tweet_source.keys()), list(ronaldo_tweet_source.values()),width=0.5, color="Blue")
figureR.suptitle('Ronaldo Tweet Source Frequency')
axR.set_xlabel('Tweet Source')
axR.set_ylabel('Frequency')
add_value_labels(axR)


#plotting Neymer
figureN, axN = plt.subplots()
axN.bar(list(neymer_tweet_source.keys()), list(neymer_tweet_source.values()),width=0.5, color="Red")
figureN.suptitle('Neymer Tweet Source Frequency')
axN.set_xlabel('Tweet Source')
axN.set_ylabel('Frequency')
add_value_labels(axN)




plt.show()

