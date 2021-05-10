# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:13:55 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a Random Forest model is built based on processed data without the use of any sampling techniques
Source: SEER_final_dataset.csv
"""
#A Random Forest model is built based on processed data without the use of any sampling techniques
#imported relevant packages
import pandas as pd 
import numpy as np

#loading the csv file
df= pd.read_csv(r"file_path.csv")

#Defining the dependent and independent varibales 
X = df.iloc[:,:60]
y = df.iloc[:,60]


from sklearn.ensemble import RandomForestClassifier
model_grid = RandomForestClassifier()

#with GRid search
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators': [5, 10, 15, 20],
               'max_features': ['log2', 'sqrt'],
               'max_depth': [10,200,5000],
               'criterion': ['gini', 'entropy']}
clf = GridSearchCV(model_grid, parameters)
clf.fit(X, y)
print(clf.best_params_)
print(clf.cv_results_['mean_test_score'])

from sklearn.model_selection import train_test_split
#Trying to use train_test_split method and evalaute the results
#Used the parameters that got with grid search

# split the data with 80% in train set and 20% in test set
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0,
                                                train_size=0.8)

model = RandomForestClassifier(n_estimators=10, max_depth=5000)
model.fit(Xtrain, ytrain)

y_predict = model.predict(Xtest)
from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

from sklearn.model_selection import cross_val_score
scores_RFC= cross_val_score(model, X, y, cv=10)
print('Cross validation 10 fold scores for RFC:' , scores_RFC)

print("Precision: ", precision_score(ytest, y_predict))
print("Recall: ", recall_score(ytest, y_predict))

from sklearn.metrics import confusion_matrix
# a confusion matrix metrics are recalled in the order of 
#1. True Negative
#2. False Positive
#3. False Negative
#4. True Positive

tn, fp, fn, tp = confusion_matrix(ytest, y_predict).ravel()
specificity = tn / (tn+fp)
print('specificity', specificity)

accuracy= (tp+tn)/(tp+tn+fn+fp)
print('Accuracy', accuracy)
from sklearn.metrics import f1_score
print('F1score: ', f1_score(ytest, y_predict))
from sklearn.metrics import roc_auc_score
print('Roc_AUC: ',roc_auc_score(ytest, y_predict))

print(np.mean(cross_val_score(model, X, y, cv=10)))

