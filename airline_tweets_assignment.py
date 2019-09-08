##
## File: assignment04.py (STAT 3250)
## Topic: Assignment 4
##

##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.

##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.

import numpy as np
import pandas as pd
at = pd.read_csv('airline_tweets.csv')

tw = at['tweet_id'].groupby(at['airline']) ## create a group by airlines
tw.count() ## count each airline


"""
1.
airline          count
American          2759
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504

"""



## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.


asent = at['airline_sentiment'].groupby(at['airline']) ## create a group by airline with sentiment
asent.count() ## total of each airline
asentpos = at[at['airline_sentiment']  == 'positive'] ## dataframe only for positive
asentpos2 = asentpos['tweet_id'].groupby(asentpos['airline']) ## create a group by airline with tweet_id to count total
asentpos2.count() ## ## total of positive 
print((asentpos2.count()/asent.count()*100).sort_values(ascending = False)) ## print the percentage



"""
## 2 

airline          percentage
Virgin America    30.158730
JetBlue           24.482448
Southwest         23.553719
United            12.872841
American          12.178325
US Airways         9.234466

"""


## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.

name = at['tweet_id'].groupby(at['name']) ## use groupby to create group
name.count().sort_values(ascending = False)[:11] ## count and sort values from largest


"""
## 3  

name            count
JetBlueNews        63
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
weezerandburnie    23
rossj987           23
GREATNESSEOA       22
MeeestarCoke       22
scoobydoo9749      21
jasemccarty        20

"""


## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.

name = at['tweet_id'].groupby(at['name']) ## make a group of name and tweetid indexed by name
morename = name.count() > 1 ## count names used greater than 1 to see True and False
morename.value_counts() ## use value_counts function to count true values
print(3000/len(name)*100) ## find the percentage


"""
4.
38.955979742890534

"""

## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.

negtw = at['name'].groupby(at['negativereason']) ## make a group by negative tweets
negtw.count().sort_values(ascending = False)[:5] ## count and sort values for the most five
negct = negtw.count() ## count
tot = np.sum(negct) ## sum up
percent = negct/tot*100 ## calculate the percentage
print(percent.sort_values(ascending = False)[:5]) ## print the answer



"""
5.

negativereason           percentage
Customer Service Issue    31.706254
Late Flight               18.141207
Can't Tell                12.965788
Cancelled Flight           9.228590
Lost Luggage               7.888429

"""

## 6.  How many of the tweets for each airline include the phrase "on fleek"?

american = at[at['airline'] == 'American'] ## subset american air as a dataframe
temp1 = american[american['text'].str.contains('on fleek')] ## subset text and find on fleek
united = at[at['airline'] == 'United']## subset american air as a dataframe
temp2 = united[united['text'].str.contains('on fleek')]## subset text and find on fleek
delta = at[at['airline'] == 'JetBlue']## subset Jetblue air as a dataframe
temp3 = delta[delta['text'].str.contains('on fleek')]## subset text and find on fleek
sw = at[at['airline'] == 'Southwest']## subset Southwest air as a dataframe
temp4 = sw[sw['text'].str.contains('on fleek')]## subset text and find on fleek
ua = at[at['airline'] == 'US Airways']## subset US airways as a dataframe
temp5 = ua[ua['text'].str.contains('on fleek')]## subset text and find on fleek
va = at[at['airline'] == 'Virgin America']## subset virgin america air as a dataframe
temp6 = va[va['text'].str.contains('on fleek')]## subset text and find on fleek


print(len(temp1)) ## print the lenth of temp1
print(len(temp1)) ## print the lenth of temp2
print(len(temp3)) ## print the lenth of temp3
print(len(temp4)) ## print the lenth of temp4
print(len(temp5)) ## print the lenth of temp5
print(len(temp6)) ## print the lenth of temp6

############ this method is faster ##########
list1 = ['American', 'United', 'JetBlue', 'Southwest', 'US Airways', 'Virgin America'] ## list for the airlines
for i in list1: ## use for loop
    american = at[at['airline'] == i] ## bring each airline
    temp1 = american[american['text'].str.contains('on fleek')] ## subset text and find on fleek
    print(i, ' has ', len(temp1), 'on fleek') ## print airline name and number of on fleek


"""
## 6 

American  has  0 on fleek
United  has  0 on fleek
JetBlue  has  146 on fleek
Southwest  has  0 on fleek
US Airways  has  0 on fleek
Virgin America  has  0 on fleek

"""


## 7.  What percentage of tweets included a hashtag?

has = at['text'] ## subset text
len(has[has.str.contains('#')]) / len(has)*100 ## find the # to count and find the percentage
                           
"""
## 7
 
17.001366120218577

"""
                           
## 8.  How many tweets include a link to a web site?

link = at['text'] ## subset text
len(link[link.str.contains('http')]) ## find the http and use length() to find the number of http

"""
## 8

1173

"""
     
## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?

att = at['text'] ## subset text 
len(att[att.str.count('@') >= 2]) ## count @ if a row has two or more @s
"""
## 9

1645

"""

## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.


### this works too!
def tweet(x , list):
    for i in list:
        if x == 'positive':
            atlist = at[at['airline'] == i]
            pos = atlist[atlist['airline_sentiment'] == x]
            print(len(pos))
        elif (x == 'negative'):
            atlist = at[at['airline'] == i]
            neg = atlist[atlist['airline_sentiment'] == x]
            print(len(neg))
        else:
            atlist = at[at['airline'] == i]
            neut = atlist[atlist['airline_sentiment'] == x]
            print(len(neut))
tweet('positive', list2)
tweet('negative', list2)
tweet('neutral', list2)


####### this method I used##########

list2 = ['American', 'United', 'JetBlue', 'Southwest', 'US Airways', 'Virgin America'] ## airline list
for i in list2: ## use for loop
    american1 = at[at['airline'] == i] ## subset airline
    possent = american1[american1['airline_sentiment'] == 'positive'] ## subset only positive from the above dataframe
    print(len(possent)) ## print the length of positive by each airline in the list

for i in list2: ## use for loop
    american1 = at[at['airline'] == i] ## subset airline in the loop
    negsent = american1[american1['airline_sentiment'] == 'negative'] ## subset only negative from the above dataframe
    print(-len(negsent)) ## print the length of negative by each airline in the list

for i in list2:
    american1 = at[at['airline'] == i] ## subset airline in the loop
    neusent = american1[american1['airline_sentiment'] == 'neutral'] ## subset only neutral from the above dataframe    
    print(len(neusent)) ## print the length of neutral by each airline in the list

meanofam = (336 - 1960) / (336 + 1960 + 463) ## calculate mean of american air
meanofun = (492 - 2633) / (492 + 2633 + 697) ## calculate mean of united air
meanofjb = (544 - 955) / (544 + 955 + 723) ## calculate mean of jetblue air
meanofsw = (570 - 1186) / (570 + 1186 + 664) ## calculate mean of southwest air
meanofua = (269 - 2263) / (269 + 2263 + 381) ## calculate mean of usairways
meanofva = (152 - 181) / (152 + 181 + 171) ## calculate mean of virgina america

airlinedf = pd.DataFrame({'airline':['American', 'United', 'JetBlue', 'Southwest', 'US Airways', 'Virgin America'],
                   'meanscore':[meanofam,meanofun,meanofjb,meanofsw,meanofua,meanofva]
                   }) ### create as dataframe to deliver it as a table form
airlinedf.index = ['','','','','',''] 
airlinedf.sort_values(by = 'meanscore', ascending = False) ## sort from largest to lowest

"""
## 10

       airline  meanscore
Virgin America  -0.057540
       JetBlue  -0.184968
     Southwest  -0.254545
        United  -0.560178
      American  -0.588619
    US Airways  -0.684518

"""


## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 
##     so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)


## tried
american1 = at[at['airline'] == 'American']
amat = american1[american1['text'].str.contains('@virginamerica')]
len(amat)


##I found this method too!!!
aline = at[at['airline'] == 'American']
alinelow = aline['text'].str.lower()
aldf = alinelow.to_frame(name='ltext')
amat = aldf[aldf['ltext'].str.contains('@usairways')]
###

##these are not good codes
l1 = ['United', 'JetBlue', 'Southwest', 'US Airways', 'Virgin America']
amct = 0
for i in l1:
    aline = at[at['airline'] == i]
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    amat = aldf[aldf['ltext'].str.contains('@american')]
    amct += len(amat)
print(amct)

l2 = ['American', 'JetBlue', 'Southwest', 'US Airways', 'Virgin America']
unct = 0
for i in l2:
    aline = at[at['airline'] == i]
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    unat = aldf[aldf['ltext'].str.contains('@united')]
    unct += len(unat)
print(unct)

l3 = ['American', 'United', 'Southwest', 'US Airways', 'Virgin America']
jbct = 0
for i in l3:
    aline = at[at['airline'] == i]
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    jbat = aldf[aldf['ltext'].str.contains('@jetblue')]
    jbct += len(jbat)
print(jbct)

l4 = ['American', 'United', 'JetBlue', 'US Airways', 'Virgin America']
swct = 0
for i in l4:
    aline = at[at['airline'] == i]
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    swat = aldf[aldf['ltext'].str.contains('@southwest')]
    swct += len(swat)
print(swct)

l5 = ['American', 'United', 'JetBlue', 'Southwest', 'Virgin America']
uact = 0
for i in l5:
    aline = at[at['airline'] == i]    
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    uaat = aldf[aldf['ltext'].str.contains('@usairways')]
    uact += len(uaat)
print(uact)

l6 = ['American', 'United', 'JetBlue', 'Southwest', 'US Airways']
vact = 0
for i in l6:
    aline = at[at['airline'] == i]
    alinelow = aline['text'].str.lower()
    aldf = alinelow.to_frame(name='ltext')
    vaat = aldf[aldf['ltext'].str.contains('@virginamerica')]     
    vact += len(vaat)
print(vact)

print(100*(amct + unct + jbct + swct + uact + vact) / len(at))


######################################I used this method######################

text = at['text'] ## subset text from the dataframe 
airline = at['airline'] ## subset airlines from the dataframe 
airline_list = ['@united', '@american', '@jetblue', '@southwest', '@virginamerica', '@usairways'] ## created airline lists with @
ct = 0 ## count variable
for i in range(len(text)): ## use for loop
    temp_text = text[i].lower() ## change text into lowercase
    temp_air = airline[i].lower().replace(" ", "") ## change airline into lowercase and remove the space 
    for air in airline_list: ## inner for loop
        if air in temp_text and air[1:] not in temp_air: ## if item in temp_text and not in temp_air
            print(temp_text)
            ct += 1 ## add 1 to count variable
            break ## break for loop

print(100*ct/len(text)) ## find the percentage and print 
                
##################################################################





"""
## 11

2.4453551912568305

"""


## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.


### I tried but not using
  
dropunique = at[at.duplicated(subset = ['name'], keep=False)]
name = dropunique['name']
name.value_counts()
len(name)

unique = dropunique.drop_duplicates(subset='name', keep='first', inplace=False)
names = unique['name']
names.value_counts()

recentpos = unique[unique['airline_sentiment'] == 'positive']
len(recentpos)

print(100*len(recentpos) / len(name))



####### this one is my answer ########################

totct = 0 ## global count variable
ct = 0 ## count variable 
name = at['name'] ## subset name column
for i in range(len(name)-1): ## use for loop
    if name[i] == name[i+1] and name[i] != name[i-1]: ## if item in the name is equal to i-1 and i+1
        totct += 1 ## add 1 to total count
        if at['airline_sentiment'][i] == 'positive': ## if it is positive 
            ct += 1 ## add 1 to count variable
print(100*ct/totct) ## find the percentage and print

####

"""
## 12

11.189634864546525

"""


## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)

import collections

hashtag = at['text'] ## subset text column
emptylist = [0] ## create an empty list
for i in hashtag: ## use for loop
    splt = i.split(" ") ## split texts by space in the hashtag
    for j in splt: ## inner for loop
        if j.startswith('#'): ## if the text start with #
            lower = j.lower() ## change it into lowercase
            emptylist.append(lower) ## put it into the empty list
ct=collections.Counter(emptylist) ## count
print(ct.most_common(11)) ## print the most common 11 hash tags and remove 0
hashdf = pd.DataFrame({'hashtags': ['#destinationdragons', '#fail', '#jetblue', '#unitedairlines', '#customerservice',
                                      '##usairways', '#neveragain', '#usairwaysfail', '#americanairlines',
                                      '#united'],
                        'counts': ['76', '64', '44', '43', '34', '30', '26', '26', '25', '25'] ## create as the table form
                                      })
hashdf.index= ['','','','','','','','','','']
print(hashdf) ## print the table




"""
13.

           hashtags counts
#destinationdragons     76
              #fail     64
           #jetblue     44
    #unitedairlines     43
   #customerservice     34
         #usairways     30
        #neveragain     26
     #usairwaysfail     26
  #americanairlines     25
            #united     25
              
"""







































