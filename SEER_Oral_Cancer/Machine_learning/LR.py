# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:26:35 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a Logistic_regression model is built based on processed data without the use of any sampling techniques
Source: SEER_final_dataset.csv
"""
#A Logistic_regression model is built based on processed data without the use of any sampling techniques
#imported relevant packages
import pandas as pd 

#loading the csv file
df= pd.read_csv(r"file_path.csv")

#Defining the dependent and independent varibales 
X = df.iloc[:,:60]
y = df.iloc[:,60]


from sklearn.linear_model import LogisticRegression
model_grid = LogisticRegression()

#with GRid search
from sklearn.model_selection import GridSearchCV
parameters = {'max_iter':[2,5,10,20,200,2000],'random_state':[10,20,50]}

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

model = LogisticRegression(max_iter=2000)
model.fit(Xtrain, ytrain)

y_predict = model.predict(Xtest)

from sklearn.metrics import accuracy_score

print("Accuracy_Logistic Regression[0-1]: " , accuracy_score(ytest, y_predict))
from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.model_selection import cross_val_score
scores_logistic_regression= cross_val_score(model, X, y, cv=10)
print('Cross validation 10 fold scores for Logistic Regression:' , scores_logistic_regression)

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

print("Precision: ", precision_score(ytest, y_predict))
print("Recall: ", recall_score(ytest, y_predict))
from sklearn.metrics import f1_score
print('F1score: ', f1_score(ytest, y_predict))

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

from sklearn.metrics import roc_auc_score
print('Roc_AUC: ',roc_auc_score(ytest, y_predict))

print(np.mean(cross_val_score(model, X, y, cv=10)))
