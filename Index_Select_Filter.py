# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:48:19 2021

@author: Admin
"""
#------------------------Index, Select & Filter--------------------------------
#Create dataframe :
import pandas as pd

#Create a DataFrame
d = {'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
            'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                    'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
                    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                               'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}

df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score','Exam']]

#View first two rows of the dataframe in pandas:
df[0:2]

#-------Filter in Pandas dataframe:--------------
#View all rows where score greater than 70  
df['Score'] > 70
df[df['Score'] > 70]

#View all the rows where score greater than 70 and less than 85
df[(df['Score'] > 70) & (df['Score'] < 85)]


#-----------------Select in Pandas dataframe-----------------------------------
#select row by using row number in pandas  with .iloc
#.iloc [1:m, 1:n] – is used to select or index rows based on their position 
#from 1 to m rows and 1 to n columns

# select first 2 rows
df.iloc[:2]
# or
df.iloc[:2,]

#select 3rd to 5th rows
df.iloc[2:5]
# or
df.iloc[2:5,]

#select all rows starting from third row
df.iloc[2:]
# or
df.iloc[2:,]

#Select column by using column number in pandas with .iloc
# select first 2 columns
df.iloc[:,:2]
#select first 1st and 4th columns
df.iloc[[2,4],[0,3]]

#Select value by using row name and column name in pandas with .loc:
#.loc [[Row_names],[ column_names]] –used to select or index rows or columns based on their name

#select value by row label and column label using loc
df.loc[[1,2,4,8,11],['Name','Score']]