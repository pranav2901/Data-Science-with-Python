# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:15:52 2021

@author: Admin
"""
#------------------------------Random Forest--------------------------------
# Random Forest Classification

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Purchase_History.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy',max_depth = 3, min_samples_leaf=5)
classifier.fit(X_train, y_train)

#To see no. of decision trees created
len(classifier.estimators_)

#To see the decision trees created
classifier.estimators_

#To access a particular decision tree, we can use indexing
classifier.estimators_[0]

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm
#Accuracy = 96%

# Random Forest visualization

#Since RF is quite big & clumpsy to draw due to large no. of DT, its not possible to 
#visualiza an entire RF on a small system like our laptop.
#Hence, we visualize individual DTs from this RF.

# Decision Tree -1 visualization-----------------
from sklearn import tree
#Lets create a blank chart of desired size using matplotlib library and place our Decision tree there.
import matplotlib.pyplot as plt
fig, axes= plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
cn=['0','1']
tree.plot_tree(classifier.estimators_[0],class_names=cn,filled = True)

#if you want save figure, use savefig method in returned figure object.
fig.savefig('RF-DT-1.png')

# Decision Tree-2 visualization-----------------
from sklearn import tree
#Lets create a blank chart of desired size using matplotlib library and place our Decision tree there.
import matplotlib.pyplot as plt
fig, axes= plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
cn=['0','1']
tree.plot_tree(classifier.estimators_[1],class_names=cn,filled = True)

#if you want save figure, use savefig method in returned figure object.
fig.savefig('RF-DT-2.png')

#-----------