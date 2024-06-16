# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:55:48 2024

@author: shivashish kaushik
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()


class model_input(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    
    
# Loading the saved model
heart_model = pickle.load(open('trained_model.sav','rb'))  


@app.post('/heart_prediction') 
def heart_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dict = json.loads(input_data)
    
    
    Age = input_dict['age']
    Sex = input_dict['sex']
    Cp = input_dict['cp']
    Trestbps = input_dict['trestbps']
    Chol = input_dict['chol']
    Fbs = input_dict['fbs']
    Restecg = input_dict['restecg']
    Thalach = input_dict['thalach']
    Exang = input_dict['exang']
    Oldpeak = input_dict['oldpeak']
    Slope = input_dict['slope']
    Ca = input_dict['ca']
    Thal = input_dict['thal']
    
    
    input_list = [Age,Sex,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]
    
    prediction = heart_model.predict([input_list])
    
    if prediction[0] == 0 :
        return 'The person is Fit'
    else:
        return 'The person is not Fit'
    
    
    
    
    