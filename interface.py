from flask import Flask,render_template,request,jsonify
from utilities import Life_expectancy
import config
import pickle

app=Flask(__name__)
@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction",methods=["post"])
def get_life_expectancy():
    data=request.form
    Country=data['Country']
    Year=float(data['Year'])
    Status=data['Status']
    Adult_Mortality=float(data['Adult_Mortality'])
    infant_deaths=float(data['infant_deaths'])
    Alcohol=float(data['Alcohol'])
    percentage_expenditure=float(data['percentage_expenditure'])
    Hepatitis_B=float(data['Hepatitis_B'])
    Measles=float(data['Measles'])
    BMI=float(data['BMI'])
    under_five_deaths=float(data['under_five_deaths'])
    Polio=float(data['Polio'])
    Total_expenditure=float(data['Total_expenditure'])
    Diphtheria=float(data['Diphtheria'])
    HIV_AIDS=float(data['HIV_AIDS'])
    GDP=float(data['GDP'])
    Population=float(data['Population'])
    thinness_1_19_years=float(data['thinness_1_19_years'])
    thinness_5_9_years=float(data['thinness_5_9_years'])
    Income_composition_of_resources=float(data['Income_composition_of_resources'])
    Schooling=float(data['Schooling'])

    instance=Life_expectancy(Country,Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,GDP,Population,thinness_1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling)
    life=instance.predict_life_expectancy()
    life1=f"Life Expectancy of {instance.Country} is {life}"

    return render_template("index.html" , Result=life1)

if __name__=="__main__":
    app.run(debug=True , port=config.PORT , host=config.HOST)


