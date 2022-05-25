# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:33:29 2021

@author: Admin
"""
#-----------------Apply Family of Functions--------------------------------
#To apply our own functions to dataset, pandas provides three functions from
#apply family of functons: pipe(), apply(), applymap()

# pipe():Table wise Function Application.
# It performs the custom operation for the entire dataframe.
import pandas as pd
# own function
def adder(adder1,adder2):return adder1+adder2

#Create a Dictionary of series
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

print(type(d))
print(d)
df = pd.DataFrame(d)
print (df)
print (df.pipe(adder,2))

# apply():Row or Column Wise Function Application.
# It performs the custom operation for either row wise or column wise.
import numpy as np
#Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

df = pd.DataFrame(d)
print (df)
#Row Wise Fxn Application:
#row wise mean
print (df.apply(np.mean,axis=1))

#Column Wise Fxn Application:
#column wise mean
print (df.apply(np.mean,axis=0))

# applymap():Element wise Function Application.

# applymap():Element wise Function Application.
# It performs specified operation on all the elements of the dataframe. 

#Create a DataFrame
d = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
     'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}

df = pd.DataFrame(d)
print (df)

#Example 1:
print (df.applymap(lambda x:x*2))
#Example2:
import math as m
print (df.applymap(lambda x:m.sqrt(x)))
