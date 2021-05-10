# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:13:55 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to drop the irrelevant columns and create dummy variables for predcitive modelling
Source: SEER_final_dataset.csv
"""
#imported relevant packages
import pandas as pd 

#loading the csv file
df= pd.read_csv(r"file_path.csv")

df1=df.drop(df[(df['Regional nodes positive (1988+)']== 95) |(df['Regional nodes positive (1988+)']== 98)| (df['Regional nodes positive (1988+)']== 97)|(df['Regional nodes positive (1988+)']== 99)| (df['Tumor_size']== 888)|(df['Tumor_size']== 1)|(df['Tumor_size']== 989)|(df['Tumor_size']== 991)|(df['Tumor_size']== 992)|(df['Tumor_size']== 993)|(df['Tumor_size']== 994)|(df['Tumor_size']== 995)|(df['Tumor_size']== 996)|(df['Tumor_size']== 000)|(df['Tumor_size']== 990)|(df['Tumor_size']== 999)].index)


#df1.drop(df1[(df1['Survival_status']=='NA')].index,inplace = True)


#df2=pd.get_dummies(df,columns=['Marital status at diagnosis','Race recode (White, Black, Other)','Sex','Primary Site','Grade','Laterality','Diagnostic Confirmation','Behavior code ICD-O-3','Radiation sequence with surgery','Reason no cancer-directed surgery','Radiation recode','Chemotherapy recode (yes, no/unk)','First malignant primary indicator','Histology'])

df1.to_excel(r"file_path.csv")



