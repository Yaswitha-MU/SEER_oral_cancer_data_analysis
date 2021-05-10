# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:19:38 2020

@author: USER
"""
import pandas as pd 
df= pd.read_csv(r"C:\Users\USER\Desktop\seer_preprocessed.csv")

df1=df.drop(df[(df['Regional nodes positive (1988+)']== 95) |(df['Regional nodes positive (1988+)']== 98)| (df['Regional nodes positive (1988+)']== 97)|(df['Regional nodes positive (1988+)']== 99)| (df['Tumor_size']== 888)|(df['Tumor_size']== 1)|(df['Tumor_size']== 989)|(df['Tumor_size']== 991)|(df['Tumor_size']== 992)|(df['Tumor_size']== 993)|(df['Tumor_size']== 994)|(df['Tumor_size']== 995)|(df['Tumor_size']== 996)|(df['Tumor_size']== 000)|(df['Tumor_size']== 990)|(df['Tumor_size']== 999)].index)


#df1.drop(df1[(df1['Survival_status']=='NA')].index,inplace = True)


#df2=pd.get_dummies(df,columns=['Marital status at diagnosis','Race recode (White, Black, Other)','Sex','Primary Site','Grade','Laterality','Diagnostic Confirmation','Behavior code ICD-O-3','Radiation sequence with surgery','Reason no cancer-directed surgery','Radiation recode','Chemotherapy recode (yes, no/unk)','First malignant primary indicator','Histology'])

df1.to_excel(r"C:\Users\USER\Desktop\seer_Final_dataset.xlsx")



