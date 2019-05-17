#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
### your code goes here ###

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 


t0=time()


from sklearn.svm import SVC
'''
try different classifier
LinearSVC()
SVC(kernel='linear')
clf=SVC(kernel="rbf",C=10000)
----optimized c for the rbf kernel, try c=10,100,1000,10000
The bigger the c, the more complex the decision boundary is.More training data you are trying to make correct
'''
clf=SVC(kernel="rbf",C=10000)
print "training time:", round(time()-t0, 3), "s"

t1=time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t1, 3), "s"

pred=clf.predict(features_test)
from sklearn.metrics import accuracy_score
print accuracy_score(pred,labels_test)

'''
use trained classifier to make the prediction
'''
print clf.predict([features_test[10]])
print clf.predict([features_test[26]])
print clf.predict([features_test[50]])
"""
There are over 1700 test events  how many are predicted to be in the class 1? 
"""
print len(pred[pred==1])

#########################################################


