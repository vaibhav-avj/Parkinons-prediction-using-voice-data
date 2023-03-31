import librosa 
import glob
import numpy as np
import parselmouth
from parselmouth.praat import call

 # load the wav file 

def extract_values(filename):
    for wave_file in glob.glob("../Recordings/" + filename): 
        y, sr = librosa.load(wave_file)
        sound = parselmouth.Sound(wave_file) 

        # extract the acoustic features 
        mfcc = librosa.feature.mfcc(y=y, sr=sr) 
        zcr = librosa.feature.zero_crossing_rate(y) 
        rms = librosa.feature.rms(y=y) 
        spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr) 
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr) 
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr) 

        # extract jitter, shimmer, HNR, RPDE, DFA, PPE, and NHR 
        jitter = librosa.feature.delta(mfcc, order=1) 
        shimmer = librosa.feature.delta(zcr) 
        harmonicity = call(sound, "To Harmonicity (cc)", 0.01, 75, 0.1, 1.0)
        hnr = call(harmonicity, "Get mean", 0, 0)
        # rpde = librosa.feature.rpde(y=y, sr=sr) 
        # dfa = librosa.feature.dfa(y=y, sr=sr) 
        ppe = librosa.feature.poly_features(y=y, sr=sr) 
        nhr = librosa.feature.tonnetz(y=y, sr=sr)

        print("Jitter:", np.mean(jitter)) 
        print("Shimmer:", np.mean(shimmer)) 
        print("HNR:", np.mean(hnr)) 
        #print("RPDE:", rpde) 
        #print("DFA:", dfa) 
        print("PPE:", np.mean(ppe))
        print("NHR:", np.mean(nhr))
        print("\n")

        values = [np.mean(jitter), np.mean(shimmer), np.mean(hnr), np.mean(ppe), np.mean(nhr)]

        return values

# ans = extract_values('rec1.wav')

# print(ans)