
#Date created- 10/12/2020
#Last Modified Date - 18/02/2021
#@author: Yaswitha Jampani
#Purpose: This script is to get the summary statistics of the variables 
#Source: SEER_final_dataset.csv

# Here the list of numerical variables and the script written for getting their summary of descriptive statistics
#Age at diagnosis
select "Survival_status", min("Age at diagnosis"), max("Age at diagnosis"), avg("Age at diagnosis"), median("Age at diagnosis"),stddev("Age at diagnosis")
from seer
group by "Survival_status"

#Tumor size
select "Survival_status", min("Tumor_size"), max("Tumor_size"), avg("Tumor_size"), median("Tumor_size"),stddev("Tumor_size")
from seer
group by "Survival_status"

# Sequence number
select "Survival_status", min("Sequence number"), max("Sequence number"), avg("Sequence number"), median("Sequence number"),stddev("Sequence number")
from seer
group by "Survival_status"

#Number of malignant tumors count
select "Survival_status", min("Total number of in situ/malignant tumors for patient"), max("Total number of in situ/malignant tumors for patient"),
avg("Total number of in situ/malignant tumors for patient"), median("Total number of in situ/malignant tumors for patient"), 
stddev("Total number of in situ/malignant tumors for patient")
from seer
group by "Survival_status"

#Number of benign tumors count
select "Survival_status", min("Total number of benign/borderline tumors for patient"), max("Total number of benign/borderline tumors for patient"),
avg("Total number of benign/borderline tumors for patient"), median("Total number of benign/borderline tumors for patient"), 
stddev("Total number of benign/borderline tumors for patient")
from seer
group by "Survival_status"

#Regional nodes positive count
select "Survival_status", min("Regional nodes positive (1988+)"), max("Regional nodes positive (1988+)"), avg("Regional nodes positive (1988+)"),
median("Regional nodes positive (1988+)"),stddev("Regional nodes positive (1988+)")
from seer
group by "Survival_status"

