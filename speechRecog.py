import speech_recognition as sr
import re

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
with sr.AudioFile('Recordings\\streamlit_audio_12_17_20228_39_54 PM.wav') as source:
    audio_text = r.listen(source)
    print("Audio file is ready!")

# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using google speech recognition
    text = r.recognize_google(audio_text, language ='en-US')
    print("Text: "+ text)

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("Could not understand audio")

# Extract UPDRS values using regular expressions
updrs_values = re.findall(r'\d+', text)
print("UPDRS values: ", updrs_values)