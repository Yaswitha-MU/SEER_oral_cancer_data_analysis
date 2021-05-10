# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:18:14 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a Gaussian Navie Bayes' model is built based on processed data without the use of any sampling techniques
Source: SEER_final_dataset.csv
"""

#A GNB model is built based on processed data without the use of any sampling techniques
#imported relevant packages
import pandas as pd 

#loading the csv file
df= pd.read_csv("file_path.csv")

#Defining the dependent and independent varibales 
X = df.iloc[:,:60]
y = df.iloc[:,60]


from sklearn.naive_bayes import GaussianNB

#First trying to use train_test_split method and evalaute the results 
from sklearn.model_selection import train_test_split

# split the data with 80% in train set and 20% in test set
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0,
                                                train_size=0.8)

model = GaussianNB()
model.fit(Xtrain, ytrain)

y_predict = model.predict(Xtest)

# Relevant metrics are calculated 
from sklearn.metrics import accuracy_score

print("Accuracy_GNB: " , accuracy_score(ytest, y_predict))
from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.model_selection import cross_val_score
scores_GNB= cross_val_score(model, X, y, cv=10)
print('Cross validation 10 fold scores for GNB:' , scores_GNB)

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

print("Precision: ", precision_score(ytest, y_predict))
print("Recall: ", recall_score(ytest, y_predict))
from sklearn.metrics import f1_score
print('F1score: ', f1_score(ytest, y_predict))

# a confusion matrix metrics are recalled in the order of 
#1. True Negative
#2. False Positive
#3. False Negative
#4. True Positive
from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(ytest, y_predict).ravel()
specificity = tn / (tn+fp)
print('specificity', specificity)

# Later ROC score is calculated 
from sklearn.metrics import roc_auc_score
print('Roc_AUC: ',roc_auc_score(ytest, y_predict))

 
# since GNB is a basic model it doesn't have much hyperparameters to use the grid search 


