# backend/models/audio_model.py

import numpy as np
import librosa
from tensorflow.keras.models import load_model

MODEL = load_model("fake_audio_detector.h5")

def extract_mfcc(file_path, max_pad_len=174):
    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc = np.pad(mfcc, ((0, 0), (0, max(0, max_pad_len - mfcc.shape[1]))), mode='constant')
    mfcc = mfcc[:, :max_pad_len]
    return mfcc.reshape(1, 40, 174, 1)

def predict_audio(file_path):
    mfcc = extract_mfcc(file_path)
    prediction = MODEL.predict(mfcc)
    label = "FAKE" if np.argmax(prediction) == 1 else "REAL"
    score = round(np.max(prediction) * 100, 2)
    return label, score
