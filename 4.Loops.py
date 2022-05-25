# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 18:51:52 2021

@author: 
"""
#--------------------------------Loops----------------------------------------
#-------------For Loop---------------
# for loop is used in case where we need to execute some part of the code until the given condition
# is satisfied. It is better to use for loop if the number of iteration is known in advance.
#It is frequently used to traverse the data structures like list, tuple, or dictionary.
#Example1:
i=0  
for i in range(0,10):
    print(i,end =',')

#Example2:printing the table of the given number
i=1
num = int(input("Enter a number:"))
for i in range(1,11):
    print("%a X %a = %a" %(num,i,num*i))

#Example3:Nested For loop
n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end="")

#Exampl4: Else statement with For loop
for i in range(0,5):
    print(i)
else:print("for loop completely exhausted, since there is no break.")

#------------While Loop-------------
# while loop is to be used in the scenario where we don't know the number of iterations in advance. 
#The block of statements is executed in the while loop until the condition specified in while loop 
#is satisfied. 
#Example1:
i=1;
while i<=10:
    print(i);
    i=i+1;

#Example2:
i=1
number=0

number = int(input("Enter the number?"))
while i<=10:
    print("%a X %a = %a \n"%(number,i,number*i));
    i = i+1;

#Example3:Infinite while loop
var = 1
while var != 2:
    i = int(input("Enter the number?"))
    print ("Entered value is %d"%(i))

while (1):
    print("Hi! we are inside the infinite while loop");

# For loop is ran finite no. of times even if we give only one value
for i in range(0,1):
    print("Hi! we are inside the finite for loop");

#Example4: Using else with while loop
i=1;
while i<=5:
    print(i)
    i=i+1;
else:print("The while loop exhausted");

#-------------If Statement----------------
#The if statement is used to test a specific condition. 
#If the condition is true, a block of code (if-block) will be executed.
#Exampl1:
num = int(input("enter the number?"))
if num%2 == 0:
    print("Number is even")

#Example2:
a = int(input("Enter a? "));
b = int(input("Enter b? "));
c = int(input("Enter c? "));
if a>b and a>c:
    print("a is largest");

if b>a and b>c:
    print("b is largest");

if c>a and c>b:
    print("c is largest");

#-----------If Else Statement-------------
#If the condition provided in the if statement is false, then the else statement will be executed.
#Example1:
age = int (input("Enter your age? "))
if age>=18:
    print("You are eligible to vote !!");
else:
    print("Sorry! you have to wait !!");

#Example2:
num = int (input("enter the number?"))
if num%2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")

#-------Elif Statement------------------
#The elif statement enables us to check multiple conditions and execute the specific block of 
#statements depending upon the true condition among them.It works like if-else-if ladder statement.
#Example:
number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50");
elif number==100:
    print("number is equal to 100");
else:
    print("number is not equal to 10, 50 or 100");
