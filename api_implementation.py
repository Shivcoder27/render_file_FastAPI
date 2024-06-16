# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:46:08 2024

@author: shivashish kaushik
"""

import json 
import requests

url = ' http://127.0.0.1:8000/heart_prediction'

input_data_for_model= {
   "age": 56,
   "sex": 0,
   "cp": 1,
   "trestbps": 140,
   "chol": 249,
   "fbs": 0,
   "restecg": 0,
   "thalach": 153,
   "exang": 0,
   "oldpeak": 1.3,
   "slope": 1,
   "ca": 0,
   "thal": 2
    }

input_json = json.dumps(input_data_for_model)
response = requests.post(url,data= input_json)
print(response.text)