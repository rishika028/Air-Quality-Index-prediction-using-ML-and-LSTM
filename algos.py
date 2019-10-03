#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:19:01 2019

@author: retroflake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = [16,9]

#reading from the dataframe from the pickle file
rf=pd.read_pickle('dframe.pkl')
aqi =pd.read_pickle('final_aqi.pkl')
aqi = np.asarray(aqi)

#feature scaling
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
print(scaler.fit(rf))
ds=scaler.transform(rf)

#taking PM2.5 as the Dependent Variable
y=aqi
#Taking rest of the variables as features
X=ds[:,6:]


#splitting the variables into train and test variables
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1234)

#converting the variables to integers(do not run this)
X=X.astype(int)
y=y.astype(int)

#Linear Regression
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)
y_pred=reg.predict(X_test)
print(reg.score(X,y))


#calculating mean square error
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)

#SVM
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score
LSVC = LinearSVC()

LSVC = LSVC.fit(X_train,y_train)
y_pred = LSVC.predict(X_test)
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

#KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
KNN=KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train,y_train)
y_pred=(KNN.predict(X_test))
print(accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
