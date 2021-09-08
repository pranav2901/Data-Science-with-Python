# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:32:15 2021

@author: Admin
"""
import matplotlib.pyplot as plt
#-----------------------------------GRAPHS---------------------------------

#--------------------------Bar Chart------------------------------------------
#Vertical Bar Chart
import numpy as np
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Happiness_Index=[60,40,70,65,85]
 
plt.bar(city,Happiness_Index,color='pink',edgecolor='red')
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Barchart - Happiness index across cities',fontsize=20)

#Horizontal Bar Chart
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Happiness_Index=[60,40,70,65,85]
 
plt.barh(city,Happiness_Index,color='blue',edgecolor='black')
plt.xlabel('Happiness_Index', fontsize=16)
plt.ylabel('City', fontsize=16)
plt.title('Horizontal Barchart - Happiness index across cities',fontsize=20)

#Stacked Bar Chart in Python with legends:
 
city=['Delhi','Beijing','Washington','Tokyo','Moscow']
Gender=['Male','Female']
Happiness_Index_Male=[60,40,70,65,85]
Happiness_Index_Female=[30,60,70,55,75]
 
plt.bar(city,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(city,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male)
#bar() function plots the Happiness_Index_Female on top of Happiness_Index_Male with the help of 
#argument  bottom=Happiness_Index_Male.
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Stacked Barchart - Happiness index across cities',fontsize=18)
plt.legend(Gender,loc=2)

#--------------------------Histogram-------------------------------------------
#Histogram with no Fills:

values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,5, histtype='step', align='mid', color='green', label='Test Score Data')
#Here, second argument is the number of bins, 
#histype=’step’: it plots the histogram in step,
#format, aligned to mid, color chosen is green.
plt.legend(loc=2)
#argument loc=2 plots the legend on the top left corner.
plt.title('Histogram of score')

#Histogram with bar Filled:
 
values = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
plt.hist(values,10, histtype='bar', color='cyan', label='Test score Data',edgecolor='black')
#Argument histype=’bar’ plots the histogram in bar filled format.
plt.legend()
plt.title('Histogram of score')

#----------------------------Box Plot------------------------------------------
#Box Plot

value1=[82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]

box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data)

#Box plot with fills and labels:

value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]

box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data,patch_artist=True,labels=['course1','course2','course3','course4'])
#argument "patch_artist=True", fills the boxplot and argument "label" takes label to be plotted.

#Horizontal box plot in python with different colors:

value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]

box_plot_data=[value1,value2,value3,value4]
box=plt.boxplot(box_plot_data,vert=0,patch_artist=True,
                labels=['course1','course2','course3','course4'],)
#Adding argument vert =0 plots the horizontal box plot.
colors = ['cyan', 'lightblue', 'lightgreen', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
#Colors array takes four different colors and passes them to four different boxes of the boxplot
#with patch.set_facecolor() function.
#-------------------Line plot or Line chart --------------------

values = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9]
plt.plot(values)


#Multiple Line charts with legends and Labels:
#lets take an example of sale of units in 2016 and 2017 to demonstrate line charts.

sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot( sales1,range(1,12))
line_chart2 = plt.plot( sales2,range(1,12))
plt.title('Monthly sales of 2016 and 2017')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.legend(['year 2016', 'year 2017'], loc=4)


#Charts with different line styles:

sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
line_chart1 = plt.plot(range(1,12), sales1,'--')
line_chart2 = plt.plot(range(1,12), sales2,':')
plt.title('Monthly sales of 2016 and 2017')


#---------------------Pie Chart--------------------------------------------
#Pie chart in Python with legends:

values = [60, 80, 90, 55, 10, 30]
Col = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
Exp = (0.5, 0, 0, 0, 0, 0)
plt.pie(values, colors=Col, labels= values,explode=Exp,counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)

#Pie chart in Python with percentage values:

values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%', shadow=True)
plt.title('Population Density Index')

#-------------------------------Scatter Plot----------------------------------
# Scatter plot in Python:

weight1=[63.3,57,64.3,63,71,61.8,62.9,65.6,64.8,63.1,68.3,69.7,65.4,66.3,60.7]
height1=[156.3,100.7,114.8,156.3,237.1,123.9,151.8,164.7,105.4,136.1,175.2,137.4,164.2,151,124.3]
plt.scatter(weight1,height1,c='r',marker='*')
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('scatter plot - height vs weight',fontsize=20)

#Scatter plot for three different groups
 
weight1=[57,58.2,58.6,59.6,59.8,60.2,60.5,60.6,60.7,61.3,61.3,61.4,61.8,61.9,62.3]
height1=[100.7,195.6,94.3,127.1,111.7,159.7,135,149.9,124.3,112.9,176.7,110.2,123.9,161.9,107.8]
 
weight2=[62.9,63,63.1,63.2,63.3,63.4,63.4,63.4,63.5,63.6,63.7,64.1,64.3,64.3,64.7,64.8,65]
height2=[151.8,156.3,136.1,124.2,156.3,130,181.2,255.9,163.1,123.1,119.5,179.9,114.8,174.1,108.8,105.4,141.4]
 
 
weight3=[69.2,69.2,69.4,69.7,70,70.3,70.8,71,71.1,71.7,71.9,72.4,73,73.1,76.2]
height3=[166.8,172.9,193.8,137.4,162.4,137.1,169.1,237.1,189.1,179.3,174.8,213.3,198,191.1,220.6]
 
import numpy as np
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
 
color_array = ['b'] * 15 + ['g'] * 17 + ['r'] * 15
 
plt.scatter(weight, height, marker='*', c=color_array)

plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('grouped scatter plot - height vs weight',fontsize=20)