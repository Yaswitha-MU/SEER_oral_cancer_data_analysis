# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:58:52 2020

@author: USER
"""
import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv(r"C:\Users\USER\Desktop\seer_Final_dataset.csv")
df2=pd.get_dummies(df,columns=['Marital status at diagnosis','Race recode (White, Black, Other)','Sex','Primary Site','Grade','Laterality','Diagnostic Confirmation','Behavior code ICD-O-3','Radiation sequence with surgery','Reason no cancer-directed surgery','Radiation recode','Chemotherapy recode (yes, no/unk)','First malignant primary indicator','Histology'])
df=pd.concat([df2,df['Survival_status']],axis=1)
df.to_csv(r"C:\Users\USER\Desktop\seer_Final_dataset_dummy.csv")
