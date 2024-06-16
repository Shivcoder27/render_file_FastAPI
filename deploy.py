import numpy as np
import pickle
import streamlit as st

# Load the pre-trained model
loaded_model = pickle.load(open('D:/PYTHON/PYTHON PROJECTS/Projects/Heart_disease_project/trained_model.sav', 'rb'))

# Function for prediction
def heart_disease_prediction(input_data):
    # Convert the input data to numpy array
    input_data_to_numpy = np.asarray(input_data, dtype=np.float32)  # Ensure all data is float
    # Reshape the numpy array as we are predicting for only one instance
    input_reshape = input_data_to_numpy.reshape(1, -1)
    # Make prediction
    prediction = loaded_model.predict(input_reshape)
    # Return result
    if prediction[0] == 0:
        return 'The person is fit', 'green'
    else:
        return 'The person is not fit', 'red'

def main():
    st.title("Heart Disease Prediction")
    st.subheader("Predict whether a person is fit or not")

    # Getting the input from user
    Age = st.number_input('Age', min_value=0, max_value=120, value=50)
    sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    Chest_Pain = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])
    Resting_BP = st.number_input('Resting Blood Pressure', min_value=0, value=120)
    Cholestrol = st.number_input('Cholesterol', min_value=0, value=200)
    Fasting_BP = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])
    Electrocardiographic_result = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
    Max_heart_rate = st.number_input('Maximum Heart Rate Achieved', min_value=0, value=150)
    Exercise_angina = st.selectbox('Exercise Induced Angina', options=[0, 1])
    Old_peak = st.number_input('Old Peak', min_value=0.0, value=1.0, step=0.1)
    Slop_of_peak_ex = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2])
    Major_vessels_color = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3])
    Thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3])

    # Code for prediction
    diagnosis = ''
    diagnosis_color = 'black'

    if st.button('Test Heart Disease'):
        input_data = [Age, sex, Chest_Pain, Resting_BP, Cholestrol, Fasting_BP, Electrocardiographic_result, Max_heart_rate, Exercise_angina, Old_peak, Slop_of_peak_ex, Major_vessels_color, Thal]
        diagnosis, diagnosis_color = heart_disease_prediction(input_data)

    # Display the diagnosis result
    st.markdown(f'<h2 style="color:{diagnosis_color};">{diagnosis}</h2>', unsafe_allow_html=True)

# Driver Code
if __name__ == '__main__':
    main()
