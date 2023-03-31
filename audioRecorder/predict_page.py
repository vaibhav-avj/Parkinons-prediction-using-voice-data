import streamlit as st 
import pickle
import numpy as np
from audioExtract import extract_values


def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    
    return data

data = load_model()

regressor_model = data['model']
scaler = data['scaler']

def  show_predict_page():
    st.title("Parkinson's Disease Prediction")
    
    st.container()
    st.write("""### This is the placeholder for parsing the Audio file that was recorded in the Record Interface.\nHere Parsel Mouth module will be used to get the values based on the UPDRS""")
    
    audio_file = st.file_uploader("Choose an patient's audio file", type = [".wav"], accept_multiple_files=False)
    values = []
    if audio_file is not None:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
        st.write(audio_file.name)

        updrs_values = extract_values(audio_file.name)
        # st.write(updrs_values)
        values = ([ "{:0.5f}".format(x) for x in updrs_values ])
        values = np.array(values)
        values = values.astype(np.float)

        # st.write("Jitter : " + str(values[0]) + "\n" + "Shimmer : " + str(values[1]) + "\n" +"NHR : " + str(values[2]) + "\n" + "HNR : " + str(values[3]) + "\n" + "PPE : " + str(values[4]))
        st.write("""### Please fill out the below fields to predict PD""")
        jitter = st.number_input('Enter Jitter(%)', step=0.000001, format="%.5f", value=values[0])
        shimmer = st.number_input('Enter Shimmer', step=0.000001, format="%.5f", value=values[1])
        nhr = st.number_input('Enter NHR(Normalized Harmonic Ratio)', step=0.000001, format="%.5f", value=values[2])
        hnr = st.number_input('Enter HNR (Harmonic-to-Noise)', step=0.000001, format="%.5f", value=values[3])
        # rpde = st.number_input('Enter RPDE', step=0.000001, format="%.5f")
        #   dfa = st.number_input('Enter DFA', step=0.000001, format="%.5f")
        ppe = st.number_input('Enter PPE', step=0.000001, format="%.5f", value=values[4])

        ok = st.button("Predict")

        if ok:
            if( jitter > 0 and shimmer > 0 and nhr > 0 and hnr > 0  and ppe > 0):
                X = np.array([[jitter, shimmer, nhr, hnr, ppe]])
                prediction = regressor_model.predict(X)

                st.write("The prediction based on the Model and User Data is : ", "{:.3f}".format(prediction[0]))
            else: 
                st.write('Please enter appropriate values')

    else:
        st.write("Please enter .wav audio file to proceed")



    

    
