# predict_chunks_audio.py

import numpy as np
from tensorflow.keras.models import load_model
import librosa
import os

def extract_mfcc(file_path, max_pad_len=174):
    y, sr = librosa.load(file_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    if mfcc.shape[1] < max_pad_len:
        pad_width = max_pad_len - mfcc.shape[1]
        mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :max_pad_len]
    return mfcc.reshape(1, 40, 174, 1)

def predict_audio(model, file_path):
    mfcc = extract_mfcc(file_path)
    prediction = model.predict(mfcc)
    label = "FAKE" if np.argmax(prediction) == 1 else "REAL"
    confidence = round(np.max(prediction) * 100, 2)
    return label, confidence

# Load model
model = load_model("fake_audio_detector.h5")

# Predict on all chunks
chunk_folder = "chunks"
chunk_files = sorted(os.listdir(chunk_folder))

print("🧠 Predictions on audio chunks:")
for i, chunk_file in enumerate(chunk_files):
    path = os.path.join(chunk_folder, chunk_file)
    label, confidence = predict_audio(model, path)
    print(f"[{i*2}-{(i+1)*2}s] → {label} ({confidence}%)")