## Five-Year Survivability of Lip, Oral Cavity, and Pharyngeal Cancer: A Risk Factor Analysis and Predictive Machine Learning Approach using SEER Database
### Overview
This project mainly focused on analyzing the five-year Lip, Oral cavity and Pharyngeal cancer survival using the national cnacer registry data; SEER. This data set has the following advantages: (a) the data collected accounts for 35% of the American population, and (b) it consists of information about demographics, tumor characteristics, and geographic locations. Based on the literarture review we found that there is a need for extensive research in these cancer types using a large amount of data like SEER national cancer registry. Our study contributes to the existing literature by assessing and listing down all the possible risk factors for cancer survivability and providing a better cancer survivability prediction model using SEER Lip, Oral cavity, and Pharyngeal cancer data. Our main objectives are :-( a) performing risk factor analysis to understand the variable co-relation with cancer survival, (b) building predictive models for assessing the five-year cancer survivability and, (c) evaluation and comparison of predictive model performances. 

In this project folder you can anticipate the our data processing, data analysis source codes. A descriptive statistics summary was performed using SQL and a cross verification was done using RStudio. Also, this project involved simple and multiple logistic regression analysis to assesses the effect of the different variables on five-year cancer survivability. Odds-ratios were calculated for each of the patient-related risk factors. R-studio was used for performing the above risk factor analysis. Later, six supervised classification models were built using the following algorithms, decision tree, random forest, logistic regression, Gaussian Naive Bayes, k- nearest neighbor, and support vector machines. We addressed the class-imbalance issue in the dataset's dependent variable by applying over and under-sampling techniques. Techniques used were SMOTE and edited nearest neighbors' rule for oversampling and under-sampling, respectively. Moreover, 10-fold cross-validation was used to validate the performance of the models. Grid searching and hyperparameter tuning were done for better performance of models. All the models were assessed based on mean accuracy values from 10-fold cross-validation, specificity, sensitivity, F-1 score, ROC curve percentages. Sensitivity is the measure of true positive rate providing the information on the percentage of the population that survived for five years after diagnosed with cancer. In contrast, specificity is the measure of the true negative rate41. All the machine learning tasks were executed in Python version 3.7 using Scikit learn, Pandas, NumPy packages. 

* **Data Source**: SEER (Surveillance, Epidemiology, and End Results) National Cancer registry data was used. SEER 18 regs with additional treatment fields data set were downloaded using SEER stat software version 8.3.6. The database was (1975-2016 varying) extracted into the comma-delimited format. 
* **Steps involved** 
  1. Data processing and dependent variable creation
      * [Preprocessing](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Data_processing/Preprocessing.py)
      * [Dummy Variables](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Data_processing/dummies.py)
  3. Data visualization using Tableau
  4. Data analysis using RStudio and SQL
      * [Simple Logistic Regression](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/4586576adbf11800d07c2504787d39c9a2a516d7/source_code/Risk_factor_analysis/Uni_Regression.R)
      * [Multiple Logistic Regression](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/4586576adbf11800d07c2504787d39c9a2a516d7/source_code/Risk_factor_analysis/Multi_Regression.R)
      * Descriptive Statistcs Summary
        * [Numerical](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/4586576adbf11800d07c2504787d39c9a2a516d7/source_code/Descriptive_statistics/descriptive_statistics_for_numerical_variables.sql)
        * [Categorical](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/4586576adbf11800d07c2504787d39c9a2a516d7/source_code/Descriptive_statistics/descriptive_statistics_for_categorical_variables.sql)
  5. Predictive modelling and comparision of the model performance uisng different algorithms
      * **Decision Tree Classifier**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/4586576adbf11800d07c2504787d39c9a2a516d7/source_code/Machine_learning/DT.py)
        * [Over sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/DT_oversampling.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/DT_undersampling.py)
      * **Gaussian Naive Bayes Classifier**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/GNB.py)
        * [Over sampling](https://github.com/Research-Informatics-Lab/Oral-Cancer/blob/main/SEER_Oral_Cancer/Machine_learning/GNB_oversampling.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/GNB_undersampling.py)
      * **K-Nearest Neighbors**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/KNN.py)
        * [Over sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/KNN_oversampling.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/KNN_undersampling.py)
      * **Logistic Regression Classifier**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/LR.py)
        * [Over sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/LR_over.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/LR_under.py)
      * **Random Forest Classifier**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/RFC.py)
        * [Over sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/RFC_oversampling.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/RFC_undersampling.py)
      * **Support Vector Machine Classifier**
        * [No sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/SVM.py)
        * [Over sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/SVM_oversampling.py)
        * [Under sampling](https://github.com/Yaswitha-MU/SEER_oral_cancer_data_analysis/blob/master/source_code/Machine_learning/SVM_undersampling.py)

### Project Files 
1. **Folder- Data_processing**
    * datapreprocessing.py file- this file consists of script necessary for the data processing as per the requiremnets. Run this file priorly for data cleaning and creation of dependant variable (five year survival status). 
2. **Folder- Risk_factor_analysis**
    * Uni_Regression.R- this file consists of script necessary for doing simple logistic statistical regression anlaysis and was written R programming language.By doing this analysis the co-relation among variables and be identified.
    * Multi_Regression.R- this file consists of script necessary for doing multiple logistic statistical regression anlaysis and was written R programming language.By doing this analysis the co-relation among variables and be identified.

3. **Folder- Machine_Learning**
    * DT.py- this script was written in python language for building the decision tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * GNB.py- this script was written in python language for building the Gaussian Navie Bayes five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * KNN.py- this script was written in python language for building the K- nearest neighbour five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * RFC.py- this script was written in python language for building the Random Forest Classifier tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * SVM.py- this script was written in python language for building the Support Vector Machine five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * LR.py- this script was written in python language for building the Logistic Regression five-year survivability predictive model using appropriate hyperparameter tuning and grid search. No sampling method was used. 
    * DT_undersampling.py- this script was written in python language for building the decision tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data. 
    * GNB_undersampling.py- this script was written in python language for building the Gaussian Navie Bayes five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data. 
    * KNN_undersampling.py- this script was written in python language for building the K- nearest neighbour five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data.  
    * RFC_undersampling.py- this script was written in python language for building the Random Forest Classifier tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data. 
    * SVM_undersampling.py- this script was written in python language for building the Support Vector Machine five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data. 
    * LR_undersampling.py- this script was written in python language for building the Logistic Regression five-year survivability predictive model using appropriate hyperparameter tuning and grid search. An undersampling sampling method was used for the purpose of even distribution of the data. 
    * DT_oversampling.py- this script was written in python language for building the decision tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data. 
    * GNB_oversampling.py- this script was written in python language for building the Gaussian Navie Bayes five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data. 
    * KNN_oversampling.py- this script was written in python language for building the K- nearest neighbour five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data.  
    * RFC_oversampling.py- this script was written in python language for building the Random Forest Classifier tree five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data.  
    * SVM_oversampling.py- this script was written in python language for building the Support Vector Machine five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data.  
    * LR_oversampling.py- this script was written in python language for building the Logistic Regression five-year survivability predictive model using appropriate hyperparameter tuning and grid search. A oversampling sampling method was used for the purpose of even distribution of the data. 

 
