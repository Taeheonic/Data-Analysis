##
## File: assignment05.py (STAT 3250)
## Topic: Assignment 5
##

##  This assignment requires the data file 'diabetic_data.csv'.  This file
##  contains records for over 100,000 hospitalizations for people who have
##  diabetes.  The file 'diabetic_info.csv' contains information on the
##  codes used for a few of the entries.  Missing values are indicated by
##  a '?'.  You should be able to read in this file using the usual 
##  pandas methods.

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

## 1.  Determine the average number of medications ('num_medications') for 
##     males and for females.

import numpy as np
import pandas as pd
dd = pd.read_csv('diabetic_data.csv')

maledf = dd[dd['gender'] == 'Male'] ## dataframe for only male
malemeds = maledf['num_medications'] ## subset number of medications
malemeds_avg = np.sum(malemeds)/len(malemeds) ## find the avg number of medications

femaledf = dd[dd['gender'] == 'Female'] ## dataframe for only female
femalemeds = femaledf['num_medications'] ## subset number of medications
femalemeds_avg = np.sum(femalemeds)/len(femalemeds) ## find the avg number of medicatons

print(malemeds_avg) ## print the answer for male
print(femalemeds_avg)  ## print the answer for female

"""
1.

avg number of meds for male =   15.828774837955583
avg number of meds for female = 16.187888425824376

"""


## 2.  Determine the average length of hospital stay ('time_in_hospital')
##     for each race classification.  (Omit those unknown '?' but include 
##     those classified as 'Other'.)

AAdf = dd[dd['race'] == 'AfricanAmerican'] ## dataframe for only AfricanAmerican
ASdf = dd[dd['race'] == 'Asian'] ## dataframe for only Asian
CCdf = dd[dd['race'] == 'Caucasian'] ## dataframe for only Caucasian
HPdf = dd[dd['race'] == 'Hispanic'] ## dataframe for only Hispanic
OTdf = dd[dd['race'] == 'Other'] ## dataframe for only Other 

AAstay = AAdf['time_in_hospital'] ## subset hospital stay
ASstay = ASdf['time_in_hospital'] ## subset hospital stay
CCstay = CCdf['time_in_hospital'] ## subset hospital stay
HPstay = HPdf['time_in_hospital'] ## subset hospital stay
OTstay = OTdf['time_in_hospital'] ## subset hospital stay

print(np.sum(AAstay)/len(AAstay)) ## print the answer for AfricanAmerican
print(np.sum(ASstay)/len(ASstay)) ## print the answer for Asian
print(np.sum(CCstay)/len(CCstay)) ## print the answer for Caucasian
print(np.sum(HPstay)/len(HPstay)) ## print the answer for Hispanic
print(np.sum(OTstay)/len(OTstay)) ## print the answer for Other

"""
2.

avg stay for AfricanAmerican = 4.507860489328475
avg stay for Asian =           3.995319812792512
avg stay for Caucasian =       4.385721231553634
avg stay for Hispanic =        4.059891998036328
avg stay for Other =           4.273572377158034

"""


## 3.  Among males, find a 95% confidence interval for the proportion that 
##     had at 2 or more procedures ('num_procedures').  Then do the same 
##     for females.

maledf = dd[dd['gender'] == 'Male'] ## subset gender and only male
n=len(maledf) ## the number of rows of the data frame for male
phat = np.sum(maledf['num_procedures']>=2)/n ## find the phat
lcl = phat - 1.96*np.sqrt(phat*(1-phat)/n) ## lower confidence level
ucl = phat + 1.96*np.sqrt(phat*(1-phat)/n) ## upper confidence level
print([lcl,ucl]) ## print confidence interval for men 

femaledf = dd[dd['gender'] == 'Female'] ## subset the dataframe for female
n=len(femaledf) ## length for female
phat = np.sum(femaledf['num_procedures']>=2)/n ## find the phat
lcl = phat - 1.96*np.sqrt(phat*(1-phat)/n) ## lower confidence level
ucl = phat + 1.96*np.sqrt(phat*(1-phat)/n) ## upper confidence level
print([lcl,ucl]) ## print confidence interval for women

"""
3.

[0.3551161035669802, 0.36378730733515563] -> male


[0.31516986803938, 0.32298177340245665] -> female

"""


## 4.  Among the patients in this data set, what percentage had more than
##     one recorded hospital visit?  (Each distinct record can be assumed 
##     to be for a distinct hospital visit.)


visit = dd.groupby("patient_nbr") ## make a group by patient_nbr
eachvisit = visit.size() ## find the each visitor's record
morethanone = eachvisit[eachvisit > 1] ## get patients more than one visit
perc = 100*len(morethanone)/len(eachvisit) # find a percentage
print(perc) # print the percentage


"""
4.

23.452837048015883

"""


## 5.  List the top-10 most common diagnoses, based on the codes listed in
##     the columns 'diag_1', 'diag_2', and 'diag_3'.

import collections
diagseries1 = dd['diag_1'] ## subset diag1
diagseries2 = dd['diag_2'] ## subset diag2
diagseries3 = dd['diag_3'] ## subset diag3
type(diagseries1) 
diag1 = diagseries1.tolist() ## change diag1 to list
diag2 = diagseries2.tolist() ## change diag2 to list 
diag3 = diagseries3.tolist() ## change diag3 to list 
totdiag = diag1 + diag2 + diag3 ## add all lists
counter = collections.Counter(totdiag) ## count
counter.most_common(10) ## most common 10

"""
5.
diagnoses number
[('428', 18101),
 ('250', 17861),
 ('276', 13816),
 ('414', 12895),
 ('401', 12371),
 ('427', 11757),
 ('599', 6824),
 ('496', 5990),
 ('403', 5693),
 ('486', 5455)]

"""

## 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
##     that the age for a person is the middle of the range.  (For instance,
##     those with 'age' [40,50) are assumed to be 45.)  Determine the average
##     age for each classification in 'insulin'.

def age(x): ## set up the age definition to divide the age group
    if x =='[0-10)':
        return (5)
    elif x== '[10-20)':
        return (15)
    elif x== '[20-30)':
        return (25)
    elif x== '[30-40)':
        return (35)
    elif x== '[40-50)':
        return (45)
    elif x== '[50-60)':
        return (55)
    elif x== '[60-70)':
        return (65)
    elif x== '[70-80)':
        return (75)
    elif x== '[80-90)':
        return (85)
    elif x== '[90-100)':
        return (95)
    
dd['mid_age']=dd['age'].apply(age) ## use apply function to create new column
insulin=dd['mid_age'].groupby(dd['insulin']) ## use groupby to make a group by insulin
print(insulin.mean()) ## find the mean of the insulin by age


""" 6
insulin
Down      63.300049
No        67.460165
Steady    65.571169
Up        63.673560
"""


## 7.  Among those whose weight range is given, assume that the actual
##     weight is at the midpoint of the given interval.  Determine the
##     average weight for those whose 'num_lab_procedures' exceeds 50,
##     then do the same for those that are fewer than 30.

def weights(x): ## create a definition weights assuming the actual weight is at the midpoint of the given interval
    if x =='[0-25)':
        return (12.5)
    elif x== '[25-50)':
        return (37.5)
    elif x== '[50-75)':
        return (62.5)
    elif x== '[75-100)':
        return (87.5)
    elif x== '[100-125)':
        return (112.5)
    elif x== '[125-150)':
        return (137.5)
    elif x== '[150-175)':
        return (162.5)
    elif x== '[175-200)':
        return (187.5)
    elif x== '>200':
        return (200)
    elif x== '?':
        pass

weight = dd['weight'].groupby(dd['weight']) ## use groupby to make a group by weight
weight.count() ## check to count by grouping
over50 = dd.loc[dd['num_lab_procedures']>50] ## subset weights over 50
less30 = dd.loc[dd['num_lab_procedures']<30] ## subset weights less 30
dd['avg>50'] = over50['weight'].apply(weights) ## create a column avg weight over 50 
dd['avg<30'] = less30['weight'].apply(weights) ## create a column avg weight less 30
over50mean = dd['avg>50'].mean() ## find the mean of avg weight over 50
less30mean = dd['avg<30'].mean() ## find the mean of avg weight less 30
print(over50mean) ## print
print(less30mean) ## print

""" 7
avg weight over 50 = 85.05018489170628
avg weight less 30 = 88.73546511627907
"""




## 8.  Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
##     and 'glyburide'.  There are columns in the data for each of these.
##     Determine the number of records for which at least two of these
##     are listed as 'Steady'.


threemed = dd['glipizide']+dd['glimepiride']+dd['glyburide'] ## add up three subset series
stead = threemed.str.count('Steady') >=2 ## find the two for more steady
print(np.sum(stead)) ## the number of records at least two of steady


""" 8
284
"""


## 9.  What percentage of reasons for admission ('admission_source_id')
##     correspond to some form of transfer from another care source?

tran = [4,5,6,10,18,22,25,26] ## create transfer array
another = dd['admission_source_id'].isin(tran).sum() ## find the tran values from the admission and sum up 
perc = another/len(dd['admission_source_id'])*100 ## make it as a percentage
print(perc) ## print the percentage

""" 9
6.218186820745633%
"""


## 10. The column 'discharge_disposition_id' gives codes for discharges.
##     Determine which codes (and the corresponding outcomes from the ID
##     file) resulted in no readmissions ('NO' under 'readmitted').  Then
##     find the top-5 outcomes that resulted in readmissions, in terms of
##     the percentage of times readmission was required.

dd2 = dd[:] ## subset data frame
dd2["No"] = 1 ## make NO as 1 
tot = dd2["No"].groupby(dd2["discharge_disposition_id"]).sum() ## sum up NO by group 
dd2.loc[dd2["readmitted"] == "NO", "No"] = 0 ## make NO and No as 0
zeros = dd2[dd2["No"] == 0] ## subset no if it is 0 and create it as dataframe
groupzeros = zeros["No"].groupby(zeros["discharge_disposition_id"]).count() ## group by discharge_disposition_id and subset NO and count
outcomes = 100-groupzeros.div(tot)*100 ## find the percentage outcomes
top5 = outcomes.sort_values(ascending=False)[0:5] ## sort values for finding top 5 values
print(top5)

""" 10

discharge_disposition_id
15    73.015873
10    66.666667
12    66.666667
28    61.151079
16    54.545455

"""