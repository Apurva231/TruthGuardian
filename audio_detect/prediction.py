import librosa
import numpy as np
from tensorflow.keras.models import load_model

def predict_audio(model, file_path):
    import librosa
    import numpy as np

    # Load the audio file
    audio, sample_rate = librosa.load(file_path, sr=16000)

    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfcc = np.pad(mfcc, ((0, 0), (0, max(0, 174 - mfcc.shape[1]))), mode='constant')
    mfcc = mfcc[:, :174]

    # Reshape for CNN
    mfcc = mfcc[np.newaxis, ..., np.newaxis]

    # Predict
    prediction = model.predict(mfcc)
    label = "FAKE" if np.argmax(prediction) == 1 else "REAL"
    confidence = round(np.max(prediction) * 100, 2)

    return label, confidence



# Load it first
model = load_model("fake_audio_detector.h5")

def extract_mfcc(file_path, max_pad_len=174):
    y, sr = librosa.load(file_path, sr=16000)  # consistent sampling
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

    # Pad or truncate
    if mfcc.shape[1] < max_pad_len:
        pad_width = max_pad_len - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :max_pad_len]

    return mfcc


mfcc = extract_mfcc("test_audio.wav")  # shape (40, 174)
mfcc = mfcc.reshape(1, 40, 174, 1)      # match training input shape


# Then use it
label, confidence = predict_audio(model, "test_audio.wav")
print(f"Prediction: {label}, Confidence: {confidence}%")
