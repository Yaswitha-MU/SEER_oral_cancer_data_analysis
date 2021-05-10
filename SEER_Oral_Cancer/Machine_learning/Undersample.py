# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:39:49 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to transform the data into normal distribution by using EditedNearestNeighbours undersampling technique
Source: SEER_final_dataset.csv
"""
import pandas as pd
#from imblearn.under_sampling import EditedNearestNEighbours

df= pd.read_csv(r"file_path.csv")

x = df.iloc[:,:60]
y = df.iloc[:,60]


from collections import Counter
from imblearn.under_sampling import EditedNearestNeighbours

# define dataset

# summarize class distribution
counter = Counter(y)
print(counter)
# define the undersampling method
undersample = EditedNearestNeighbours(n_neighbors=3)
# transform the dataset
x, y = undersample.fit_resample(x, y)
# summarize the new class distribution
counter = Counter(y)

df = pd.concat([pd.DataFrame(x), pd.DataFrame(y)], axis=1)
df.to_csv(r"file_path.csv", index=False, encoding='utf-8')
