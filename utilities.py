import pandas as pd
import numpy as np
import config
import pickle
import json


class Life_expectancy():
    def __init__(self,Country,Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling):
        self.Country=Country
        self.Year=Year
        self.Status=Status
        self.Adult_Mortality=Adult_Mortality
        self.infant_deaths=infant_deaths
        self.Alcohol=Alcohol
        self.percentage_expenditure=percentage_expenditure
        self.Hepatitis_B=Hepatitis_B
        self.Measles=Measles
        self.BMI=BMI
        self.under_five_deaths=under_five_deaths
        self.Polio=Polio
        self.Total_expenditure=Total_expenditure
        self.Diphtheria=Diphtheria
        self.HIV_AIDS=HIV_AIDS
        self.GDP=GDP
        self.Population=Population
        self.thinness_1_19_years=thinness_1_19_years
        self.thinness_5_9_years=thinness_5_9_years
        self.Income_composition_of_resources=Income_composition_of_resources
        self.Schooling=Schooling

    def load_model(self):
        with open(config.model_file_path,"rb") as f1:
            self.model=pickle.load(f1)
        with open(config.project_file_data,"r") as f2:
            self.project_data=json.load(f2)

    def predict_life_expectancy(self):
        self.load_model()
        series=pd.Series(np.zeros(len(self.project_data['columns'])),index=self.project_data['columns'])

        series['Country']=self.project_data['Country'][self.Country]
        series['Year']=self.Year
        series['Status']=self.project_data['Status'][self.Status]
        series['Adult_Mortality']=self.Adult_Mortality
        series['infant_deaths']=self.infant_deaths
        series['Alcohol']=self.Alcohol
        series['percentage_expenditure']=self.percentage_expenditure
        series['Hepatitis_B']=self.Hepatitis_B
        series['Measles']=self.Measles
        series['BMI']=self.BMI
        series['under_five_deaths']=self.under_five_deaths
        series['Polio']=self.Polio
        series['Total_expenditure']=self.Total_expenditure
        series['Diphtheria']=self.Diphtheria
        series['HIV_AIDS']=self.HIV_AIDS
        series['GDP']=self.GDP
        series['Population']=self.Population
        series['thinness_1_19_years']=self.thinness_1_19_years
        series['thinness_5_9_years']=self.thinness_5_9_years
        series['Income_composition_of_resources']=self.Income_composition_of_resources
        series['Schooling']=self.Schooling

        pred_output=self.model.predict([series])[0]
        pred_output=np.around(pred_output,2)

        return pred_output
        












# Country=0
# Year=2015
# Status=1
# Adult_Mortality=263
# infant_deaths=62
# Alcohol=0.01
# percentage_expenditure=71.2796
# Hepatitis_B=65
# Measles=1154
# BMI=19.1
# under_five_deaths=83
# Polio=6
# Total_expenditure=8.16
# Diphtheria=65
# HIV_AIDS=0.1
# GDP=584.2592
# Population=33736494
# thinness_1_19_years=17.2
# thinness_5_9_years=17.3
# Income_composition_of_resources=0.479
# Schooling=10.1

# pred_input=np.array([Country,Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,Hepatitis_B,
#                      Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,GDP,Population,
#                      thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling])

# pred_output=dt2_model.predict([pred_input])[0]