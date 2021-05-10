# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:13:55 2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to create the dependent variable and clean the data set appropriately
Source: SEER_final_dataset.csv
"""

#imported relevant packages
import pandas as pd 

#loading the csv file
df= pd.read_csv(r"file_path.csv")

# Merging the tumor size columns 
df["Tumor_size"]= ""
for index,row in df.iterrows():
    print(index/len(df.index))
    if row["Year of diagnosis"]>=1983 and row["Year of diagnosis"]<=1987 :
        df.at[index,"Tumor_size"]= row["EOD 4 - size (1983-1987)"]
    elif row["Year of diagnosis"]>=1988 and row["Year of diagnosis"]<=2003 :
        df.at[index,"Tumor_size"]= row["EOD 10 - size (1988-2003)"]
    elif row["Year of diagnosis"]>=2004 and row["Year of diagnosis"]<=2015 :
        df.at[index,"Tumor_size"]= row["CS tumor size (2004-2015)"]
    else:
        df.at[index,"Tumor_size"]= row["Tumor Size Summary (2016+)"]

#creating the histology column and coding based on histopathology type squamous cell carcinoma as 1 and others 0
df['Histology']=''
for index,row in df.iterrows():
    print(index)
    print(index/len(df.index))
  
    if row["ICD-O-3 Hist/behav"]== '8084/3: Squamous cell carcinoma, clear cell type':
        df.at[index,"Histology"]= 1
    elif row["ICD-O-3 Hist/behav"]== ' 8076/3: Squamous cell carcinoma, micro-invasive':
        df.at[index,"Histology"]= 1
    elif row["ICD-O-3 Hist/behav"]== '8074/3: Squamous cell carcinoma, spindle cell':
        df.at[index,"Histology"]= 1
   
    elif row["ICD-O-3 Hist/behav"]== ' 8070/3: Squamous cell carcinoma, NOS':
        df.at[index,"Histology"]= 1
    elif row["ICD-O-3 Hist/behav"]== '8071/3: Squamous cell carcinoma, keratinizing, NOS':
        df.at[index,"Histology"]= 1
    elif row["ICD-O-3 Hist/behav"]== '8072/3: Squamous cell carcinoma, large cell, nonkeratinizing, NOS':
        df.at[index,"Histology"]= 1
    
    elif row["ICD-O-3 Hist/behav"]== '8073/3: Squamous cell carcinoma, small cell, nonkeratinizing':
        df.at[index,"Histology"]= 1
    
    elif row["ICD-O-3 Hist/behav"]== ' 8075/3: Squamous cell carcinoma, adenoid':
        df.at[index,"Histology"]= 1
    else:
        df.at[index,"Histology"]= 0

# Creating dependent variable from few variables like vital status, COD, Survival months and Follow up
#If survived Yes=1 and No=0
df["Survival_status"]= ""
for index,row in df.iterrows():
    print(index/len(df.index))
    if row["Type of follow-up expected"]== 1:
        df.at[index,"Survival_status"]="NA"
    elif row["Type of follow-up expected"]== 2 and row["Survival months"]<=60 and row["SEER cause-specific death classification"]== 1:
        df.at[index,"Survival_status"]=0
    elif row["Type of follow-up expected"]== 4 and row["Survival months"]<=60 and row["SEER cause-specific death classification"]== 1:
        df.at[index,"Survival_status"]=0
    elif row["Survival months"]==60 and row["Vital status recode (study cutoff used)"]== 1:
        df.at[index,"Survival_status"]=1
    elif row["Survival months"]>60 and row["Type of follow-up expected"]== 2 or 4 :
        df.at[index,"Survival_status"]=1
    else:
        df.at[index,"Survival_status"]="NA"

#Dropping unwanted columns and rows with least clinical importance and null values 
df2=df.drop(['CS tumor size (2004-2015)',"ICD-O-3 Hist/behav",'Year of diagnosis', 'EOD 10 - size (1988-2003)',"Tumor Size Summary (2016+)","EOD 4 - size (1983-1987)",'Regional nodes examined (1988+)','Site recode ICD-O-3/WHO 2008', 'Primary Site - labeled','Race/ethnicity', 'Type of follow-up expected', 'SEER cause-specific death classification',"Vital status recode (study cutoff used)","Survival months"], axis=1)
data= df2[(df2['Race recode (White, Black, Other)']== 9) |(df2['Marital status at diagnosis']== 9)| (df2['Grade']== 9) |(df2['Grade']== 5) |(df2['Grade']== 6) |(df2['Grade']== 7) |(df2['Grade']== 8) | (df2['Laterality']== 9) | (df2['Diagnostic Confirmation']== 9) | (df2['Behavior code ICD-O-3']== 0) | (df2['Reason no cancer-directed surgery']== 9) | (df2['Radiation recode']== 0) |(df2['Radiation recode']== 8) | (df2['Sequence number']== 60) | (df2['Sequence number']== 61) | (df2['Sequence number']== 62) |(df2['Sequence number']== 63) | (df2['Sequence number']== 64) | (df2['Sequence number']== 65) | (df2['Sequence number']== 66) | (df2['Sequence number']== 67) | (df2['Sequence number']== 68) | (df2['Sequence number']== 69) | (df2['Sequence number']== 70) | (df2['Sequence number']== 75) |(df2['Sequence number']== 88) | (df2['Sequence number']== 99) | (df2['First malignant primary indicator']== 0) | (df2['Total number of in situ/malignant tumors for patient']== 99) | (df2['Total number of benign/borderline tumors for patient']== 99)|(df2['Regional nodes positive (1988+)']== 'Blank(s)')|(df2['Tumor_size']== 'Blank(s)')].index
df2.drop(data, inplace = True)


# converting primary site into categorial variables with less codes
df4=df2
for index,row in df4.iterrows():
    print(index)
    print(index/len(df4.index))
  
    if row["Primary Site"]== 0 or row["Primary Site"]== 1 or row["Primary Site"]== 2 or row["Primary Site"]== 3 or row["Primary Site"]== 4 or row["Primary Site"]== 5 or row["Primary Site"]== 6 or row["Primary Site"]== 8 or row["Primary Site"]== 9: 
   
        df4.at[index,"Primary Site"]= 1
    
    elif row["Primary Site"]== 19 or row["Primary Site"]== 20 or row["Primary Site"]== 21 or row["Primary Site"]== 22 or row["Primary Site"]== 23 or row["Primary Site"]== 24 or row["Primary Site"]== 25 or row["Primary Site"]== 26  or row["Primary Site"]== 28 or row["Primary Site"]== 29 :
        df4.at[index,"Primary Site"]= 2
   
    elif row["Primary Site"]== 30 or row["Primary Site"]== 31 or row["Primary Site"]== 39 :
        df4.at[index,"Primary Site"]= 2
   
    elif row["Primary Site"]== 40 or row["Primary Site"]== 41  or row["Primary Site"]== 48 or row["Primary Site"]== 49:
        df4.at[index,"Primary Site"]= 2
    elif row["Primary Site"]== 50 or row["Primary Site"]== 51 or row["Primary Site"]== 52 or row["Primary Site"]== 58 or row["Primary Site"]== 59:
        df4.at[index,"Primary Site"]= 2
    
    elif row["Primary Site"]== 60 or row["Primary Site"]== 61 or row["Primary Site"]== 62 or row["Primary Site"]== 68 or row["Primary Site"]== 69: 
        df4.at[index,'Primary Site']= 2
        
    elif row["Primary Site"]== 79 or row["Primary Site"]== 80 or row["Primary Site"]== 81 or row["Primary Site"]== 88 or row["Primary Site"]== 89:
        df4.at[index,"Primary Site"]= 3
    
    elif row["Primary Site"]== 90 or row["Primary Site"]== 91 or row["Primary Site"]== 98 or row["Primary Site"]== 99 :
        df4.at[index,"Primary Site"]= 3
    
    elif row["Primary Site"]== 100 or row["Primary Site"]== 101 or row["Primary Site"]== 102 or row["Primary Site"]== 103 or row["Primary Site"]== 104 or row["Primary Site"]== 108 or row["Primary Site"]== 109 or row["Primary Site"]== 110 or row["Primary Site"]== 111 or row["Primary Site"]== 112 or row["Primary Site"]== 113 or row["Primary Site"]== 118 or row["Primary Site"]== 119 or row["Primary Site"]== 129 or row["Primary Site"]== 130 or row["Primary Site"]== 131 or row["Primary Site"]== 132 or row["Primary Site"]== 138 or row["Primary Site"]== 139:
        
    
        df4.at[index,"Primary Site"]= 4
    
    else:

        df4.at[index,"Primary Site"]= 9

df5= df4
for index,row in df5.iterrows():
    print(index/len(df5.index))
    if row["Age recode with <1 year olds"]== '00 years' or row["Age recode with <1 year olds"]== '1-4 years' or row["Age recode with <1 year olds"]== '5-9 years' or row["Age recode with <1 year olds"]== '10-14 years' or row["Age recode with <1 year olds"]== '15-19 years' or row["Age recode with <1 year olds"]== '20-24 years' or row["Age recode with <1 year olds"]== '25-29 years':
        df5.at[index,"Age recode with <1 year olds"]= 0
    elif row["Age recode with <1 year olds"]== '30-34 years' or row["Age recode with <1 year olds"]== '35-39 years' or row["Age recode with <1 year olds"]== '40-44 years' or row["Age recode with <1 year olds"]== '45-49 years':
        df5.at[index,"Age recode with <1 year olds"]= 1
    elif row["Age recode with <1 year olds"]== '50-54 years' or row["Age recode with <1 year olds"]== '55-59 years' or row["Age recode with <1 year olds"]== '60-64 years' or row["Age recode with <1 year olds"]== '65-69 years':
        df5.at[index,"Age recode with <1 year olds"]= 2
        
    else:
        df5.at[index,"Age recode with <1 year olds"]= 3
'''
df6=df4
for index,row in df6.iterrows():
    print(index/len(df6.index))
    if row["Age at diagnosis"] >=0 and row["Age at diagnosis"] <=29:
        df6.at[index,"Age at diagnosis"]= 0
    elif row["Age at diagnosis"] >=30 and row["Age at diagnosis"] <=59:
        df6.at[index,"Age at diagnosis"]= 1
        
    else:
        df6.at[index,"Age at diagnosis"]= 2
'''
df5.to_csv(r"file_path.csv")
