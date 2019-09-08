##
## File: assignment03.py (STAT 3250)
## Topic: Assignment 3
##

##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.

## 1.  All questions refer to the data set 'absent.csv'.
import numpy as np # load "numpy"
import pandas as pd # load pandas as pd
abst = pd.read_csv('absent.csv')

## 1(a) Find the mean absent time among all records.
print(np.mean(abst['Absenteeism time in hours'])) ## mean of absent time and print

"""
## 1(a)

output = 6.924324324324324 hrs

"""

## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.

th = abst.loc[abst['Day of the week'] == 5] ## make a variable for the subset of Day of the week which is Thursday
print(len(th)) ## find the length of the variable and print
"""
## 1(b)

output = 125

"""

## 1(c) Find the number of different employees represented in 
##      this data.
print(len(abst['ID'].groupby(abst['ID']))) ## group by ID and figure out the length of the ID

"""
## 1(c)

output = 36

"""


## 1(d) Find the transportation expense for the employee with
##      ID = 34.

te = np.mean(abst.loc[abst['ID']==34, ['Transportation expense']]) ## make a variable for the mean of transportation expense which is found by subsetting Transportation expense with corresponding ID(34)
print(te) ## print out

"""
## 1(d)

output = 118

"""


## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.

meanhr = abst['Absenteeism time in hours'].groupby(abst['ID']) ## groupby ID and subset absent hours and make a variable for them
print(meanhr.mean().loc[11]) ## find the mean number of hours absent for ID = 11 and print

"""
## 1(e)

output = 11.25

"""
## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.

pet = abst['Absenteeism time in hours'].groupby(abst['Pet']) ##groupby Pet and subset absent hours and make a vraiable for them
nopet = pet.mean()[0] ## find the records of those who have no pets
yespet = pet.mean()[2:] ## find the records of those who have more than one pet(2 or more)
print(nopet) ## print the mean number of hrs for people have no pet
print(yespet.mean()) ## take another mean function to find the mean of people who have 2, 4, 5, or 8 pets and print the mean number of hrs for people have 2 or more pets

"""
## 1(f)

output = nopet = 6.828260869565217
         more than one = 5.057291666666667

"""
## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.

sm8 = abst.loc[abst['Absenteeism time in hours'] > 8, ['Social smoker']] ## subset absent hrs which are greater than 8, and subset corresponding social smoker
sm4 = abst.loc[abst['Absenteeism time in hours'] <= 4, ['Social smoker']] ## subset absent hrs which are equal or less than 4, and subset corresponding social smoker
sm8perc = np.sum(sm8==1)/np.sum(sm8==sm8)*100 ## calculate the propotion of smokers and times 100 to mkae is as percentage
sm4perc = np.sum(sm4==1)/np.sum(sm4==sm4)*100 ## calculate the propotion of smokers and times 100 to mkae is as percentage
print(sm8perc) ## print the percentage for the proportion of smokers whose abst hrs >8
print(sm4perc) ## print the percentage for the proportion of smokers whose abst hrs <=4

"""
## 1(g)

output = over8 = 6.349206
         less4 = 6.290672

"""

## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.

sd8 = abst.loc[abst['Absenteeism time in hours'] > 8, ['Social drinker']] ## subset absent hrs which are greater than 8, and subset corresponding social drinker
sd4 = abst.loc[abst['Absenteeism time in hours'] <= 4, ['Social drinker']] ## subset absent hrs which are greater than 8, and subset corresponding social drinker
sd8perc = np.sum(sd8==1)/np.sum(sd8==sd8)*100 ## calculate the propotion of drinkers and times 100 to mkae is as percentage
sd4perc = np.sum(sd4==1)/np.sum(sd4==sd4)*100 ## calculate the propotion of drinkers and times 100 to mkae is as percentage
print(sd8perc) ## print the percentage for the proportion of drinkers whose abst hrs >8
print(sd4perc) ## print the percentage for the proportion of drinkers whose abst hrs <=4

"""
## 1(h)

output = over8 = 73.015873
         less4 = 53.362256

"""


## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.
 
sorthr = abst['Absenteeism time in hours'].groupby(abst['ID']) ## subsent absent hr and ID and make a group for them by ID
top5 = sorthr.sum().sort_values(ascending=False)[0:5] ## sort values by decending and take top 5
print(top5) ## print top 5 employee IDs

"""
## 2(a)

output = 
ID
3     482
14    476
11    450
28    347
34    344

"""

## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.

day = abst['Absenteeism time in hours'].groupby(abst['Day of the week']) ## subset day of the week and absent hours and make a group by day of the week
print(day.mean()) ## print the avg hours absent for each day of the week

"""
## 2(b)

output = Day of the week
        2    9.248447
        3    7.980519
        4    7.147436
        5    4.424000
        6    5.125000

"""

## 2(c) Repeat 2(b) replacing day of the week with month.

month = abst['Absenteeism time in hours'].groupby(abst['Month of absence']) ## subset month of absence and absent hours and make a group by month of absence
print(month.mean()) ## print the avg hours absent for each month

"""
## 2(c)

output = Month of absence
        0      0.000000
        1      4.440000
        2      4.083333
        3      8.793103
        4      9.094340
        5      6.250000
        6      7.611111
        7     10.955224
        8      5.333333
        9      5.509434
        10     4.915493
        11     7.507937
        12     8.448980
       
"""
## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers.

## both works
reason = abst.loc[abst['Social smoker'] == 1, ['Reason for absence']] ## subset Social smokers with corresponding reason for absence
print(reason)
reason['Reason for absence'].value_counts()[0:7] ## count reason for absecne value by descending order and subset from first index to 8th b/c 5 of 3rd common reasons are ranked same

## this works too
sortedreason = reason.sort_values(by = 'Reason for absence')
print(sortedreason)
sortedreason['Reason for absence'].value_counts()

reason1 = abst.loc[abst['Social smoker'] == 0, ['Reason for absence']] ## subset non-social smokers with corresponding reason for absence
print(reason1)
reason1['Reason for absence'].value_counts()[0:3] ## count reason for absecne value by descending order and subset from the first index to the third index

"""
## 2(d)

output = for the smokers 
        0     8
        25    7
        19    4
        18    4
        28    4
        22    4
        23    4  
        for the non-smokers
        23    145
        28    108
        27     69               
        
"""

## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.
n = len(abst) ## find the length of absent data
phat = np.sum(abst['Social drinker']==1)/np.sum(abst['Social drinker']==abst['Social drinker']) ## calculate phat which is the proportion of the records that are from social drinkers
lb = phat - 1.96*np.sqrt(phat*(1-phat)/n) ## calculate lower boundary to find the confidence interval
ub = phat + 1.96*np.sqrt(phat*(1-phat)/n) ## calculate upper boundary to find the confidence interval
print(lb) ## print lower bound
print(ub) ## print upper bound

"""
## 2(d)

output = lower bound = 0.5318725067607831
         upper bound = 0.603262628374352
         95% Confidence interval = ( 0.5318725067607831 , 0.603262628374352 )
"""



## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)

## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.


popmean = np.mean(pop) ## population mean
arr = np.zeros(100000) ## set an array as 100000 zeros array
for i in range(0,100000): ## run for loop in range 100000 ## use for loop with range 100000
    s = np.random.choice(pop, size=10) ## sampling
    smean = np.mean(s) ## sample mean
    arr[i] = smean ## put the calculated sample mean into the empty array    
meanofsmean = np.mean(arr) ## mean of the sample means
PRB = 100*((meanofsmean) - (popmean)) / (popmean) ## calculate the percentage relative bias
print(PRB) ## print the value

"""
## 3(a)

output = 0.01724215872006188
        
"""

## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.


popvar = np.var(pop) ## population variance
arr1 = np.zeros(100000) ## set an arry as 100000 empty array
for i in range(0,100000): ## run for loop in range 100000
    s1 = np.random.choice(pop, size=10) ## sampling
    svar = np.var(s1) ## sample variance
    arr1[i] = svar ## put the calculated sample variance into the empty array
meanofsvar = np.mean(arr1) ## mean of the sample variances
PRB1 = 100*((meanofsvar) - (popvar)) / (popvar) ## calculate the percentage relative bias
print(PRB1) ## print the value


"""
## 3(b)

output = -9.814260535327193
  
"""

## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)

popvar = np.var(pop) ## population variance
arr2 = np.zeros(100000) ## make the arr2 as the empty set
for i in range(0,100000): ## run for loop in range 100000
    samp = np.random.choice(pop, size=10) ## sampling
    svar1 = np.var(samp, ddof=1) ## sample variance with degree of freedom 1
    arr2[i] = svar1 ## put it into the empty array
meanofsvar1 = np.mean(arr2) ## mean of the sample variances
PRB2 = 100*((meanofsvar1) - (popvar)) / (popvar) ## calculate the percentage relative bias
print(PRB2) ## print the value


"""
## 3(c)

output = 0.05553451845402835
  
"""

## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.

popmed = np.median(pop) ## population median
arr3 = np.zeros(100000) ## empty array
for i in range(0,100000): ## run for loop in range 100000
    s = np.random.choice(pop, size=10) ## sampling
    smed = np.median(s) ## sample median
    arr3[i] = smed ## put it into the empty array
meanofsmed = np.mean(arr3) ## mean of sample medians
PRB3 = 100*((meanofsmed) - (popmed)) / (popmed) ## calculate the percentage relative bias
print(PRB3) ## print the value

"""
## 3(d)

output = 7.514432355360508
  
"""

