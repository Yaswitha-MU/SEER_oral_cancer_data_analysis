'''
Date created- 10/12/2020
Last Modified Date - 18/02/2021
@author: Yaswitha Jampani
Purpose: This script is to get the significant relations between variables 
Source: SEER_final_dataset.csv
'''
mydata <- read.csv("C://Users//USER//Desktop//seer_Final_dataset.csv")

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
mylogit1 <- glm(Survival_status ~ mydata$Age.at.diagnosis, data = mydata, family = "binomial")
mylogit2 <- glm(Survival_status ~ mydata$Marital.status.at.diagnosis, data = mydata, family = "binomial")
mylogit3 <- glm(Survival_status ~ mydata$Race.recode..White..Black..Other., data = mydata, family = "binomial")
mylogit4 <- glm(Survival_status ~ mydata$Sex, data = mydata, family = "binomial")
mylogit5 <- glm(Survival_status ~ mydata$Primary.Site, data = mydata, family = "binomial")
mylogit6 <- glm(Survival_status ~ mydata$Grade, data = mydata, family = "binomial")
mylogit7 <- glm(Survival_status ~ mydata$Laterality, data = mydata, family = "binomial")
mylogit8 <- glm(Survival_status ~ mydata$Diagnostic.Confirmation, data = mydata, family = "binomial")
mylogit9 <- glm(Survival_status ~ mydata$Radiation.sequence.with.surgery, data = mydata, family = "binomial")
mylogit10 <- glm(Survival_status ~ mydata$Reason.no.cancer.directed.surgery, data = mydata, family = "binomial")
mylogit11 <- glm(Survival_status ~ mydata$Radiation.recode, data = mydata, family = "binomial")
mylogit12 <- glm(Survival_status ~ mydata$Chemotherapy.recode..yes..no.unk., data = mydata, family = "binomial")
mylogit13 <- glm(Survival_status ~ mydata$Sequence.number, data = mydata, family = "binomial")
mylogit14 <- glm(Survival_status ~ mydata$Regional.nodes.positive..1988.., data = mydata, family = "binomial")
mylogit15 <- glm(Survival_status ~ mydata$Total.number.of.in.situ.malignant.tumors.for.patient, data = mydata, family = "binomial")
mylogit16 <- glm(Survival_status ~ mydata$Total.number.of.benign.borderline.tumors.for.patient, data = mydata, family = "binomial")
mylogit17 <- glm(Survival_status ~ mydata$Tumor_size, data = mydata, family = "binomial")
mylogit18 <- glm(Survival_status ~ mydata$Histology, data = mydata, family = "binomial")


#OR(Odd's Ratio)
exp(mylogit1$coefficients[-1])
exp(mylogit2$coefficients[-1])
exp(mylogit3$coefficients[-1])
exp(mylogit4$coefficients[-1])
exp(mylogit5$coefficients[-1])
exp(mylogit6$coefficients[-1])
exp(mylogit7$coefficients[-1])
exp(mylogit8$coefficients[-1])
exp(mylogit9$coefficients[-1])
exp(mylogit10$coefficients[-1])
exp(mylogit11$coefficients[-1])
exp(mylogit12$coefficients[-1])
exp(mylogit13$coefficients[-1])
exp(mylogit14$coefficients[-1])
exp(mylogit15$coefficients[-1])
exp(mylogit16$coefficients[-1])
exp(mylogit17$coefficients[-1])
exp(mylogit18$coefficients[-1])


