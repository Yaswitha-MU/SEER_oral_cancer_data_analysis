
#Date created- 10/12/2020
#Last Modified Date - 18/02/2021
#@author: Yaswitha Jampani
#Purpose: This script is to get the summary statistics of the variables 
#Source: SEER_final_dataset.csv


# Here the list of categorical variables and the script written for getting their summary of descriptive statistics
#Marital status
select "Survival_status", a."Marital status at diagnosis", count_marital_status_at_diagnosis,
count_marital_status_at_diagnosis*100 / b.group_count as percentage_marital_status_at_diagnosis
from (
    select "Survival_status", "Marital status at diagnosis", count("Marital status at diagnosis") as count_marital_status_at_diagnosis
    from seer
    group by "Survival_status", "Marital status at diagnosis" 
) as a
inner join
(
  select  "Marital status at diagnosis", count("Marital status at diagnosis") as group_count  
  from seer
  group by "Marital status at diagnosis"
) as b
on a."Marital status at diagnosis" = b."Marital status at diagnosis"
order by "Marital status at diagnosis"

#Race recoded
select "Survival_status", a."Race recode (White, Black, Other)", count_race_recode,
count_race_recode*100 / b.group_count as percentage_race_recode
from (
    select "Survival_status", "Race recode (White, Black, Other)", count("Race recode (White, Black, Other)") as count_race_recode
    from seer
    group by "Survival_status", "Race recode (White, Black, Other)" 
) as a
inner join
(
  select  "Race recode (White, Black, Other)", count("Race recode (White, Black, Other)") as group_count  
  from seer
  group by "Race recode (White, Black, Other)"
) as b
on a."Race recode (White, Black, Other)" = b."Race recode (White, Black, Other)"
order by "Race recode (White, Black, Other)"

#sex
select "Survival_status", a."Sex", count_sex,
count_sex*100 / b.group_count as percentage_sex
from (
    select "Survival_status", "Sex", count("Sex") as count_sex
    from seer
    group by "Survival_status", "Sex" 
) as a
inner join
(
  select  "Sex", count("Sex") as group_count  
  from seer
  group by "Sex"
) as b
on a."Sex" = b."Sex"
order by "Sex"

#Primary Site
select "Survival_status", a."Primary Site", count_primary_site,
count_primary_site*100 / b.group_count as percentage_primary_site
from (
    select "Survival_status", "Primary Site", count("Primary Site") as count_primary_site
    from seer
    group by "Survival_status", "Primary Site" 
) as a
inner join
(
  select  "Primary Site", count("Primary Site") as group_count  
  from seer
  group by "Primary Site"
) as b
on a."Primary Site" = b."Primary Site"
order by "Primary Site"

#Grade
select "Survival_status", a."Grade", count_grade,
count_grade*100 / b.group_count as percentage_grade
from (
    select "Survival_status", "Grade", count("Grade") as count_grade
    from seer
    group by "Survival_status", "Grade" 
) as a
inner join
(
  select  "Grade", count("Grade") as group_count  
  from seer
  group by "Grade"
) as b
on a."Grade" = b."Grade"
order by "Grade"

#Laterality
select "Survival_status", a."Laterality", count_laterality,
count_laterality*100 / b.group_count as percentage_laterality
from (
    select "Survival_status", "Laterality", count("Laterality") as count_laterality
    from seer
    group by "Survival_status", "Laterality" 
) as a
inner join
(
  select  "Laterality", count("Laterality") as group_count  
  from seer
  group by "Laterality"
) as b
on a."Laterality" = b."Laterality"
order by "Laterality"

#Diagnostic confirmation
select "Survival_status", a."Diagnostic Confirmation", count_diagnostic_confirmation,
count_diagnostic_confirmation*100 / b.group_count as percentage_diagnostic_confirmation
from (
    select "Survival_status", "Diagnostic Confirmation", count("Diagnostic Confirmation") as count_diagnostic_confirmation
    from seer
    group by "Survival_status", "Diagnostic Confirmation" 
) as a
inner join
(
  select  "Diagnostic Confirmation", count("Diagnostic Confirmation") as group_count  
  from seer
  group by "Diagnostic Confirmation"
) as b
on a."Diagnostic Confirmation" = b."Diagnostic Confirmation"
order by "Diagnostic Confirmation"

#Radiation sequence with surgery
select "Survival_status", a."Radiation sequence with surgery", count_radiation_sequence_surgery,
count_radiation_sequence_surgery*100 / b.group_count as percentage_radiation_sequence_surgery
from (
    select "Survival_status", "Radiation sequence with surgery", count("Radiation sequence with surgery") as count_radiation_sequence_surgery
    from seer
    group by "Survival_status", "Radiation sequence with surgery" 
) as a
inner join
(
  select  "Radiation sequence with surgery", count("Radiation sequence with surgery") as group_count  
  from seer
  group by "Radiation sequence with surgery"
) as b
on a."Radiation sequence with surgery" = b."Radiation sequence with surgery"
order by "Radiation sequence with surgery"

#Radiation recode
select "Survival_status", a."Radiation recode", count_radiation_recode,
count_radiation_recode*100 / b.group_count as percentage_radiation_recode
from (
    select "Survival_status", "Radiation recode", count("Radiation recode") as count_radiation_recode
    from seer
    group by "Survival_status", "Radiation recode" 
) as a
inner join
(
  select  "Radiation recode", count("Radiation recode") as group_count  
  from seer
  group by "Radiation recode"
) as b
on a."Radiation recode" = b."Radiation recode"
order by "Radiation recode"

#Reason for no cancer directed surgery
select "Survival_status", a."Reason no cancer-directed surgery", count_reason_no_surgery,
count_reason_no_surgery*100 / b.group_count as percentage_reason_no_surgery
from (
    select "Survival_status", "Reason no cancer-directed surgery", count("Reason no cancer-directed surgery") as count_reason_no_surgery
    from seer
    group by "Survival_status", "Reason no cancer-directed surgery" 
) as a
inner join
(
  select  "Reason no cancer-directed surgery", count("Reason no cancer-directed surgery") as group_count  
  from seer
  group by "Reason no cancer-directed surgery"
) as b
on a."Reason no cancer-directed surgery" = b."Reason no cancer-directed surgery"
order by "Reason no cancer-directed surgery"

#Chemotherapy recode
select "Survival_status", a."Chemotherapy recode (yes, no/unk)", count_chemotherapy_recode,
count_chemotherapy_recode*100 / b.group_count as percentage_chemotherapy_recode
from (
    select "Survival_status", "Chemotherapy recode (yes, no/unk)", count("Chemotherapy recode (yes, no/unk)") as count_chemotherapy_recode
    from seer
    group by "Survival_status", "Chemotherapy recode (yes, no/unk)" 
) as a
inner join
(
  select  "Chemotherapy recode (yes, no/unk)", count("Chemotherapy recode (yes, no/unk)") as group_count  
  from seer
  group by "Chemotherapy recode (yes, no/unk)"
) as b
on a."Chemotherapy recode (yes, no/unk)" = b."Chemotherapy recode (yes, no/unk)"
order by "Chemotherapy recode (yes, no/unk)"

#Histology
select "Survival_status", a."Histology", count_histology,
count_histology*100 / b.group_count as percentage_histology
from (
    select "Survival_status", "Histology", count("Histology") as count_histology
    from seer
    group by "Survival_status", "Histology" 
) as a
inner join
(
  select  "Histology", count("Histology") as group_count  
  from seer
  group by "Histology"
) as b
on a."Histology" = b."Histology"
order by "Histology"
