#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#########################################################
from sklearn import tree
t0=time()
clf=tree.DecisionTreeClassifier(min_samples_split=40)
print 'creating classifier time: ',round(time()-t0,3),'s'


t1=time()
clf.fit(features_train, labels_train)
print 'training time: ',round(time()-t1,3),'s'

pred=clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracyDT=accuracy_score(pred,labels_test)
print 'accuracyDT=',accuracyDT
'''
the data is organized into a numpy array where
the number of rows is the number of data points
the number of columns is the number of features
'''
print len(features_train[0])


#########################################################
