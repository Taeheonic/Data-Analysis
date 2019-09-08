##
## File: assignment07.py (STAT 3250)
## Topic: Assignment 7 
##

##  This assignment requires data from four files: 
##
##      'movies.txt':  A file of over 3900 movies
##      'users.dat':   A file of over 6000 reviewers who provided ratings
##      'ratings.dat': A file of over 1,000,000 movie ratings
##      'zips.txt':    A file of zip codes and location information
##
##  The file 'readme.txt' has more information about the first three files.
##  You will need to consult the readme file to answer some of the questions.

##  Note: You will need to convert the zip code information in 'users.dat' into
##  state (or territory) information for one or more of the questions below.
##  You must use the information in 'zips.txt' for this purpose, you cannot
##  use other conversion methods. 

## 1.  Determine the percentage of users that are female.  Do the same for the
##     percentage of users in the 35-44 age group.  In the 18-24 age group,
##     determine the percentage of male users.

import pandas as pd
import numpy as np    
open('users.dat', encoding="utf8").read().splitlines() ## open dat file
udf = pd.read_csv('users.dat', sep='::',header=None, names = ['UserID', 'Gender', 'Age', 'Occupation', 'Zipcode']) ## read text as dataframe

fem = udf[udf['Gender'] == 'F'] ## subset female df
totfem = fem['Gender'].count() ## count
femperc = (totfem/len(udf)*100) ## find the percentage of female
print(femperc) ## print

ag35 = udf[udf['Age'] == 35] ## subset age == 35
femag35 = ag35[ag35['Gender'] == 'F'] ## subset female
len(femag35) ## length
ag35perc = (len(femag35)/len(ag35)*100) ## find the percentage in the 30-44 age
print(ag35perc) ## print

ag18 = udf[udf['Age'] == 18] ## subset age == 18
mag18 = ag18[ag18['Gender'] == 'M'] ## subset male
len(mag18) ## length
ag18perc = (len(mag18)/len(ag18)*100) ## find the percentage in the 18-24 age
print(ag18perc) ## print


"""
1.

28.294701986754966% -> female users percentage

28.331936295054483% -> female users percentage in the 35-44 age group

72.98277425203989% -> male users percentage in the 18-24 age group

"""

## 2.  Give a year-by-year table of counts for the number of ratings, sorted by
##     year in ascending order.

import datetime
open('ratings.dat', encoding="utf8").read().splitlines() ## open rating data
rdf = pd.read_csv('ratings.dat', sep='::',header=None, names=['UserID','MovieID','Rating','Timestamp'])
## read rating data as csv
rdf['Timestamp'] = pd.to_datetime(rdf['Timestamp'], unit='s') ## by using pd.to_datetime read it as second
rdf['Timestamp'] = rdf['Timestamp'].dt.year ## subset year
times = rdf['Rating'].groupby(rdf['Timestamp']).count().sort_index(ascending=False) ## groupby year and counts for number of ratings
print(times) ## print



"""
2.

Timestamp
2003      3348
2002     24046
2001     68058
2000    904757

"""

## 3.  Determine the average rating for females and the average rating for 
##     males.

merge3 = pd.merge(udf, rdf, on='UserID', how='outer') ## merge user and rating data
merge3['Rating'].groupby(merge3['UserID']) ## groupby userID with rating

femm = merge3[merge3['Gender'] == 'F'] ## subset female
femm['Rating'].mean() ## ind the mean of rating 

mem = merge3[merge3['Gender'] == 'M'] ## subset male
mem['Rating'].mean() ## find the mean of rating


"""
3.

3.6203660120110372 -> female avg rating
3.5688785290984373 -> male avg rating
    
"""


## 4.  Find the top-10 movies based on average rating.  (Movies and remakes 
##     should be considered different.)  Give a table with the movie title
##     (including the year) and the average rating, sorted by rating from
##     highest to lowest.  (Include ties as needed.)


g2 = rdf['Rating'].groupby(rdf['UserID']).sum() ## groupby userid with rating and sum
g3 = rdf['Rating'].groupby(rdf['UserID']).count() ## groupby userid with rating and count
avgrating = g2/g3 ## 
adf = avgrating.to_frame()
concadf = pd.merge(udf, adf, on='UserID')

############this one i used################
open('movies.txt', encoding="utf8").read().splitlines() ## open text file
mvdf = pd.read_csv('movies.txt', sep='::',header=None, names=['MovieID','Title','Genre']) ## read text as dataframe 

g4 = rdf['Rating'].groupby(rdf['MovieID']).sum() ## groupby userid with rating and sum
g5 = rdf['Rating'].groupby(rdf['MovieID']).count() # groupby userid with rating and count
avgrating2 = g4/g5 ## find the avg
adf2 = avgrating2.to_frame() ## to frame
concadf2 = pd.merge(mvdf, adf2, on='MovieID') ## merge with movie data
concadf2 ## conca datAFRAME

top10 = concadf2['Rating'].groupby(concadf2['Title']) ## groupby title with rating
top10.sum().sort_values(ascending=False)[:10] ## find the top-10
############this one i used################

ratmerge = pd.merge(mvdf, rdf, on='MovieID', how='outer')
ratmerge['Rating'].groupby(ratmerge['MovieID']).mean()


"""
4.

Title
Gate of Heavenly Peace, The (1995)           5.0
Lured (1947)                                 5.0
Ulysses (Ulisse) (1954)                      5.0
Smashing Time (1967)                         5.0
Follow the Bitch (1998)                      5.0
Song of Freedom (1936)                       5.0
Bittersweet Motel (2000)                     5.0
Baby, The (1973)                             5.0
One Little Indian (1973)                     5.0
Schlafes Bruder (Brother of Sleep) (1995)    5.0

"""
## 5.  Determine the number of movies listed in 'movies.txt' for which there
##     is no rating.  Determine the percentage of these unrated movies for
##     which there is a more recent remake.

ratmerge = pd.merge(mvdf, rdf, on='MovieID', how='outer') ## merge movie with rating
rats = ratmerge['Rating'] ## subset rating
norats = rats.isna().sum() ## find if nan

ratmerge['TF'] = rats.isna() ## put as a column
rattrue = ratmerge[ratmerge['TF'] == True] ## subset if its true
rattrue['Title'] = rattrue['Title'].str[0:-7] ## cut the year
ratct = rattrue['MovieID'].groupby(rattrue['Title']).count() ## count using groupby
remake = ratct[ratct>1] ## if there is 2 or more it is remake 
perc = len(remake)/len(ratmerge)*100 ## find the percentage 
print(perc, '%') ## print


"""
5.

no rating = 177
the percentage of these unrated movies for which there is a more recent remake 0.0 %

"""

## 6.  Determine the average rating for each occupation classification 
##     (including 'other or not specified'), and give the results in a
##     table sorted from highest to lowest average and including the
##     occupation title.

readme = pd.Series(open('readme.txt').read().splitlines()) ## read readme
temp = readme[70:89].str.split(':') ## bring the lines for occupation

g6 = merge3['Rating'].groupby(merge3['Occupation']).mean().astype(float) ## groupby occupation with rating find the mean 

open('readme.txt', encoding="utf8").read().splitlines() ## read readme
occu = pd.read_csv('readme.txt', sep=':', header=None, names=['Occupation', 'Name']) ##change itto csv
occu1 = occu[51:72] ## bring the occupation line
occudf = pd.concat([occu1['Name'].reset_index(drop=True), g6.reset_index(drop=True)], axis=1) ## use concate and put the name instead of occupation number
occudf.sort_values(ascending=False, by='Rating') ## sort values and get table


"""
6.

                          Name    Rating
13                   "retired"  3.781736
15                 "scientist"  3.689774
6         "doctor/health care"  3.661578
9                  "homemaker"  3.656589
3             "clerical/admin"  3.656516
12                "programmer"  3.654001
14           "sales/marketing"  3.618481
11                    "lawyer"  3.617371
17       "technician/engineer"  3.613574
7       "executive/managerial"  3.599772
16             "self-employed"  3.596575
1          "academic/educator"  3.576642
2                     "artist"  3.573081
0     "other" or not specified  3.537544
5           "customer service"  3.537529
4       "college/grad student"  3.536793
10              "K-12 student"  3.532675
18       "tradesman/craftsman"  3.530117
20                    "writer"  3.497392
8                     "farmer"  3.466741
19                "unemployed"  3.414050

"""

## 7.  Determine the average rating for each genre, and give the results in
##     a table listing genre and average rating in descending order.

ratmerge = pd.merge(mvdf, rdf, on='MovieID', how='outer') ## merge movie with rating
## make a list with movie name
mvlist = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
emplist = [] ## empty list
for i in mvlist: ## use for loop to get the table
    temp = ratmerge[ratmerge['Genre'].str.contains(i)]
    rat = temp['Rating'].mean() ## find the mean
    emplist.append(rat)    
print(emplist) ## print empty list

mvsrs = pd.Series(mvlist) 
empsrs = pd.Series(emplist)        
pd.concat([mvsrs.rename('movie'), empsrs.rename('rating')], axis=1).sort_values(ascending=False, by='rating') ## concatenate and sortvalues 

"""
7. 

          movie    rating
9     Film-Noir  4.075188
6   Documentary  3.933123
16          War  3.893327
7         Drama  3.766332
5         Crime  3.708679
2     Animation  3.684868
12      Mystery  3.668102
11      Musical  3.665519
17      Western  3.637770
13      Romance  3.607465
15     Thriller  3.570466
4        Comedy  3.522099
0        Action  3.491185
1     Adventure  3.477257
14       Sci-Fi  3.466521
8       Fantasy  3.447371
3      Children  3.422035
10       Horror  3.215013

"""
## 8.  For the user age category, assume that the user has age at the midpoint
##     of the given range.  (For instance '35-44' has age (35+44)/2 = 39.5)
##     For 'under 18' assume an age of 16, and for '56+' assume an age of 60.
##     For each possible rating (1-5) determine the average age of the raters.

def agerange(x): # age range function
        if x == 1: # return the number if the condition is fulfilled
            return (16)
        elif x== 25:
            return (42)
        elif x== 35:
            return (39.5)
        elif x== 45:
            return (47)
        elif x== 50:
            return (52.5)
        elif x== 56:
            return (60)
    
concadf3 = pd.merge(udf, rdf, on='UserID', how='outer') ##merge user data and rating data
concadf3['midage'] = concadf3['Age'].apply(agerange) ## create midage column in the df and put the result from my defenition use apply
ageofrat = concadf3['midage'].groupby(concadf3['Rating']) ## groupby rating with midage
ageofrat.mean() ## find the average age of the raters

"""
8.

Rating     Age
1    41.885447
2    42.361927
3    42.805336
4    42.963296
5    43.056285

-> the avg age of the raters
"""

## 9.  Find all combinations (if there are any) of occupation and genre for 
##     which there are no ratings.  

concadf4 = pd.merge(udf, rdf, on='UserID', how='outer') ##merge user and rating dagt
concadf5 = pd.merge(concadf4, mvdf, on='MovieID', how='outer') ## merge the merged data and movie data

noratdata = concadf5[concadf5['Rating'].isna()] ##subset in there is nan
unqnorat = noratdata.drop_duplicates(subset='Genre', keep='first', inplace=False) ## for the genre drop duplicates
pd.concat([unqnorat['Genre'], unqnorat['Occupation']], axis=1) ##use pd.concat to concatenate genre and occupation and see if there is any combination

"""
9.

No combination -> The table doesn't give me any combination because occupation is nan.

"""

## 10. For each age group, determine the occupation that gave the lowest 
##     average rating.  Give a table that includes the age group, occupation,
##     and average rating.  (Sort by age group from youngest to oldest) 

## subset age group -> find the lowest rating of occupation

merge3 = pd.merge(udf, rdf, on='UserID', how='outer') ##merge user data and rating data

age1 = merge3[merge3['Age'] == 1] ##subset if age is 1 as a dataframe
age2 = merge3[merge3['Age'] == 18] ##subset if age is 18 as a dataframe
age3 = merge3[merge3['Age'] == 25] ##subset if age is 25 as a dataframe
age4 = merge3[merge3['Age'] == 35] ##subset if age is 35 as a dataframe
age5 = merge3[merge3['Age'] == 45] ##subset if age is 45 as a dataframe
age6 = merge3[merge3['Age'] == 50] ##subset if age is 50 as a dataframe
age7 = merge3[merge3['Age'] == 56] ##subset if age is 56 as a dataframe

age11 = age1.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a1 = age11[['Occupation','Rating']].groupby(age11['Occupation']).mean().sort_values(ascending=True, by='Rating').head(1) 
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age22 = age2.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a2 = age22[['Occupation','Rating']].groupby(age22['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age33 = age3.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a3 = age33[['Occupation','Rating']].groupby(age33['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age44 = age4.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a4 = age44[['Occupation','Rating']].groupby(age44['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age55 = age5.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a5 = age55[['Occupation','Rating']].groupby(age55['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age66 = age6.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a6 = age66[['Occupation','Rating']].groupby(age66['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
age77 = age7.loc[:,'Occupation':'Rating'] ##subset columns from occupation to rating
a7 = age77[['Occupation','Rating']].groupby(age77['Occupation']).mean().sort_values(ascending=True,by='Rating').head(1)
##groupby occupation and subset occupation and rating after finding mean subset the lowest rating
a10 = a1.append(a2).append(a3).append(a4).append(a5).append(a6).append(a7) ## append all the results
a1010 = a10.set_index([pd.Index([1, 18, 25, 35, 45, 50, 56])]) ## put age as an index
occupations = ['lawyer', 'farmer', 'unemployed', 'farmer', 'college/grad student', 'tradesman/craftsman', 'K-12 student']
##replace occupation number into name
a1010['Occupation'] = occupations
print(a1010) ##print table

"""
10.

Age           Occupation    Rating
1                 lawyer  3.066667
18                farmer  3.235525
25            unemployed  3.366426
35                farmer  2.642045
45  college/grad student  3.280000
50   tradesman/craftsman  3.437610
56          K-12 student  3.291755

"""

## 11. Find the top-5 states in terms of average rating.  Give in table form
##     including the state and average rating, sorted from highest to lowest.
##     Note: If any of the zip codes in 'users.dat' includes letters, then we
##     classify that user as being from Canada, which we treat as a state for
##     this and the next question.

zipcode = pd.read_csv('zipcodes.txt') ##read zipcode data

merged11=pd.merge(rdf, udf, on=['UserID'], how='outer') ##merge ratings and users data on UserID
states = zipcode[zipcode["Zipcode"].astype(str).str.contains('[a-zA-Z]') == False] ##subset states data with only us states (us zipcodes)
merged11["Zipcode"] = merged11["Zipcode"].str.split("-").str[0].astype(int) ##split zipcode by - and get only first string
merged111 = pd.merge(merged11, states, on=['Zipcode'], how='inner') ## merge us zipcodes data and merged data on zipcode
trimmed = merged111[(merged111["Zipcode"] > 9999) & (merged111["Zipcode"] < 100000)] ##5digit zip code and  contain only 5 digit zipcode
top5 = trimmed["Rating"].groupby(trimmed["State"]).mean().sort_values(ascending=False)[0:5] ##group ratings by state and find the mean and sort values descending order and find top5 
print(top5) ##print top 5


"""
11.

GU    4.236842
AK    4.008094
AP    3.938967
MS    3.913241
IN    3.820510

"""

## 12. For each genre, determine which state produced the most reviews.  
##     (Include any ties.)

udf['Zipcode'] = udf['Zipcode'].str.split('-').str[0].astype(int) ##split zipcode by -
merge3 = pd.merge(udf, rdf, on='UserID', how='outer') ##merge user data and rating data
urmv = pd.merge(merge3, mvdf, on='MovieID', how='outer') ## merge movie data and the merged data above
finalmerge = pd.merge(zipcode, urmv, on='Zipcode', how='inner') ##finally merge zipcode data with the merged one above

genlist = mvdf['Genre'].str.split('|') ##split genre by |
lists=np.unique(sum(genlist,[])) ##make unique genre list
empty = [] ## empty set
for i in lists.tolist(): #for each genre list
    data=finalmerge[finalmerge['Genre'].str.contains(i)] ##subset each genre
    state=data['Rating'].groupby(data['State']).count() ##group ratings by state and count
    reviews=state.sort_values(ascending=False).head(1).reset_index() ##sort and subset the largest value
    table=[i,reviews["State"][0], reviews["Rating"][0]] ##make a table
    empty.append(table) ##append to empty list
table7=pd.DataFrame(empty, columns=['Genre','State','Reviews']) ## put headings above each column
print(table7) ##print the result




"""
12.

          Genre State  Reviews
0        Action    CA    82536
1     Adventure    CA    42273
2     Animation    CA    13587
3    Children's    CA    21920
4        Comedy    CA   109518
5         Crime    CA    25736
6   Documentary    CA     2797
7         Drama    CA   111456
8       Fantasy    CA    10898
9     Film-Noir    CA     6239
10       Horror    CA    23253
11      Musical    CA    12697
12      Mystery    CA    13192
13      Romance    CA    45406
14       Sci-Fi    CA    50330
15     Thriller    CA    61704
16          War    CA    20989
17      Western    CA     6397

"""