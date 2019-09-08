##
## File: assignment09.py (STAT 3250)
## Topic: Assignment 9 
##

##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.

## 1.  Find all schools that have won the championship, and make a table that
##     incluldes the school and number of championships, sorted from most to
##     least.

import numpy as np
import pandas as pd
ncaa = pd.read_csv("ncaa.csv") ## read csv file
champ = ncaa[ncaa['Region Name'] == 'Championship'] ## subset championship dataframe
ch1 = champ[champ['Score'] > champ['Score.1']] ## subset dataframe if score is greater than score.1
ch1s = ch1['Team'] ## subset Team
ch2 = champ[champ['Score'] < champ['Score.1']] ## subset dataframe if score is less than score.1
ch2s = ch2['Team.1'] ## subset Team.1
table1 = pd.concat([ch1s, ch2s]).value_counts() ## concatenate two series and count values


"""
1.

Duke              5
North Carolina    4
Connecticut       4
Villanova         3
Kentucky          3
Louisville        2
Kansas            2
Florida           2
Syracuse          1
Arkansas          1
Arizona           1
Michigan St       1
Virginia          1
UNLV              1
Michigan          1
Indiana           1
UCLA              1
Maryland          1

"""


## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.

first = ncaa[ncaa['Round'] == 1] ## subset dataframe as a round 1
tour = first['Team'] ## subset Team name 
tour1 = first['Team.1'] ## subset Team.1 name
pd.concat([tour, tour1]).value_counts()[:11] ## concatenate two series and find the top10 schools

"""
2.

Kansas            34
Duke              34
Arizona           32
North Carolina    32
Kentucky          30
Michigan St       29
Syracuse          28
Louisville        26
Purdue            26
Oklahoma          26
Texas             26

"""
## 3.  Determine the average tournament seed for each school, then make a
##     table with the 10 schools that have the lowest average (hence the
##     best teams). Sort the table from smallest to largest, and include
##     all that tie for 10th position if necessary.

first = ncaa[ncaa['Round'] == 1] ## subset round 1 as a dataframe
s1 = first['Seed'].append(first['Seed.1']) #combine seed and seed.1
t1 = first['Team'].append(first['Team.1']) #combine team and team.1
stdf=pd.DataFrame({'Seed':s1, 'Team':t1}) ## make as dataframe with two subset
print(stdf['Seed'].groupby(stdf['Team']).mean().sort_values(ascending=True)[0:10]) ## group seed by team and find the mean and print top 10 



"""
3.

Team
Duke               2.176471
Kansas             2.500000
North Carolina     2.718750
Kentucky           3.566667
Connecticut        3.950000
Loyola Illinois    4.000000
Massachusetts      4.375000
Syracuse           4.428571
Arizona            4.437500
Ohio St            4.450000

"""
## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....

ncaa['margin'] = abs(ncaa['Score'] - ncaa['Score.1']) ## create a column which has margin
ncaa['margin'].groupby(ncaa['Round']).mean() ##groupby round with margin and get the mean

"""
4.

Round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143

"""

## 5.  Give a table of the percentage of wins by the higher seed by round,
##     sorted by round in order 1, 2, 3, ...

sd1 = ncaa[ncaa['Seed'] > ncaa['Seed.1']] ## subset dataframe where Seed is greater than Seed.1
sc1 = sd1[sd1['Score'] < sd1['Score.1']] ## subset dataframe which contains Score is less than Score.1
ct1 = sc1['Team'].groupby(sc1['Round']).count() ## groupby Round with Team and count

sd2 = ncaa[ncaa['Seed'] < ncaa['Seed.1']] ## subset dataframe where Seed.1 is greater than Seed.
sc2 = sd2[sd2['Score'] > sd2['Score.1']] ## suvset dataframe which contains Score is greater than Score.1
ct2 = sc2['Team'].groupby(sc2['Round']).count()## groupby Round with Team and count

table5 = pd.concat([ct1, ct2], axis=1).sum(axis=1) ## concatenate two series and find the sum
allround = ncaa['Team'].groupby(ncaa['Round']).count() ## from the whole data use groupby Round with Team and count

print(100*table5/allround) ## calculate the percentage of wins by the higher seed by round

"""
5. 

Round
1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    48.571429
6    57.142857

"""

## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.

f4 = ncaa[ncaa['Region Name'] == 'Final Four'] ## subset dataframe if Region Name is Final Four
s1yr = f4['Seed'].groupby(f4['Year']).mean() ## groupby Year with Seed and find the mean
s2yr = f4['Seed.1'].groupby(f4['Year']).mean() ## groupby Year with Seed.1 and find the mean 
pd.concat([s1yr, s2yr], axis=1).mean(axis=1).sort_values(ascending=True)[:5] ## concatenate two series and get mean and find the top5

"""
6.

Year
2008    1.00
1993    1.25
2007    1.50
2001    1.75
1999    1.75

"""
## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.


first = ncaa[ncaa['Round'] == 1] ## subset round 1 as a dataframe
hiseed = first[first['Seed'] < first['Seed.1']] ## subset if Seed.1 is greater than Seed
hiscore = hiseed[hiseed['Score'] > hiseed['Score.1']] ## Subset if Score is greater than Score.1
seedct = hiscore['Team'].groupby(hiscore['Seed']).count() ## groupby Seed with Team and count
totseed = first['Team'].groupby(first['Seed']).count() ## from the first round dataframe groupby Seed with Team
table = 100*seedct/totseed ## find the percentage of wins by the higher seed
table7 = table.to_frame() ## make is as a datafrmae 
table7.set_index([pd.Index(['1-16', '2-15', '3-14', '4-13', '5-12', '6-11', '7-10', '8-9'])]) ## put the games as index

"""
7.

Games      Team
1-16  99.285714
2-15  94.285714
3-14  85.000000
4-13  79.285714
5-12  64.285714
6-11  62.857143
7-10  60.714286
8-9   48.571429

"""
## 8.  For each champion, determine the average margin of victory in all
##     games played by that team.  Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.


######

def champion(ncaa): ## function for determine champion
    if ncaa['Score'] > ncaa['Score.1']:
        return ncaa['Team']
    else:
        return ncaa['Team.1']

final = ncaa[ncaa['Round']==6] ##subset final round
final['Champion']='' ##created an empty column
final['Champion']=final.apply(champion, axis =1) ## put values in the champion column using apply function
merge8 = pd.merge(ncaa, final, on='Year', how='inner') ## merge two dataframe on Year as inner
champ = merge8[(merge8['Team_x'] == merge8.Champion) | (merge8['Team.1_x'] == merge8.Champion)] ## Subset dataframe if Team_x and Team.1_x are champion
table8 = champ['margin_x'].groupby([champ['Champion'], champ['Year']]).mean().sort_values(ascending = False) ## groupby champion with margin and get avg margin and get top10
table8[:10]

"""
8.

Champion        Year
Kentucky        1996    21.500000
Villanova       2016    20.666667
North Carolina  2009    20.166667
UNLV            1990    18.666667
Villanova       2018    17.666667
Duke            2001    16.666667
Louisville      2013    16.166667
Florida         2006    16.000000
North Carolina  1993    15.666667
Duke            2015    15.500000
"""

## 9.  For each champion, determine the average seed of all opponents of that
##     team.  Make a table of top-10 in terms of average seed, sorted from 
##     highest to lowest.  Include all that tie for 10th position if necessary.
##     Then make a table of the bottom-10, sorted from lowest to highest.
##     Again include all that tie for 10th position if necessary. 


def opps(ncaa): ## function for determine champion
    if ncaa['Score'] > ncaa['Score.1']:
        return ncaa['Seed.1']
    else:
        return ncaa['Seed']
ncaa['Oppseed']='' ## create empty column
ncaa['Oppseed']=ncaa.apply(opps, axis=1) ## put values into that column using apply function
final['Oppseed']='' ##created an empty column  
final['Oppseed']=final.apply(opps, axis =1) ## put values into that column using apply function
merge9 = pd.merge(ncaa, final, on='Year', how='inner') ## merge two dataframe on year as inner
cham = merge9[(merge9['Team_x'] == merge9.Champion) | (merge9['Team.1_x'] == merge9.Champion)] ## Subset dataframe if Team_x and Team.1_x are champion
cham['Oppseed_x'].groupby([cham['Champion'], champ['Year']]).mean().sort_values(ascending = False)[:11] ## groupby champion with seed# of opposite team and get means and get top10  
cham['Oppseed_x'].groupby([cham['Champion'], champ['Year']]).mean().sort_values(ascending = True)[:11] ## groupby champion with seed# of opposite team and get means and get bottom10  
"""
9.

Champion        Year
UNLV            1990    9.000000
Louisville      2013    8.500000
Virginia        2019    8.000000
Kansas          2008    8.000000
Florida         2006    7.666667
Connecticut     1999    7.500000
Louisville      1986    7.500000
Arkansas        1994    7.333333
Michigan St     2000    7.166667
Indiana         1987    7.000000
North Carolina  2005    7.000000 -> top11

Champion        Year
Villanova       1985    3.333333
Connecticut     2014    4.666667
Villanova       2016    4.833333
North Carolina  1993    5.500000
Syracuse        2003    5.666667
North Carolina  2017    5.666667
North Carolina  2009    5.833333
Michigan        1989    6.000000
Maryland        2002    6.000000
Florida         2007    6.000000
Kentucky        1996    6.000000 -> bot11

"""



## 10. Determine the 2019 champion.


champs = ncaa[ncaa['Year'] == 2019] ## subset 2019 dataframe
champion = champs[champs['Region Name'] == 'Championship'] ## subset championship dataframe
winner = champion[champion['Score'] > champion['Score.1']] ## subset dataframe if Score is greater than Score.1
winner['Team'] ## subset Team

winner1 = champion[champion['Score'] < champion['Score.1']] ## subset dataframe if Score.1 is greater than Score
winner1['Team.1'] ## subset Team.1

pd.concat([winner['Team'], winner1['Team.1']]) ## concatenate Team and Team.1 to check who is the winner 
"""
10.

2204    Virginia

"""