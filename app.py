import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('model.sav', 'rb'))

# logic 
def make_prediction(input_data):
    input_data = np.array(input_data).reshape(1,-1)
    print(input_data)
    prediction = model.predict(input_data)
    print(prediction)
    return prediction[0]

def main():
    ''' UI CODE : Streamlit code'''
    st.title("Heart Attack Prediction")

    # form inputs 
    with st.form(key='input_form'):
        age = st.number_input('Age',min_value=5,max_value=80)
        sex = st.selectbox('Sex (1=Male , 0=Female)',[1,0])
        cp = st.selectbox('Chest Pain type (1,2,3,4)',[1,2,3,4])
        trtbps = st.number_input(' resting blood pressure (in mm Hg)')
        chol=st.number_input('cholestoral in mg/dl fetched via BMI sensor')
        fbs = st.selectbox('(fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)',[1,0])
        rest_ecg = st.selectbox('resting electrocardiographic results',[0,1,2])
        thalach = st.number_input('maximum heart rate achieved')
        exang = st.selectbox('exercise induced angina (1 = yes; 0 = no)',[1,0])
        oldpeak = st.number_input('Previous peak')
        slp = st.selectbox('Slope (0,1,2)',[0,1,2])
        caa = st.selectbox('Number of major vessels (0,1,2,3)',[0,1,2,3])
        thall = st.selectbox('Thal rate (0,1,2)',[0,1,2])

        # predict button 
        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            input_data = [age,sex,cp,trtbps,chol,fbs,rest_ecg,thalach,exang,oldpeak,slp,caa,thall]
            prediction = make_prediction(input_data)
            if prediction == 1:
                st.error('You have heart disease')
            else:
                st.success('You do not have heart disease')




if __name__ == "__main__":
    main()