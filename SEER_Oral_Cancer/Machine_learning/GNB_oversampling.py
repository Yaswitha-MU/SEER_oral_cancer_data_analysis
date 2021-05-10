# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:18:14 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a Gaussian Navie Bayes' model that was built based on processed data with the use of SMOTE over sampling techniques
Source: SEER_final_dataset.csv
"""
#A GNB model is built based on processed data with the use of SMOTE over sampling techniques
#imported relevant packages
import pandas as pd 

#loading the csv file
df= pd.read_csv(r"file_path.csv")

#This script is to transform the data into normal distribution by using SMOTE oversampling technique
from imblearn.over_sampling import SMOTE
dependent_variable_no= 60
seed=100
k=1
smote = SMOTE(sampling_strategy='auto',random_state=seed, k_neighbors=k )
x_fit, y_fit = smote.fit_resample(df.iloc[:,:dependent_variable_no],df.iloc[:,dependent_variable_no])
df = pd.concat([pd.DataFrame(x_fit), pd.DataFrame(y_fit)], axis=1

#Defining the dependent and independent varibales 
X = df.iloc[:,:dependent_variable_no]
y = df.iloc[:,dependent_variable_no]


from sklearn.naive_bayes import GaussianNB

#First trying to use train_test_split method and evalaute the results 
from sklearn.model_selection import train_test_split

# split the data with 80% in train set and 20% in test set
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=50,
                                                train_size=0.8)

model = GaussianNB()
model.fit(Xtrain, ytrain)

y_predict = model.predict(Xtest)


# Relevant metrics are calculated 
from sklearn.metrics import accuracy_score
print("Accuracy_GNB: " , accuracy_score(ytest, y_predict))
               
from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

from sklearn.model_selection import cross_val_score
scores_GNB= cross_val_score(model, X, y, cv=10)
print('Cross validation 10 fold scores for GNB:' , scores_GNB)

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

# since GNB is a basic model it doesn't have much hyperparameters to use the grid search 
