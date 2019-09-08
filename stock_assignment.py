##
## File: assignment08.py (STAT 3250)
## Topic: Assignment 8 
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
import numpy as np ## import numby
import pandas as pd ## import pandas
pd.set_option('display.max_columns', 10)
from glob import glob ## import glob
files=glob("*.csv") ## use glob function to bring all the csv files in the directory
df_list = [] ## empty list
for filename in sorted(files): ## use for loop to bring all the files
    df_list.append(pd.read_csv(filename))
    combined = pd.concat(df_list) ## concatenate list as dataframe
combined
##1. Find the mean for the Open, High, Low, and Close entries for all records for all stocks
combined['Open'].mean() ## calculate the mean of Open
combined['High'].mean() ## calculate the mean of High
combined['Low'].mean() ## calculate the mean of Low
combined['Close'].mean() ## calculate the mean of Close
"""
1.
50.86385220906213 -> open
51.459411725747884 -> high
50.25336771426483 -> low
50.876481580135426 -> close

"""

##2. Find the top-5 and bottom-5 stocks in terms of their average Close price. Give tables showing the
## stock ticker symbol and the average Open price.
empt = [] ## create empty list
for i in files: ## use for loop in files
    stock = pd.read_csv(i) ## read each csv file
    avg = stock['Close'].mean() ## subset close and calculate mean
    table = [i.split('.')[0], avg] ## create list which include file name and average of close
    empt.append(table) ## append them
empt
## create the empt list as a datagrame and find the top5 and bottom5
top5 = pd.DataFrame(empt, columns=['stock', 'avg']).sort_values(ascending=False, by='avg').head(5)
bot5 = pd.DataFrame(empt, columns=['stock', 'avg']).sort_values(ascending=True, by='avg').head(5)
print(top5) ## print
print(bot5) ## print

"""
2.
    stock         avg
49    CME  253.956017
25    AZO  235.951950
17   AMZN  185.140534
34    BLK  164.069088
116    GS  139.146781 -> top5

    stock        avg
104   FTR   8.969515
93      F  11.174158
286   XRX  11.291864
87   ETFC  12.808103
120  HBAN  13.697483 -> bot5

"""

##3. Find the top-5 and bottom-5 stocks in terms of the day-to-day volatility of the price, which we define
## to be the mean of the daily differences High - Low for each stock. Give tables for each, as in the
## previous problem.

empt3 = [] ## create empty list
for i in files: ## use for loop
    stock = pd.read_csv(i) ## read each csv file
    stock['Vol'] = stock['High'] - stock['Low'] ## Calculate Volatility and put them into the newcolumn 'Vol'
    avg = stock['Vol'].mean() ## find the mean of volatility
    table = [i.split('.')[0], avg] ## create the list of stock name and avg vol
    empt3.append(table) ## append them
## create the dataframe and find the top5 and the bottom 5
top5 = pd.DataFrame(empt3, columns=['stock', 'vol']).sort_values(ascending=False, by='vol').head(5)
bot5 = pd.DataFrame(empt3, columns=['stock', 'vol']).sort_values(ascending=True, by='vol').head(5)
print(top5) ## print top5
print(bot5) ## print bot5


"""
3.
    stock       vol
49    CME  7.697287
17   AMZN  4.691407
34    BLK  4.470693
25    AZO  4.330294
132   ICE  4.056189 -> top5

    stock       vol
104   FTR  0.205275
286   XRX  0.308743
93      F  0.323567
120  HBAN  0.343893
182    NI  0.363250 -> bot5

"""

##4. Repeat the previous problem, this time using the relative volatility, which we define to be the mean of
## High − Low
## 0.5(Open + Close)
## for each day. As above, provide tables.

empt4 = [] ## create empty list
for i in files: ## use for loop
    stock = pd.read_csv(i) ## read each csv file
    stock['R.Vol'] = (stock['High'] - stock['Low'])/(0.5*(stock['Open'] + stock['Close'])) ## Calculate Relative Volatility and put them into the newcolumn 'R.Vol'
    avg = stock['R.Vol'].mean() ## find the mean of 'R.Vol'
    table = [i.split('.')[0], avg] ## ## create the list of stock name and avg R.vol
    empt4.append(table) ## append them
## create the dataframe and find the top5 and the bottom 5
top5 = pd.DataFrame(empt4, columns=['stock', 'r.vol']).sort_values(ascending=False, by='r.vol').head(5)
bot5 = pd.DataFrame(empt4, columns=['stock', 'r.vol']).sort_values(ascending=True, by='r.vol').head(5)
print(top5) ## print top5
print(bot5) ## print bot5

"""
4.

    stock     r.vol
1     AAL  0.055533
156  LVLT  0.054870
82   EQIX  0.051295
216  REGN  0.048172
87   ETFC  0.045381 -> top5

    stock     r.vol
110   GIS  0.013966
199    PG  0.014192
142     K  0.014992
48     CL  0.015521
274   WEC  0.015761 -> bot5

"""
##5. For each day the market was open in October 2008, find the average daily Open, High, Low, Close,
##and Volume for all stocks.
###check####
octo = combined[(combined['Date'] <= '2008-10-31') & (combined['Date'] >= '2008-10-01')] ## subset dataframe with the specific date
october = octo[['Open', 'High', 'Low', 'Close', 'Volume']].groupby(octo['Date']).mean() ## groupby date with with these columns and calculate the mean
print(october) ## print the table

""" 
5.

            Open       High        Low      Close        Volume
Date                                                                
2008-10-01  43.147874  44.089999  41.845493  43.095090  7.319004e+06
2008-10-02  43.033478  43.443991  40.642233  41.126958  9.555247e+06
2008-10-03  41.555534  42.923984  39.882176  40.264390  9.184641e+06
2008-10-06  39.408827  40.564248  36.730878  39.176739  1.176339e+07
2008-10-07  39.427268  40.293947  36.644575  36.933873  1.091851e+07
2008-10-08  36.106591  38.785221  35.062443  36.676517  1.378626e+07
2008-10-09  37.250109  38.002160  33.437178  33.848607  1.281094e+07
2008-10-10  32.581401  35.952582  30.432287  33.992102  1.820152e+07
2008-10-13  35.486543  38.041322  34.122389  37.548197  1.148344e+07
2008-10-14  38.581369  39.626962  35.513443  36.784888  1.240928e+07
2008-10-15  36.149596  36.757105  32.879340  33.197032  1.051697e+07
2008-10-16  33.485713  35.096629  31.415127  34.599193  1.258398e+07
2008-10-17  33.735344  36.184362  32.729962  34.400653  9.973754e+06
2008-10-20  34.989340  36.357728  33.968497  35.909339  7.657442e+06
2008-10-21  35.390477  36.344741  34.189521  34.665477  7.599813e+06
2008-10-22  33.751940  34.344688  31.386153  32.373295  9.425614e+06
2008-10-23  32.889517  33.987036  30.561443  32.516369  1.189890e+07
2008-10-24  30.046028  32.498308  29.403749  31.395146  9.726575e+06
2008-10-27  30.638140  31.924868  29.501411  29.877173  8.362392e+06
2008-10-28  30.860222  33.145389  29.345018  32.955575  1.091700e+07
2008-10-29  32.864871  34.887581  31.854395  33.179376  1.036944e+07
2008-10-30  34.273941  35.292079  32.884269  34.284817  8.928569e+06
2008-10-31  33.995771  35.761028  33.294631  34.976910  9.213693e+06

"""


## 6. For 2011, fi nd the date with the maximum average relative volatility 
##    for all stocks and the date with the minimum average relative volatility 
##    for all stocks. (Consider only days when the market is open.)
        
eleven = combined[combined['Date'].str[0:4] == '2011'] ## subset the date is 2011 dataframe
empty6=[] ## create empty list
for i in range (1,13): ## use for loop for each month
    for s in range (1,32): ## use for loop for each date
        month = eleven[eleven['Date'].str[5:7].astype(int)==i] ## subset the corresponding month
        day = month[month['Date'].str[8:10].astype(int)==s] ## subset the corresponding date
        day['R.Vol'] = (day['High'] - day['Low'])/(0.5*(day['Open'] + day['Close'])) ## calculate the volatility
        average = day['R.Vol'].mean() ## find the mean of vol
        table=[i, s, average] ## list for month, date, and the avg volatility
        empty6.append(table) ## append them
result6=pd.DataFrame(empty6, columns = ['Month', 'Day', 'R.Vol']) ## create the dataframe       
print(result6.sort_values(by='R.Vol',ascending=False)[0:1]) ## find the maximum
print(result6.sort_values(by='R.Vol',ascending=True)[0:1]) ## find the minimum
"""
6.
     Month  Day     R.Vol
224      8    8  0.073087 -> max
     Month  Day     R.Vol
370     12   30  0.014162 -> min
"""


##7. For 2010-2012, for each day of the week, find the average relative volatility for all stocks. (Consider
##only days when the market is open.)

combined['Subdate'] = pd.to_datetime(combined['Date']) ## subset date and change it to datime and create new column 
combined['R.Vol'] = (combined['High'] - combined['Low'])/(0.5*(combined['Open'] + combined['Close'])) ## calculate the relative vol
combined['Day'] = combined['Subdate'].dt.dayofweek ## subset only dayoftheweek and dcreate the new column
combined1012 = combined[(combined['Date'] <= '2012-12-31') & (combined['Date'] >= '2010-01-01')] ## subset only for certain date
table7 = combined1012['R.Vol'].groupby(combined1012['Day']).mean() ## groupby day and find the r.vol 
Table7 = table7.to_frame() ## change it to frame
Daytable = Table7.set_index([pd.Index(['Mo', 'Tu', 'We', 'Th', 'Fr'])]) ## put index of day
print(Daytable) ## print table

"""
7.

Day    R.Vol
Mo  0.022109
Tu  0.023836
We  0.023443
Th  0.024865
Fr  0.023018

"""

##8. For each month of 2009, determine which stock had the maximum average relative volatility. Give a
##table with the month (number is fine), stock ticker symbol, and average relative volatility.

empt8 = [] ## create the empty list
for i in files: ## use for loop in files
    stock = pd.read_csv(i) ## read csv for each file
    stock['R.Vol'] = (stock['High'] - stock['Low'])/(0.5*(stock['Open'] + stock['Close'])) ## calculate the relative volatility
    stock['Subdate'] = pd.to_datetime(stock['Date']) ## create the subdate column which contains datetime
    stock09 = stock[(stock['Subdate'].dt.year == 2009)] ## use .dt.year to subset only 2009 dataframe 
    for s in range(1,13): ## use for loop for the months
        month = stock09[stock09['Subdate'].dt.month == s] ## subset dataframe corresponding to the month
        avg = month['R.Vol'].mean() ## find the mean of relative volatility
        table = [i.split('.')[0], s, avg] ## create the list of stock name, month, and avg r.vol
        empt8.append(table) ## append them
result8 = pd.DataFrame(empt8, columns = ['Stock', 'Month', 'Avg']) ## make it as dataframe


empt88 = [] ## create empty list
for i in range(1,13): ## use for loop for month
    a = result8[result8['Month'] == i].sort_values(ascending=False, by='Avg').head(1).reset_index() ## subset corresponding month as dataframe and find the max()
    alist = [a['Stock'][0], i, a['Avg'][0]] ## create the list with stock, month, and avg r.vol
    empt88.append(alist) ## append them
empt88


result88 = pd.DataFrame(empt88, columns = ['Stock', 'Month', 'Avg.R.Vol']) ## create dataframe
print(result88) ## print

"""
8.

   Stock  Month  Avg.R.Vol
0    GGP      1   0.190686
1   HBAN      2   0.275587
2    GGP      3   0.241744
3    GGP      4   0.212291
4    GGP      5   0.187383
5    GGP      6   0.131522
6    AIG      7   0.121527
7    AIG      8   0.141233
8    GGP      9   0.103328
9    AAL     10   0.071610
10   GGP     11   0.089010
11   GGP     12   0.112847

"""

##9. The “Python Index” is designed to capture the collective movement of all of our stocks. For each date,
##this is defined as the average price for all stocks for which we have data on that day, weighted by the
##volume of shares traded for each stock. That is, for stock values S1, S2, . . . with corresponding sales
##volumes V1, V2, . . ., the average weighted by volume is
##S1V1 + S2V2 + · · ·
##V1 + V2 + · · ·
##Find the Open, High, Low, and Close for the Python Index for each day the market was open in
##January 2013. Give a table the includes the Date, Open, High, Low, and Close, with one date per row.


## sum of open times volume/ sum of volume

Jan = combined[(combined['Date'] < '2013-01-31') & (combined['Date'] > '2013-01-01')] ## subset specific dates
empt9 = [] ## create empty list
for i in range(1,32): ## use for loop for dates
    mon = Jan[Jan['Date'].str[8:10].astype(int)==i] ## subset corresponding date as dataframe
    avgw1 = ((mon['Open']*mon['Volume'])).sum()/(mon['Volume'].sum()) ## find the python index for open
    avgw2 = ((mon['High']*mon['Volume'])).sum()/(mon['Volume'].sum()) ## find the python index for high
    avgw3 = ((mon['Low']*mon['Volume'])).sum()/(mon['Volume'].sum()) ## find the python index for close
    avgw4 = ((mon['Close']*mon['Volume'])).sum()/(mon['Volume'].sum()) ## find the python index for low
    list9 = [i, avgw1, avgw2, avgw3, avgw4] ## create the list for date, the avg price wighted by volume for open, high, close, low
    empt9.append(list9) ## append them
empt9
result9 = pd.DataFrame(empt9, columns = ['Date', 'Open', 'High', 'Low', 'Close']) ## create dataframe
result9.dropna(inplace=True)
print(result9)
"""
9.

  Date       Open       High        Low      Close
1      2  37.218240  37.669825  36.804244  37.394700
2      3  36.683928  37.175883  36.309854  36.730561
3      4  37.735301  38.197961  37.471489  37.969676
6      7  39.433973  39.952425  39.087880  39.596959
7      8  39.403554  39.748143  38.922081  39.354890
8      9  35.033924  35.411876  34.651302  35.014333
9     10  37.137210  37.527043  36.757483  37.295754
10    11  37.932903  38.256677  37.579063  37.991448
13    14  38.348330  38.759699  37.980530  38.388938
14    15  38.323527  38.880771  38.003460  38.487561
15    16  39.353471  39.731879  38.887220  39.347620
16    17  35.884004  36.233690  35.551895  35.877188
17    18  40.277388  40.652477  39.865453  40.376961
21    22  40.567323  41.068261  40.241281  40.851074
22    23  44.417554  45.121563  44.065735  44.770209
23    24  48.814446  49.728573  48.237470  49.174833
24    25  58.340138  62.089706  58.052795  61.453043
27    28  50.844625  51.450083  49.590466  50.007070
28    29  41.631649  42.499318  41.221507  42.174208
29    30  45.212780  45.587135  44.354852  44.792994

"""


##10. For the years 2007-2012 determine the top-5 months and years in terms of average relative volatility
##of the Python Index. Give a table with the month, year, and average relative volatility.

yr07 = pd.DataFrame(combined[combined['Date'].str.contains('2007')]).sort_values(by='Date') ##subset 2007 years dataframe sort by date
yr08 = pd.DataFrame(combined[combined['Date'].str.contains('2008')]).sort_values(by='Date') ##subset 2008 years dataframe sort by date
yr09 = pd.DataFrame(combined[combined['Date'].str.contains('2009')]).sort_values(by='Date') ##subset 2009 years dataframe sort by date
yr10 = pd.DataFrame(combined[combined['Date'].str.contains('2010')]).sort_values(by='Date') ##subset 2010 years dataframe sort by date
yr11 = pd.DataFrame(combined[combined['Date'].str.contains('2011')]).sort_values(by='Date') ##subset 2011 years dataframe sort by date
yr12 = pd.DataFrame(combined[combined['Date'].str.contains('2012')]).sort_values(by='Date') ##subset 2012 years dataframe sort by date

concayr = pd.concat([yr07, yr08, yr09, yr10, yr11, yr12]) ## concatenate all the years above
concayr['open'] = concayr['Open']*concayr['Volume']  ## create new column which is calculated from open*volume
concayr['high'] = concayr['High']*concayr['Volume'] ## create new column which is calculated from high*volume
concayr['low'] = concayr['Low']*concayr['Volume'] ## create new column which is calculated from low*volume
concayr['close'] = concayr['Close']*concayr['Volume'] ## create new column which is calculated from close*volume

closey = concayr['close'].groupby(concayr['Date']) ## groupby date with close
openy = concayr['open'].groupby(concayr['Date']) ## groupby date with open
lowy = concayr['low'].groupby(concayr['Date']) ## groupby date with low
highy = concayr['high'].groupby(concayr['Date']) ## groupby date with high
volumey = concayr['Volume'].groupby(concayr['Date']) ## groupby date with volume

## create dataframe with pyindex
df10 = pd.DataFrame({'Open': openy.sum()/volumey.sum(), 'High': highy.sum()/volumey.sum(), 
                     'Low': lowy.sum()/volumey.sum(), 'Close': closey.sum()/volumey.sum()})

df10['Date'] = df10.index.values ## put date as an index

df10['AvgR.vol'] = (df10['High'] - df10['Low'])/(0.5*(df10['Open'] + df10['Close'])) ## calculate average relative volatility
df10['Month'] = df10['Date'].str.split('-').str[1] ## bring month
df10['Year'] = df10['Date'].str.split('-').str[0] ## bring year

result10 = df10['AvgR.vol'].groupby([df10['Month'], df10['Year']]).mean() ## groupby month and year with Average relative volatility   
result10.groupby(level=0, group_keys=False).nlargest(1).sort_values(ascending=False).iloc[0:5] ## top5 

""" 
10.

Month  Year    AvgR.vol
10     2008    0.100923
11     2008    0.081326
09     2008    0.067881
03     2009    0.066229
12     2008    0.062545

"""
