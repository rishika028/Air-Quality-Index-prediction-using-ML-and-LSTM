#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:40:30 2019

@author: retroflake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = [16,9]
df=pd.read_csv("../dataset/aqi.csv")

df=df.drop(['locationid','stationname','chinesename','latitude','longitude','est_time'],axis=1)


df['pm10']=df['pm10'].replace('-',np.NaN)
df['o3']=df['o3'].replace('-',np.NaN)
df['no2']=df['no2'].replace('-',np.NaN)
df['so2']=df['so2'].replace('-',np.NaN)
df['co']=df['co'].replace('-',np.NaN)
df['temperature']=df['temperature'].replace('-',np.NaN)
df['dewpoint']=df['dewpoint'].replace('-',np.NaN)
df['pressure']=df['pressure'].replace('-',np.NaN)
df['wind']=df['wind'].replace('-',np.NaN)
df['humidity']=df['humidity'].replace('-',np.NaN)
df=df.dropna()
df=df.dropna(axis='columns')

df
df.to_pickle('dframe.pkl')