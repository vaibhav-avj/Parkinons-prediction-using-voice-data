# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version April 2022

import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components


def showRecordPage():
    # st.set_page_config(page_title="Record Patient Audio")
    st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''', unsafe_allow_html=True)
    st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''', unsafe_allow_html=True)  # darkmode
    st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''', unsafe_allow_html=True)  # lightmode
    record_audio()


def record_audio():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)


    st.title('Record patient\'s audio here')
    st.subheader('Follow the below steps:')
    st.write('''
    1. Click on Start recording\n
    2. Make sure the surrounding is noise free\n
    3. Let the patient Pronounce Vowels\n
    \t\tA E I O U\n
    4. Click on Stop Recording\n
    5. Download the file and store in the 'Recordings' Folder\n
    \n
    Make sure to name the file accordingly
    ''')


    # STREAMLIT AUDIO RECORDER Instance
    val = st_audiorec()

    # web component returns arraybuffer from WAV-blob
    st.write('Audio data received in the Python backend will appear below this message ...')

    if isinstance(val, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            val = np.array(val)             # convert to np array
            sorted_ints = val[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            wav_bytes = stream.read()

        # wav_bytes contains audio data in format to be further processed
        # display audio data as received on the Python side
        st.audio(wav_bytes, format='audio/wav')
        st.write('This audio data will further parsed in order get the values of UPDRS scale.')



# if __name__ == '__main__':
#     showRecordPage()
