# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:13:55 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to create the dummy varaibles 
Source: SEER_final_dataset.csv
"""


import pandas as pd 

#loading the csv file
df= pd.read_csv(r"file_path.csv")
df2=pd.get_dummies(df,columns=['Marital status at diagnosis','Race recode (White, Black, Other)','Sex','Primary Site','Grade','Laterality','Diagnostic Confirmation','Behavior code ICD-O-3','Radiation sequence with surgery','Reason no cancer-directed surgery','Radiation recode','Chemotherapy recode (yes, no/unk)','First malignant primary indicator','Histology'])
df=pd.concat([df2,df['Survival_status']],axis=1)
df.to_csv(r"file_path.csv")
