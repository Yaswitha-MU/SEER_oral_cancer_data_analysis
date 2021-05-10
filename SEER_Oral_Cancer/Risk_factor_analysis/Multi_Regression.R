'''
Date created- 10/12/2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to get the significant relations between variables 
Source: SEER_final_dataset.csv

'''
mydata <- read.csv("dataset.csv")

#calling categorical variables 
mydata$Marital.status.at.diagnosis <- as.factor(mydata$Marital.status.at.diagnosis)
mydata$Race.recode..White..Black..Other. <- as.factor(mydata$Race.recode..White..Black..Other.)
mydata$Sex <- as.factor(mydata$Sex)
mydata$Primary.Site <- as.factor(mydata$Primary.Site)
mydata$Grade <- as.factor(mydata$Grade)
mydata$Laterality <- as.factor(mydata$Laterality)
mydata$Diagnostic.Confirmation <- as.factor(mydata$Diagnostic.Confirmation)
mydata$Radiation.sequence.with.surgery <- as.factor(mydata$Radiation.sequence.with.surgery)
mydata$Reason.no.cancer.directed.surgery <- as.factor(mydata$Reason.no.cancer.directed.surgery)
mydata$Radiation.recode <- as.factor(mydata$Radiation.recode)
mydata$Chemotherapy.recode..yes..no.unk. <- as.factor(mydata$Chemotherapy.recode..yes..no.unk.)
mydata$Histology <- as.factor(mydata$Histology)

#fitting the model 
mylogit1 <- glm(Survival_status ~ Age.at.diagnosis + Marital.status.at.diagnosis+ Race.recode..White..Black..Other.+ Sex+ Primary.Site+ Grade+ Laterality+ Diagnostic.Confirmation+ Radiation.sequence.with.surgery+ Reason.no.cancer.directed.surgery+Radiation.recode+Chemotherapy.recode..yes..no.unk.+Sequence.number+Regional.nodes.positive..1988..+Total.number.of.in.situ.malignant.tumors.for.patient+Total.number.of.benign.borderline.tumors.for.patient+Tumor_size+Histology , data = mydata, family = "binomial")

#getting summary statistics 
summary(mylogit1)
#OR
exp(mylogit1$coefficients[-1])

#RR
mylogit1 <- glm(Survival_status ~ Age.at.diagnosis + Marital.status.at.diagnosis+ Race.recode..White..Black..Other.+ Sex+ Primary.Site+ Grade+ Laterality+ Diagnostic.Confirmation+ Radiation.sequence.with.surgery+ Reason.no.cancer.directed.surgery+Radiation.recode+Chemotherapy.recode..yes..no.unk.+Sequence.number+Regional.nodes.positive..1988..+Total.number.of.in.situ.malignant.tumors.for.patient+Total.number.of.benign.borderline.tumors.for.patient+Tumor_size+Histology , data = mydata, family = "binomial")
exp(coef(mylogit1))[-1]
