#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import matplotlib.pyplot as plt

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# clf = MultinomialNB()
clf_ = GaussianNB()
# clf.fit(features_train, labels_train)
t0 = time()
clf_.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")
# predicted = clf.predict(features_test)
t1 = time()
predicted_ = clf_.predict(features_test)
print("prdicting time:", round(time()-t1, 3), "s")

# print('Predicted Labels: ', predicted)
# print('MultinomialNB Model Prediction Accuracy (proportion): ', accuracy_score(labels_test, predicted))
print('GaussianNB Model Prediction Accuracy (proportion): ', accuracy_score(labels_test, predicted_))


#########################################################
