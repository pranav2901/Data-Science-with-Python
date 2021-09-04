# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:05:47 2021

@author: Admin
"""
#--------------------------Handling Missing Values----------------------------

#Counting the Missing Values---------------------------
import pandas as pd
import numpy as np

#Create a DataFrame
df1 = {'Subject':['semester1','semester2','semester3','semester4','semester1',
                  'semester2','semester3'],
'Score':[62,47,np.nan,74,np.nan,77,85]}

df1 = pd.DataFrame(df1,columns=['Subject','Score'])
print(df1)

'''Is there any missing values in dataframe '''
df1.isnull()
df1.notnull()

'''Is there any missing values across columns'''
df1.isnull().any()

'''How many missing values are there across each column'''
df1.isnull().sum()

#Dropping rows with Missing Values-----------------------

#Create a DataFrame
df1 = {'Name':['George','Andrea','micheal','maggie','Ravi','Xien','Jalpa',np.nan],
       'State':['Arizona','Georgia','Newyork','Indiana','Florida','California',np.nan,np.nan],
       'Gender':["M","F","M","F","M","M",np.nan,np.nan],
       'Score':[63,48,56,75,np.nan,77,np.nan,np.nan]}

df1 = pd.DataFrame(df1,columns=['Name','State','Gender','Score'])
print(df1)

#Drop all rows that have any NaN (missing) values
df1.dropna()

#Drop only if entire row has NaN values
df1.dropna(how='all')

#Drop only if a row has more than 2 NaN values
df1.dropna(thresh=2)

#Drop NaN in a specific column
df1.dropna(subset=['Gender'])
df2 = df1.dropna(subset=['Gender','Score'])
df2
#Dropping rows using axis values:
df1
df1.dropna(axis=0)

#Dropping columns using axis values:
df1.dropna(axis=1)

#------------------Creating Data Frame Again-----------------------------------
df1 = {'Name':['George','Andrea','micheal','maggie','Ravi','Xien','Jalpa',np.nan],
       'State':['Arizona','Georgia','Newyork','Indiana','Florida','California',np.nan,np.nan],
       'Gender':["M","F","M","F","M","M",np.nan,np.nan],
       'Score':[63,48,56,75,np.nan,77,np.nan,np.nan]}

df1 = pd.DataFrame(df1,columns=['Name','State','Gender','Score'])
print(df1)
#------------------Replacing Missing Values with Zero--------------------------

df1
df1.fillna(0)

#-----------------Replacing Missing Values with Mean of the column-------------

df1
df1["Score"].fillna(df1["Score"].mean(),inplace=True)
print(df1)

#----------------Replacing Missing Value with Median of the column-------------
df1["Score"].fillna(df1["Score"].median(), inplace=True)
print(df1)

#Replace Missing (or) Generic Values using replace() method
#Many times, we have to replace a generic value with some specific value. 
#We can achieve this by applying the replace method.
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
print(df)

print (df.replace({1000:10,2000:60}))

#------------------Handling Duplicate Values--------------------------------

#The drop_duplicates() function performs common data cleaning task that deals with duplicate values
#in the DataFrame. This method helps in removing duplicate values from the DataFrame.

emp = {"Name": ["Parker", "Smith", "William", "Parker"],  
"Age": [21, 32, 29, 21]}  
info = pd.DataFrame(emp)  
print(info) 
info = info.drop_duplicates() 
print(info)


emp = {"Name": ["Parker", "Smith", "William", "Parker"],  
"Age": [21, 32, 29, 22]}  
info = pd.DataFrame(emp) 
print(info)
info = info.drop_duplicates()  
print(info)  