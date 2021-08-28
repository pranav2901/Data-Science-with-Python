# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:32:07 2021

@author: Admin
"""
# -*- coding: utf-8 -*-
"""

#abs(): Returns the absolute value of a number.
#  integer number     

integer = -20
abs(integer)  
print('Absolute value of -20 is:', abs(integer))  
  
#  floating number  

floating = -20.83  
print('Absolute value of -20.83 is:', abs(floating))  

#all(): It returns true if all items passed in iterable object are true. 
#Otherwise, it returns False.
#This fxn accepts an iterable object (such as list, dictionary, etc.). 
# all values true  

k = [1, 3, 4, 6]  
print(all(k))
  
# all values false  

k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))
  
# empty iterable  
k = []  
print(all(k)) 

#------------------------------------------------------------------------------------

#bool(): Converts a value to boolean(True or False)
test1 = []  
print(test1,'is',bool(test1)) 

test1 = [0]
print(test1,'is',bool(test1))    

test1 = None  
print(test1,'is',bool(test1))  

test1 = 'Easy string'  
print(test1,'is',bool(test1)) 

#sum(): Used to get the sum of numbers of an iterable, i.e., list.

list_1 = [1,2,4]  
s = sum(list_1)  
print(s)  
  
s = sum(list_1, 10)  
print(s) 

#len(): Returns the length (the number of items) of an object.

strA = 'Python'  
print(len(strA))  

#list() creates a list in python.
# empty list  

Gaurav = list()
print(Gaurav)  
  
#Converting string to list
String = 'abcde'       
print(list(String)) 

#divmod(): Used to get quotient and remainder of two numbers. 
#This function takes two numeric arguments and returns a tuple. 
#Both arguments are required and numeric 
# Calling function  
result = divmod(10,2)  
# Displaying result  
print(result)  

#dict(): Its a constructor which creates a dictionary. 
# Calling function  
result = dict() # returns an empty dictionary 
print(result)
 
result2 = dict(a=1,b=2)  
# Displaying result  
print(result2)  

#set(): It is used to create a new set using elements passed during the call. 
#It takes an iterable object as an argument and returns a new set object.
# Calling function  
result = set() # empty set  
result2 = set('12')  
result3 = set('javatpoint') 
result4 = {1,2}
print (result4)
# Displaying result  
print(result)  
print(result2)  
print(result3)  

#pow(): Used to compute the power of a number.
# positive x, positive y (x**y)  
print(pow(4, 2))  
  
# negative x, positive y  
print(pow(-4, 2))  

#tuple(): Used to create a tuple object.
t1 = tuple()  
print('t1=', t1)  
  
# creating a tuple from a list 
l =  [1, 6, 9]
t2 = tuple(l)  
print('t2=', t2)  
  
# creating a tuple from a string  
t1 = tuple('Java') 
print('t1=',t1)  

#----------------------------------------------------------------------
#lambda()- Helps creating anonymous functions. 
#Lambda functions can accept any number of arguments, 
#but they can return only one value in the form of expression.

#Multiple arguments to Lambda function
x = lambda a,b:a+b 
# a and b are the arguments and a+b is the expression which gets evaluated and returned.   
print("Addition = ",x(20,10)) 

#Program to filter out the list which contains numbers  divisible by 3.
List = [1,2,3,4,10,123,22]  
Oddlist = list(filter(lambda x:(x%3 == 0),List)) 
# the list contains all the items of the list for which the lambda function evaluates to true  
print(Oddlist) 

#program to triple each number of the list using map  
List = [1,2,3,4,10,123,22] 
new_list = list(map(lambda x:x*3,List)) 
# this will return the triple of each item of the list and add it to new_list  
print(new_list)  