#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:10:53 2019

@author: retroflake
"""

import aqi
import pandas as pd
import numpy as np

#Reading the features from the pickle file
df=pd.read_pickle('dframe.pkl')

max_aqi = []
aqi_list = []

#finding the AQI from the given feature of pollutants
for i in range(1012):
    max_aqi.append(aqi.find_aqi('PM2.5',int(df.iloc[i][0])))
    max_aqi.append(aqi.find_aqi('PM10',int(df.iloc[i][1])))
    max_aqi.append(aqi.find_aqi('O3',int(df.iloc[i][2])))
    max_aqi.append(aqi.find_aqi('NO2',int(df.iloc[i][3])))
    max_aqi.append(aqi.find_aqi('SO2',int(df.iloc[i][4])))
    max_aqi.append(aqi.find_aqi('CO',int(df.iloc[i][5])))
    aqi_list.append(max(max_aqi))
    max_aqi = []
    
#Using pandas to convert the 'list' to a dataframe so that it can be saved in a pickle file 
aqi_list= pd.DataFrame(aqi_list)
#Saving the dataframe in the pickel format
aqi_list.to_pickle('final_aqi.pkl')

#Just an example to show how to import a pickle file and convert it into an array
hh=pd.read_pickle('final_aqi.pkl')
hh= np.asarray(hh)

    