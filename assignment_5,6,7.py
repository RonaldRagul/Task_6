# -*- coding: utf-8 -*-
"""Assignment_5,6,7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E9CSVS0BOOdg2cU9gwWo0ZJTsY7mtxgb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

"""###Assignment 5

"""

ground_cricket_data = {"Chirps/Second": [20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7,
                                         15.7, 15.4, 16.3, 15.0, 17.2, 16.0, 17.0,
                                         14.4],
                       "Ground Temperature": [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7,
                                              71.6, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5,
                                              76.3]}
df = pd.DataFrame(ground_cricket_data)
df

#split data
x = df.iloc[:,-1:]
y = df.iloc[:,:-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

xtrain=x_train.values.reshape(-1,1)
ytrain=y_train.values.reshape(-1,1)
xtest=x_test.values.reshape(-1,1)
ytest=y_test.values.reshape(-1,1)

#model fiting
lr=LinearRegression()
lr.fit(xtrain,ytrain)
y_pred=lr.predict(xtest)

## 1.Find the linear regression equation for this data.
print("coffecient",lr.coef_)
print("Intercept",lr.intercept_)
Yeq=(xtest*lr.coef_)+lr.intercept_
print(Yeq)

## 2.Chart the original data and the equation on the chart.
plt.xlabel("Ground Temperature")
plt.ylabel("Chirps/Second")
plt.scatter(x,y,color="red",marker="+")
plt.plot(xtest,y_pred,color="blue")
plt.show

## 3.Find the equation's  𝑅2  
er_scr=r2_score(ytest,y_pred)
print("Error score =", er_scr)

## 4. Extrapolate data: If the ground temperature reached 95, then at what approximate rate would you expect the crickets to be chirping?
Yeq=(95*lr.coef_)+lr.intercept_
print(Yeq)

# 5.Interpolate data: With a listening device, you discovered that on a particular morning the crickets were chirping at a rate of 18 chirps per second. What was the approximate ground temperature that morning?
xeq=18-lr.intercept_
xeq/lr.coef_
ieq=(xeq/lr.coef_)
print(ieq)

"""###Assignment 6

"""

data =pd.read_fwf("brain_body.txt")
df = pd.DataFrame(data)
df.head()

##spliting data
x = np.log2(df.iloc[:,:-1])
y = np.log2(df.iloc[:,-1:])

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=2)

xtrain=x_train.values.reshape(-1,1)
ytrain=y_train.values.reshape(-1,1)
xtest=x_test.values.reshape(-1,1)
ytest=y_test.values.reshape(-1,1)

##model_fit
lr =LinearRegression()
lr.fit(xtrain,ytrain)
y_pred =lr.predict(xtest)

##1.Find the linear regression equation
print("coefficient",lr.coef_)
print("intercept",lr.intercept_)
yeq=(x*lr.coef_)+lr.intercept_
print(yeq)

## 2. Chart the original data and the equation on the chart.
# plot the graph
plt.xlabel("Brain")
plt.ylabel("Body")
plt.scatter(x,y,color="red",marker="+")
plt.plot(xtest,y_pred,color="blue")

## 3. Find the equation's  𝑅2  score (use the .score method) to determine whether the equation is a good fit for this data. (0.8 and greater is considered a strong correlation.)

er_scr=r2_score(ytest,y_pred)
print("Error score =", er_scr)

"""###Assignment 7

"""

df = pd.read_fwf("salary.txt", header=None, 
                 names=["Sex", "Rank", "Year", "Degree", "YSdeg", "Salary"])

df.head()

##spliting data
x =df.iloc[:,:5]
y =df.iloc[:,-1:]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 3)

#fitting data
lr = LinearRegression()  
lr.fit(x_train, y_train)
train_data_pred=lr.predict(x_train)
y_pred =lr.predict(x_test)

plt.scatter(y_train,train_data_pred)

##1.linear reggerssion equation
print("Intercept: ", lr.intercept_)
print("Coefficients:")
list(zip(x, lr.coef_))


lre = (x_test*lr.coef_)+lr.intercept_
lre

error_score=r2_score(y_test,y_pred)
print(error_score)

print("Coefficients:")
list(zip(x,lr.coef_))

## 3.Report whether sex is a factor in salary.
corr = df.corr()["Salary"].sort_values(ascending=False)[1:]
corr

# -> From the resultgiven below, the correlation value between sex and salary is -0.252782
# -> Since the corrrelation between sex and city is negative, we can conclude that sex is not a factor or a bad factor to predict the salary.