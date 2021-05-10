# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:57:22 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to transform the data into normal distribution by using SMOTE oversampling technique
Source: SEER_final_dataset.csv
"""
import pandas as pd
from imblearn.over_sampling import SMOTE

df= pd.read_csv(r"file_path.csv")
seed=100
k=1
x = df.iloc[:,:60]
y = df.iloc[:,60]

smt = SMOTE(sampling_strategy='auto',random_state=seed, k_neighbors=k )
x_res, y_res = smt.fit_resample(x, y)
df = pd.concat([pd.DataFrame(x_res), pd.DataFrame(y_res)], axis=1)
df.to_csv(r"file_path.csv", index=False, encoding='utf-8')
