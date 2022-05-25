# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:44:17 2021

@author: Admin
"""
#---------------------------------Joins----------------------------------------
#We can merge two data frames in python by using the merge() function of pandas
#Create dataframe:
import pandas as pd

# Example 1:

# data frame 1
d1 = {'Customer_id':pd.Series([1,2,3,4,5,6]),
      'Product':pd.Series(['Oven','Oven','Oven','Television','Television','Television'])}
df1 = pd.DataFrame(d1)
print(df1)

# data frame 2
d2 = {'Customer_id':pd.Series([2,4,6]),
      'State':pd.Series(['California','California','Texas'])}
df2 = pd.DataFrame(d2)
print(df2)

#Inner join using pandas: 
#Return only those rows where left table have matching keys in the right table
print (pd.merge(df1, df2, on='Customer_id', how='inner'))

#Full join using pandas
#Returns all rows from both tables.

print (pd.merge(df1, df2, on='Customer_id', how='outer'))
#join records from left table which have matching keys in right table.

#Left Join using pandas
#Returns all rows from left table and any rows with matching keys from right table.
print (pd.merge(df1, df2, on='Customer_id', how='left'))

#Right Join using pandas
#Returns all rows from right table and any rows with matching keys from left table.
print (pd.merge(df1, df2, on='Customer_id', how='right'))

#Example 2:

# Dataset 1
emp_1 = {"Name": ["Penn", "Smith", "William", "Parker"],  
"Age": [21, 32, 29, 28]}  
EmpList_1 = pd.DataFrame(emp_1)  
print(EmpList_1)

# Dataset 2
emp_2 = {"Name": ["Penn", "Suzzane", "William"],  
"Education-Level": ["Under-Grad", "PG", "Grad"]}  
EmpList_2 = pd.DataFrame(emp_2)  
print(EmpList_2)

#Inner join using pandas: 
print (pd.merge(EmpList_1, EmpList_2, on='Name', how='inner'))

#Full join using pandas
print (pd.merge(EmpList_1, EmpList_2, on='Name', how='outer'))
#join records from left table which have matching keys in right table.

#Left Join using pandas
print (pd.merge(EmpList_1, EmpList_2, on='Name', how='left'))

#Right Join using pandas
#Returns all rows from right table and any rows with matching keys from left table.
print (pd.merge(EmpList_1, EmpList_2, on='Name', how='right'))
