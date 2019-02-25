# Twitter Data Analysis
    Lexical diversity, Sentimental Analysis, Twitter Ratio, Device and Client Used.

### Technology Used
* Language - Python
* Modules - Matplotlib, tweepy, numpy, nltk
* IDE - Spyder

### Background
In Twitter, vast variety of people publicly post contents. Just as in real life, individuals communicate differently and can be differentiated by the differences in the works they create. This is an attempt to differnciate 3 Twitter accounts. The 3 different accounts that I have chosen for this purpose is 3 international footballers- Leonel Messi, Cristiano Ronaldo, Neymer. They are well known for their great performance in football world and considered rivals. This reads at least 3000 tweets of each players and calculates lexical diversity, does sentimental analysis, calculates twitter ratio, analyzes the devices and client they used to tweet. 

| ![Messi](/image/messi.jpg) | ![Ronaldo](/image/ronaldo.jpg) | ![Neymer](/image/neymer.jpg) |
|----------------------------|--------------------------------|------------------------------|
|            Messi           |             Ronaldo            |            Neymer            |

#### Lexical Diversity
Lexical diversity calculates how many different words that are used in the text.</br>
![Lexical diversity of Messi, Ronaldo, Neymer](/image/lexical_diversity.PNG)</br>

    Green - Messi, Blue - Ronaldo, Red - Neymer.
Lexical diversity = unique words/ total words. The more the lexical diversity is the more unique words have been used by the user. Y-axis is the lexical diversity in percentage for each tweets in X-axis. For each users, the number of tweets are 150. It looks like, Ronaldo and Neymer have ups and downs(quite a variations) in their lexical diversity. However, Ronaldo have more tweets with high lexical diversity than Neymer. On the other hand, Messi does not have very much tweets with high lexical diversity. Although there is lot of variations in the outcome, the highest peak is the almost the same for each users. 

#### Senimental Analysis
| ![Sentimental Angle1](/image/sentimental_angle1.png) | ![sentimental Angle2](/image/sentimental_angle2.png) | ![Sentimental Angle3.png](/image/sentimental_angle3.png) | ![Sentimental Angle4.png](/image/sentimental_angle4.png) |
|-----------------------------------------------------|------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
    Green - Messi, Blue - Ronaldo, Red - Neymer.

Sentiment analysis is categorizing or identifying opinions inorder to determine writer's attitude towards a topic. In my analysis, I have done sentiment analysis on Messi, Ronaldo, and Neymer's tweets. According to my analysis, most of their tweets can be categorized as neutral, however, Messi has more negative tweets than Ronaldo and Neymer. 

#### Word Frequency Analysis

| ![Messi](/image/word_frequency_messi.PNG) | ![Ronaldo](/image/word_frequency_ronaldo.PNG) | ![Neymer](/image/word_frequency_neymer.PNG) |
|----------------------------|--------------------------------|------------------------------|
| Messi Word Frequency       |Ronaldo Word Frequency          |Neymer Word Frequency           |




