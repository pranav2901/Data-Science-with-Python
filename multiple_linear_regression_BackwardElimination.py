# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:49:36 2021

@author: Admin
"""
# Multiple Linear Regression

# Importing the libraries

'import matplotlib.pyplot as plt'
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('D:\SkillEdge\Python\Final\Codes\pyData/50_Startups.csv')

#Method-1 (Handling Categorical Variables)
pd.get_dummies(dataset["State"])
pd.get_dummies(dataset["State"],drop_first=True)
S_Dummy = pd.get_dummies(dataset["State"],drop_first=True)
S_Dummy.head(5)
#Now, lets concatenate these dummy var columns in our dataset.
dataset = pd.concat([dataset,S_Dummy],axis=1)
dataset.head(5)
#dropping the columns whose dummy var have been created
dataset.drop(["State",],axis=1,inplace=True)
dataset.head(5)
#------------------------------------------------------------------------------

#Obtaining DV & IV from the dataset
X = dataset.iloc[:,[0,1,2,4,5]].values
y = dataset.iloc[:,3].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Accuracy of the model

#Calculating the r squared value:
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

#Coefficient
regressor.coef_

# Intercept
regressor.intercept_

#The above score tells that our model is 93% accurate with the test dataset.

#--------------------------Backward Elimination--------------------------------
#Backward elimination is a feature selection technique while building a machine learning model. It is used
#to remove those features that do not have significant effect on dependent variable or prediction of output.

#Step: 1- Preparation of Backward Elimination:

#Importing the library:
import statsmodels.api as sm

#Adding a column in matrix of features:
import numpy as nm
X = nm.append(arr = nm.ones((50,1)).astype(int), values=X, axis=1)

#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of 
#independent features that are significantly affecting the dependent variable.
x_opt=X[:, [ 0,1,2,3,4,5]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of 
#statsmodels library. Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

#In the above summary table, we can clearly see the p-values of all the variables. 
#Here x1, x2 are dummy variables, x3 is R&D spend, x4 is Administration spend, and x5 is Marketing spend.

#Now since x5 has highest p-value greater than 0.05, hence, will remove the x1 variable
#(dummy variable) from the table and will refit the model.
x_opt= X[:, [0,1,2,3,4]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Now since x4 has highest p-value greater than 0.05, hence, will remove the x4 variable
#(dummy variable) from the table and will refit the model.
x_opt= X[:, [0,1,2,3]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Now we will remove the Admin spend (x2) which is having .602 p-value and
# again refit the model.
x_opt= X[:, [0,1,3]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Finally, we will remove one more variable, which has .60 p-value for marketing spend,
#that is more than significant level value of 0.05
x_opt= X[:, [0,1]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

#Hence,only  R&D independent variable is a significant variable for the prediction. 
#So we can now predict efficiently using this variable.

#----------Building Multiple Regression model by only using R&D spend:-----------------
#importing datasets  
data_set= pd.read_csv('F:/WORK/pyWork/pyData/50_Startups.csv') 
#Extracting Independent and dependent Variable  
x_BE= data_set.iloc[:,:-4].values
y_BE= data_set.iloc[:,4].values 
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_BE, y_BE, test_size= 0.2, random_state=0)

#Fitting the MLR model to the training set:  
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_BE_train, y_BE_train)

#Predicting the Test set result;
y_pred= regressor.predict(x_BE_test)

#Cheking the score  
#Calculating the r squared value:
from sklearn.metrics import r2_score
r2_score(y_BE_test,y_pred)
#The above score tells that our model is now more accurate with the test dataset with
#accuracy equal to 95%

#Calculating the coefficients:
print(regressor.coef_)

#Calculating the intercept:
print(regressor.intercept_)

#Regression Eq'n: Profit = 48416 + 0.85*R&D_Spend
© 2021 GitHub, Inc.