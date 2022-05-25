# -*- coding: utf-8 -*-
"""
Created on Sat April 4 01:46:06 2020

@author: Admin
"""

print("hello world")

#Numbers
#a=3 , b=5  #a and b are number objects 

#String
str1 = 'Hello Students' #string str1
str2 = ' how are you' #string str2  
str1
str2
print (str1[0:5]) #printing first five character using slice operator  
(str1[0:5])
print (str1[4]) #printing 5th character of the string  
print (str1*2) #printing the string twice  
print (str1 + str2) #printing the concatenation of str1 and str2

#Lists
l  = [1, "hi", "python", True] 
print (l[3:])  
print (l[0:2])
print (l) 
print (l + l) 
print (l * 3)
print (type(l))
#Lets try mutation 
l[1] = "Bye"
print (l)

#Tuple
t  = ('hi', 'python', 2, 4) 
t 
print (t[1:]);  
print (t[0:3]);  
print (t);  
print (t + t)
print (t * 3)  
print (type(t)) 
#Lets try mutation 
t[1] = "Bye"
print (t)

#Dictionary
d = {1:"Jimmy", 2:'Alex', 3:'john', 4:'mike'}
d
print("1st name is "+d[1])  
print("2nd name is "+ d[4]) 
print (d); 
print (d.keys());  
print (d.values());

#----ADVANCED----
#list
#ordered collection of items; sequence of items in a list
shoplist =['apple','carrot','mango', 'banana']
shoplist
len(shoplist)
print(shoplist)

#add item to list
shoplist.append('rice')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )
zoo = ('python','lion','elephant','bird')
zoo
len(zoo)
languages = 'c', 'java', 'php' , 1 #better to put (), this also works
languages
type(languages)

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon

student = {'A101': 'Abhinav', 'A102': 'Ravi', 'A103':'Prafull', 'A104': 'Karan'}
student
student['A103']
print('Name of rollno A103 is ' +student['A103'])
del student['A104']
student
len(student)

#for rollno, name in student.items():
    #print('name of {} is {} '.format(rollno, name) )

#Lets test Mutation: 
#adding a value
student['A104'] = 'Hitesh'
student

#Set
Anubhav = {1,2,3,4,5}
Anubhav
Aman_1 = set()
Aman_1

#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india','england','australia','sri lanka','ireland'])
teamA
teamB = set(['pakistan', 'south africa','bangladesh','ireland'])
teamB

#Checking whether a data value exists in a set or not.
'india' in teamA
'india' in teamB

#Adding values in a set
teamA.add('China')
teamA  #puts in order
teamA.add('india')
teamA  #no duplicates
teamA.remove('australia')
teamA

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

d

df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score','Exam']]

#View first two rows of the dataframe in pandas:
df[0:2]





