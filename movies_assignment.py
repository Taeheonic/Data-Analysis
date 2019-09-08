##
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
##

##  This assignment requires the data file 'movies.txt'.  This file
##  contains records for nearly 4000 movies, including a movie ID number, 
##  the title (with year of release, which is not part of the title), and a 
##  list of movie genre classifications (such as Romance, Comedy, etc). 

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.
import pandas as pd
import numpy as np    
open('movies.txt', encoding="utf8").read().splitlines() ## open text file
mvdf = pd.read_csv('movies.txt', sep='::',header=None, names=['ID','Title','Genre']) ## read text as dataframe 
type(mvdf) ## check if mvdf is dataframe
movies = mvdf.groupby('Title').size() ## make a group by title and subset size
repeated = movies > 1 ## find if there is repeated movie titles
print(np.sum(repeated)) ## print the number of repeated titles

"""
1.

0

"""

## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".

genre = mvdf['Genre'] ## subset Genre
print(len(genre[genre.str.contains('Action')])) ## subset strings which contain action and find the number of it
print(len(genre[genre.str.contains('Comedy')])) ## subset strings which contain comedy and find the number of it
print(len(genre[genre.str.contains('Children') & genre.str.contains('Animation')])) ## ## subset strings which contain children's and animation and find the number of it


"""
2.

Action = 503
Comedy = 1200
Children's and Animation = 84

"""


## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 

hrdf = mvdf[mvdf['Genre'] == 'Horror'] ## pull out Horror dataframe
lowtitle = hrdf['Title'].str.lower() ## lowercase
print(len(lowtitle[lowtitle.str.contains('massacre')])/len(hrdf)*100) ## find the number of the words and divide by total length and find the percentage
print(len(lowtitle[lowtitle.str.contains('texas')])/len(hrdf)*100) ## find the number of the words and divide by total length and find the percentage

hrdf = mvdf[mvdf['Genre'].str.contains('Horror')] ## pull out Horror dataframe
lowtitle = hrdf['Title'].str.lower() ## lowercase
print(len(lowtitle[lowtitle.str.contains('massacre')])/len(hrdf)*100) ## find the number of the words and divide by total length and find the percentage
print(len(lowtitle[lowtitle.str.contains('texas')])/len(hrdf)*100) ## find the number of the words and divide by total length and find the percentage

"""
3.

The question was kind of ambiguous, so I found two ways of anwers

First answer: ONLY Horror
massacre = 5.056179775280898%
texas = 2.247191011235955%

Second answer: Horror with other genres
massacre = 2.623906705539359
texas = 1.1661807580174928
"""


## 4.  How many titles are exactly one word?

titles = mvdf['Title'] ## subset title
tdf = titles.str.split(" ").str.len().to_frame() ## split by space and find each word's length and make it as dataframe
trues = tdf['Title'] <= 2 ## find the trues
print(np.sum(trues)) ## sum up all the trues

"""
4.

690

"""

## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.

## works
mvdf[~mvdf.Genre.str.contains('\|')] ## put \ this sign because of regex problem

## this works too
onedf = mvdf[~mvdf['Genre'].str.contains('\|')] ## create a new dataframe without rows which contain |
onegens = onedf['Genre'].groupby(onedf['Genre']) ## group by Genre
top3 = onegens.count().sort_values(ascending = False)[:3] ## count genre and sort values for the top3
print(top3) ## print top3

"""
5.

Genre
Drama     843
Comedy    521
Horror    178

"""

## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.

mvdf['#gens'] = mvdf['Genre'].str.split('|').str.len() ## split genres and count the number of strings in each row and put it intto the og dataframe as a new column
print(mvdf) ## check
groups = mvdf['#gens'].groupby(mvdf['#gens']) ## group by #gens to count it 
print(groups.count()) ## count them and print
mvdf[mvdf['#gens'] == 6] ## just check my answer
          
"""
6.

#gens count
0        0 (I included 0 because the question asked to determine # of movies with 0 genres)
1     2025
2     1322
3      421
4      100
5       14
6        1

"""

## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)

## remove the last string in the title
## create new column and make it as a dataframe

mvdf['Title'] = mvdf['Title'].str[:-6]  ## drop the years
remakes = mvdf['Title'].groupby(mvdf['Title']) ## group by Title
remake = remakes.count().sort_values() > 1 ## count them and sort values to check and find if the name is repeated
print(np.sum(remake)) ## sum up TRUE values and print

"""
7.

38

"""

## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

#############################################this method is using loop but I didn't use this#################
comgens = mvdf['Genre'].str.split('|')
emplist = [0] 
for i in comgens: 
    splt = i.split('|') 
    for j in splt: 
        emplist.append(j) 

empsrs = pd.Series(emplist)
top5 = empsrs.value_counts()[:5]
print(100*top5/len(mvdf))
###################################THIS ONE IS MY ANSWER#####################################################
one = mvdf[mvdf['#gens'] == 1]
two = mvdf[mvdf['#gens'] == 2]
three = mvdf[mvdf['#gens'] == 3]
four = mvdf[mvdf['#gens'] == 4]          
five = mvdf[mvdf['#gens'] == 5]          
six = mvdf[mvdf['#gens'] == 6]          

## one genre
list0 = one['Genre'].tolist()                
## create list for two genres
list1 = two.Genre.apply(lambda x: x.split("|")[-1]).tolist()
list2 = two.Genre.apply(lambda x: x.split("|")[-2]).tolist()                
type(list1)          
## create list for three genres
list3 = three.Genre.apply(lambda x: x.split("|")[-1]).tolist()
list4 = three.Genre.apply(lambda x: x.split("|")[-2]).tolist()
list5 = three.Genre.apply(lambda x: x.split("|")[-3]).tolist()
## for four
list6 = four.Genre.apply(lambda x: x.split("|")[-1]).tolist()
list7 = four.Genre.apply(lambda x: x.split("|")[-2]).tolist()
list8 = four.Genre.apply(lambda x: x.split("|")[-3]).tolist()
list9 = four.Genre.apply(lambda x: x.split("|")[-4]).tolist()
## for five
list10 = five.Genre.apply(lambda x: x.split("|")[-1]).tolist()
list11 = five.Genre.apply(lambda x: x.split("|")[-2]).tolist()
list12 = five.Genre.apply(lambda x: x.split("|")[-3]).tolist()
list13 = five.Genre.apply(lambda x: x.split("|")[-4]).tolist()
list14 = five.Genre.apply(lambda x: x.split("|")[-5]).tolist()
## for six
list15 = six.Genre.apply(lambda x: x.split("|")[-1]).tolist()
list16 = six.Genre.apply(lambda x: x.split("|")[-2]).tolist()
list17 = six.Genre.apply(lambda x: x.split("|")[-3]).tolist()
list18 = six.Genre.apply(lambda x: x.split("|")[-4]).tolist()
list19 = six.Genre.apply(lambda x: x.split("|")[-5]).tolist()
list20 = six.Genre.apply(lambda x: x.split("|")[-6]).tolist()

totlist = list0 + list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14 + list15 + list16 + list17 + list18 + list19 + list20
print(100*pd.Series(totlist).value_counts()[:5]/len(mvdf))

#######WOW THIS IS AWESOME THAT I FOUND##########

divgen = mvdf['Genre'].str.replace('\|', " ") ## subset genre and decompose by |
divgendf = divgen.to_frame() ## make it as a dataframe
divgensrs = pd.Series(' '.join(divgendf['Genre']).lower().split()).value_counts()[:5] ## make it as series and find only top5 genres
print(100*divgensrs/len(mvdf)) ## find the percentage

"""
8.

Genre      Percentage
Drama       41.282514
Comedy      30.903940
Action      12.953902
Thriller    12.670616
Romance     12.129797

"""


## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.

####################code1######################################################
mvdf['Title'] = mvdf['Title'].str[:-6]  ## drop the years
rom = mvdf[mvdf['Genre'].str.contains('Romance')] ## create dataframe which contains romance in Genre
lowttl = rom['Title'].str.lower() ## change all the strings to lowercase
lowttl = lowttl.str.replace(' the ', ' ').str.replace(' of ', ' ').str.replace(' a ', ' ').str.replace(' and ', ' ').replace('\!', '', regex=True).replace('\.', '', regex=True).replace(',', '', regex=True).replace('\(', '', regex=True).replace('\)', '', regex=True)
lodf = lowttl.to_frame() ## use replace function to remove unwanted words
lowttl.value_counts()
print(lodf) ## check
pd.Series(' '.join(lodf['Title']).lower().split()).value_counts()[:5] ## use joinfunction to look at substring and count each words frequency and extract only top 5 

####################code2######################################################
mvdf['Title'] = mvdf['Title'].str[:-6]  ## drop the years
rom = mvdf[mvdf['Genre'].str.contains('Romance')] ## create dataframe which contains romance in Genre
lowttl = rom['Title'].str.lower() ## change all the strings to lowercase
lowttl = lowttl.str.replace(' the ', ' ').str.replace(' of ', ' ').str.replace(' a ', ' ').str.replace(' and ', ' ')
lodf = lowttl.to_frame() ## use replace function to remove unwanted words
lowttl.value_counts()
print(lodf) ## check
pd.Series(' '.join(lodf['Title']).lower().split()).value_counts()[:5] ## use joinfunction to look at substring and count each words frequency and extract only top 5 

"""
9.

I found the answer more exactly to answer the question, but later I realized that Professor Holt said that we can ignore these words such as "love)" and "you,".
    
This is more exact answer
words    count
in       27
love     24
to       14
you      12
on       10

This is the answer when I ignore these words such as "love)" and "you,"
in      27
love    21
to      14
on      10
you     10
"""

## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.

mudf = mvdf[mvdf['Genre'].astype(str).str.contains('Musical')] ## subset if genre is Musical as dataframe
myear = mudf['Title'].str[-5:].str[:-1] ## leave only year
numyear = pd.to_numeric(myear) ## change it into numeric
mumu = np.sum(numyear)/len(myear) ## find the mean
print(mumu) ## print
medmu = np.median(numyear) ## find the median
print(medmu) ## print

othersdf = mvdf[~mvdf['Genre'].astype(str).str.contains('Musical')] ## subset if genre is not Musical as datafrane
othyear = othersdf['Title'].str[-5:].str[:-1] ## leave only year
numothyear = pd.to_numeric(othyear) ## change it into numeric
muoth = np.sum(numothyear)/len(othyear) ## find the mean
print(muoth) ## print
medoth = np.median(numothyear) ## find the median
print(medoth) ## print


"""
10.

1968.7456140350878 -> mean of movies year released genre is musical
1967.0             -> median of movies year released genre is musical  
1986.5908729105863 -> mean of movies year release genre except musical
1994.0             -> median of movies year released genre except musical

"""





