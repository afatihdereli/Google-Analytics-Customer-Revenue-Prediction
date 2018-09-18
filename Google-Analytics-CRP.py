# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:02:58 2018

@author: fatih.dereli
"""
#Reading data
import pandas as pd

import json as js

train_df=pd.read_csv('train.csv')

test_df=pd.read_csv('test.csv')

ss_df=pd.read_csv('sample_submission.csv')

#Object sizes in MB
def measure_memory(df, name):
    size_df = df.memory_usage(deep=True)
    print('{} size: {:.2f} MB'.format(name, size_df.sum()/ 1024**2))

measure_memory(train_df, 'Train')
measure_memory(test_df, 'Test')


#Checking first rows of objects
train_df.head()

test_df.head()

ss_df.head()

train_df.info()

len(train_df) - train_df.count()
#channelGrouping	date	device	fullVisitorId	geoNetwork	sessionId	socialEngagementType	totals	trafficSource	visitId	visitNumber	visitStartTime


#JSON formatted columns
train_df.device.head()

js.loads(train_df.device)

train_df.geoNetwork.head()

train_df.trafficSource.head()

train_df.totals.head()


#JSON to DF

from pandas import Series, DataFrame
import numpy as np
import gc


#which columns have json
#device
json_cols = ['device', 'geoNetwork', 'totals',  'trafficSource']
column = 'device'

for column in json_cols:

	c_load = test_df[column].apply(js.loads)
	c_list = list(c_load)
	c_dat = js.dumps(c_list)

	test_df = test_df.join(pd.read_json(c_dat))
	test_df = test_df.drop(column , axis=1)

test_df.head()
test_df.to_csv('test_cleaned.csv')


test = []
gc.collect()
#which columns have json
#device
json_cols = ['device', 'geoNetwork', 'totals',  'trafficSource']
column = 'device'

for column in json_cols:

	c_load = train_df[column].apply(js.loads)
	c_list = list(c_load)
	c_dat = js.dumps(c_list)

	train_df = train_df.join(pd.read_json(c_dat))
	train_df = train_df.drop(column , axis=1)

train_df.head()
train_df.to_csv('train_cleaned.csv')

#Summary after flattened JSON objects
train_df.info()

len(train_df) - train_df.count()

test_df.info()

len(test_df) - test_df.count()

#Test NaN values bounces,newVisits,adContent,isTrueDirect,keyword,referralPath

test_df.referralPath.head()

#train_df=pd.read_csv('train_cleaned.csv')

#test_df=pd.read_csv('test.csv')