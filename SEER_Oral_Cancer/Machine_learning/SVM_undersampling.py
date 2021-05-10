# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 04:05:16 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to build a Support Vector Machine model is built based on processed data with the use of Edited KNN sampling techniques
Source: SEER_final_dataset_undersampling.csv
"""
# A SVM model is built based on processed data with the use of Edited KNN under-sampling techniques
# imported releant packages
import pandas as pd 


# loading the csv file
df= pd.read_csv(r"file_path.csv")

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

from sklearn.svm import SVC
model_grid = SVC()

# with GRid search
from sklearn.model_selection import GridSearchCV

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10, 20]}
clf = GridSearchCV(model_grid, parameters)
clf.fit(X, y)
print(clf.best_params_)
print(clf.cv_results_['mean_test_score'])
# from sklearn.datasets import make_classification


from sklearn.model_selection import train_test_split
# trying to use train_test_split method and evalaute the results
# used the parameters that got with grid search

# split the data with 80% in train set and 20% in test set
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0,
                                                train_size=0.8)

model = SVC(kernel='rbf')
model.fit(Xtrain, ytrain)

y_predict = model.predict(Xtest)

from sklearn.metrics import confusion_matrix
print (confusion_matrix(ytest, y_predict))

from sklearn.model_selection import cross_val_score
scores_SVM= cross_val_score(model, X, y, cv=10)
print('Cross validation 10 fold scores for SVM:' , scores_SVM)

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

print("Precision: ", precision_score(ytest, y_predict))
print("Recall: ", recall_score(ytest, y_predict))

from sklearn.metrics import confusion_matrix
# A confusion matrix metrics are recalled in the order of 
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
