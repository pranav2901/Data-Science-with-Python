# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:49:04 2021

@author: Admin
"""
# Logistic Regression

#-------------Logistic Regression------------------------------
#Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Import data 
titanic_data = pd.read_csv("D:\SkillEdge\Python\Final\Codes\pyData/titanic.csv")
titanic_data.head(5)
titanic_data.tail(5)

print("No. of passengers in original dataset:" +str(len(titanic_data.index)))
      
#Analyzing Data
sns.countplot(x="survived",data=titanic_data)

sns.countplot(x="survived",hue="sex",data=titanic_data)

sns.countplot(x="survived",hue="pclass",data=titanic_data)

#CHECKING DATA TYPE OF A VARIABLE AND CONVERTING IT INTO ANOTHER TYPE-----
titanic_data.info()
titanic_data["age"].plot.hist()
plt.hist(titanic_data["age"])


#Converting var "age" from object type to float type
titanic_data["age"] = pd.to_numeric(titanic_data.age, errors='coerce')
titanic_data.info()
#Parameter: errors = 'coerce' in above fxn, replaces missing values (like "?") if any
#in "age" column by "nan" values.

titanic_data["age"].plot.hist()

#Converting var "fare" from object type to float type
titanic_data["fare"] = pd.to_numeric(titanic_data.fare, errors='coerce')
titanic_data.info()
#Parameter: errors = 'coerce' in above fxn, replaces missing values (like "?") if any
#in "fare" column by "nan" values.

titanic_data["fare"].plot.hist()

#Identifying/Finding missing values if any----
titanic_data.isnull()
titanic_data.isnull().sum()

sns.heatmap(titanic_data.isnull(),yticklabels=False, cmap="viridis")

#Note: 
#Since missing values in "fare" are quite less, we can delete such rows.
#Since missing values in "age" are high, its better we do imputation in it.

sns.boxplot(x="age",data=titanic_data)
sns.boxplot(x="fare",data=titanic_data)

#By boxplot we observe that the no. of outliers in "age" are quite less, hence,
#if we plan to do imputation in "age" we can do it by "mean" imputation.

#Handling Missing Values------------
titanic_data.head(5)

#Droping all the rows which have a missing value in column (Fare)
#Drop NaN in a specific column
titanic_data.dropna(subset=['fare'],inplace=True)
sns.heatmap(titanic_data.isnull(),yticklabels=False)

#Imputing missing values in column (Age) with mean imputation
titanic_data["age"].fillna(titanic_data["age"].mean(), inplace=True)
sns.heatmap(titanic_data.isnull(),yticklabels=False)

#Hence, we do not have any missing values in the dataset now.
titanic_data.isnull().sum()

#Note:
#A Heat map is usually drawn for either continuous of categorical var
#Lets take few cont var columns and draw the heat map
#Cont = titanic_data[:,[5,6,7]]
#sns.heatmap(Cont)

#There are lot of string value var in dataset which have to be converted to numerical
#values for applying machine learing algoritm. Hence, we will now convert string var 
#to numerical var.
titanic_data.info()
pd.get_dummies(titanic_data["sex"])

pd.get_dummies(titanic_data["sex"],drop_first=True)

Sex_Dummy = pd.get_dummies(titanic_data["sex"],drop_first=True)
Sex_Dummy.head(5)

pd.get_dummies(titanic_data["embarked"])
Embardked_Dummy = pd.get_dummies(titanic_data["embarked"],drop_first=True)
Embardked_Dummy.head(5)

pd.get_dummies(titanic_data["pclass"])
PClass_Dummy = pd.get_dummies(titanic_data["pclass"],drop_first=True)
PClass_Dummy.head(5)

#Now, lets concatenate these dummy var columns in our dataset.
titanic_data = pd.concat([titanic_data,Sex_Dummy,PClass_Dummy,Embardked_Dummy],axis=1)
titanic_data.head(5)

#dropping the columns whose dummy var have been created
titanic_data.drop(["sex","embarked","pclass","Passenger_id","name","ticket"],axis=1,inplace=True)
titanic_data.head(5)

#Splitting the dataset into Train & Test dataset
x=titanic_data.drop("survived",axis=1)
y=titanic_data["survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
help(LogisticRegression())
logmodel = LogisticRegression(solver='liblinear') #It is the default solver for Scikit-learn versions earlier than 0.22.0.
logmodel.fit(X_train, y_train)

predictions = logmodel.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,predictions)

confusion_matrix(predictions,y_test)

#Hence, accuracy = (165+84)\(165+84+30+44) = 77.5%

#Calculating the coefficients:
print(logmodel.coef_)

#Calculating the intercept:
print(logmodel.intercept_)

#----To Improve the accuracy of the model, lets go with Backward ELimination Method &
# rebuild the logisitc model again with few independent variables--------
titanic_data_1 = titanic_data
titanic_data_1.head(5)

#--------------------------Backward Elimination--------------------------------
#Backward elimination is a feature selection technique while building a machine learning model. It is used
#to remove those features that do not have significant effect on dependent variable or prediction of output.

#Step: 1- Preation of Backward Elimination:
#Importing the library:
import statsmodels.api as sm

#Adding a column in matrix of features:
x1=titanic_data_1.drop("survived",axis=1)
y1=titanic_data_1["survived"]
import numpy as nm
x1 = nm.append(arr = nm.ones((1291,1)).astype(int), values=x1, axis=1)

#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of 
#independent features that are significantly affecting the dependent variable.
x_opt= x1[:, [0,1,2,3,4,5,6,7,8,9,10]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of statsmodels library. 
#Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y1, exog=x_opt).fit()

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

#In the above summary table, we can clearly see the p-values of all the variables. 
#And remove the ind var with p-value greater than 0.05
x_opt= x1[:, [0,1,2,4,5,6,7,8,9,10]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,4,5,6,7,9,10]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,5,6,7,9,10]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt= x1[:, [0,1,2,5,6,7,10]]
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()
regressor_OLS.summary()
#Hence,independent var - age, sibsp, sex, pclass & embarked are significant variable 
#for the predicting the value of Dependent Var "survived".
#So we can now predict efficiently using these variables.

#-------Building Logistic Regression model using ind var: age, sibsip, sex, pclass & embarked--------  
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_opt, y1, test_size= 0.25, random_state=0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression(solver='liblinear')
logmodel.fit(x_BE_train, y_BE_train)

predictions = logmodel.predict(x_BE_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_BE_test,predictions)

#Accuracy = (170+87)/(170+87+25+41) = 80%

#Calculating the coefficients:
print(logmodel.coef_)

#Calculating the intercept:
print(logmodel.intercept_)

#So, ur final Predicitve Modelling Equation becomes:
#Survived = 
#exp(3.74 -0.03*age -0.27*sibsp -2.52*sex(male) -1.03*pclass(2) -2.1*pclass(3) -0.33*embd(S))
# \
#exp(3.74 -0.03*age -0.27*sibsp -2.52*sex(male) -1.03*pclass(2) -2.1*pclass(3) -0.33*embd(S)) + 1
