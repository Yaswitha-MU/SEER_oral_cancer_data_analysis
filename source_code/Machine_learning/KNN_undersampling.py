# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:23:26 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a K-Nearest Neighbhor model is built based on processed data with the use of under sampling techniques
Source: SEER_final_dataset.csv
"""
# A KNN model is built based on processed data with the use of under sampling techniques
# imported relevant packages
import pandas as pd 

# loading the file
df= pd.read_csv(r"C:\Users\USER\Desktop\seer_Final_dataset_under.csv")

# this script is to transform the data into normal distribution by using EditedNearestNeighbours undersampling technique
from collections import Counter
from imblearn.under_sampling import EditedNearestNeighbours

# define dataset
# summarize class distribution
dependent_variable_no= 60
counter = Counter(df.iloc[:,dependent_variable_no])
print(counter)
# define the undersampling method
undersample = EditedNearestNeighbours(n_neighbors=3)
# transform the dataset
X_fit, y_fit = undersample.fit_resample(df.iloc[:,:dependent_variable_no],df.iloc[:,dependent_variable_no])
df = pd.concat([pd.DataFrame(X_fit), pd.DataFrame(y_fit)], axis=1)

# defining the dependent and independent varibales 
X = df.iloc[:,:dependent_variable_no]
y = df.iloc[:,dependent_variable_no]


from sklearn.neighbors import KNeighborsClassifier
model_1 = KNeighborsClassifier()

# with GRid search
from sklearn.model_selection import GridSearchCV
parameters = {'n_neighbors':[2,5,10,20,200]}
clf = GridSearchCV(model_1, parameters)
clf.fit(X, y)
print(clf.best_params_)
print(clf.cv_results_['mean_test_score'])

from sklearn.model_selection import train_test_split
# trying to use train_test_split method and evalaute the results
# used the parameters that got with grid search

# split the data with 80% in train set and 20% in test set
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0,
                                                train_size=0.8)

model_2 = KNeighborsClassifier(n_neighbors=2)
model_2.fit(Xtrain, ytrain)

y_predict = model_2.predict(Xtest)

from sklearn.metrics import accuracy_score

print("Accuracy_KNN[0-1]: " , accuracy_score(ytest, y_predict))
from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.model_selection import cross_val_score
scores_KNN= cross_val_score(model_2, X, y, cv=10)
print('Cross validation 10 fold scores for KNN:' , scores_KNN)

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

print("Precision: ", precision_score(ytest, y_predict))
print("Recall: ", recall_score(ytest, y_predict))
from sklearn.metrics import f1_score
print('F1score: ', f1_score(ytest, y_predict))

from sklearn.metrics import confusion_matrix

# A confusion matrix metrics are recalled in the order of 
#1. True Negative
#2. False Positive
#3. False Negative
#4. True Positive

tn, fp, fn, tp = confusion_matrix(ytest, y_predict).ravel()
specificity = tn / (tn+fp)
print('specificity', specificity)

Accuracy= (tp+tn)/(tp+tn+fn+fp)
print('Accuracy', Accuracy)

from sklearn.metrics import roc_auc_score
print('Roc_AUC: ',roc_auc_score(ytest, y_predict))
print(np.mean(cross_val_score(model, X, y, cv=10)))

