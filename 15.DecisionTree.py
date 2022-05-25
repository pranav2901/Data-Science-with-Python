# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:48:32 2021

@author: Admin
"""

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('F:\WORK\pyWork\AnalyticsEdge_Python\pyData\Purchase_History.csv')

#Method-1 (Handling Categorical Variables)
pd.get_dummies(dataset["Gender"])
pd.get_dummies(dataset["Gender"],drop_first=True)
S_Dummy = pd.get_dummies(dataset["Gender"],drop_first=True)
S_Dummy.head(5)
#Now, lets concatenate these dummy var columns in our dataset.
dataset = pd.concat([dataset,S_Dummy],axis=1)
dataset.head(5)
dataset.tail(2)
#dropping the columns whose dummy var have been created
dataset.drop(["Gender",],axis=1,inplace=True)
dataset.head(5)
#------------------------------------------------------------------------------

#Obtaining DV & IV from the dataset
X = dataset.iloc[:, [1,2,4]].values
y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 2)


# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
#classifier = DecisionTreeClassifier(criterion = 'entropy')
#If desired we can supply extra parameters to decision trees fxn, but 
#it may or may not give better accuracy.                                    
classifier = DecisionTreeClassifier(criterion = 'entropy',max_depth = 3, min_samples_leaf=5)

classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
#Accuracy = 91%

# Decision Tree visualization-----------------
from sklearn import tree

#Simple Decision Tree
tree.plot_tree(classifier)
#image is quite blurred

#Lets try to make decision tree more interpretable by adding filling colors.
tree.plot_tree(classifier,filled = True)
#Although the Decision tree shows class name & leafs are colred but still its view is blurred.

#Lets create a blank chart of desired size using matplotlib library and place our Decision tree there.
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
#The above line is used to set the pixels of the Decision Trees nodes so that
#the content mentioned in each node of Decision tree is visible.
cn=['0','1']
tree.plot_tree(classifier,class_names=cn,filled = True)

#if you want save figure, use savefig method in returned figure object.
fig.savefig('Skilledge-Python-April-batch.png')
