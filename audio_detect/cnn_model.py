import os
import numpy as np
np.complex = complex  # 🔧 Fix for librosa compatibility

import librosa
import librosa.display
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Directory containing 'real' and 'fake' folders
DATASET_PATH = "for-2seconds/training"
SAMPLES_TO_CONSIDER = 22050 * 2  # 2 seconds of audio

def extract_features(file_path, max_pad_len=216):
    try:
        audio, sr = librosa.load(file_path, sr=22050)
        if len(audio) < SAMPLES_TO_CONSIDER:
            audio = np.pad(audio, (0, SAMPLES_TO_CONSIDER - len(audio)))
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        pad_width = max_pad_len - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        return mfcc
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

X, y = [], []
for label, class_dir in enumerate(["real", "fake"]):
    folder = os.path.join(DATASET_PATH, class_dir)
    for file in os.listdir(folder):
        if file.endswith(".wav"):
            mfcc = extract_features(os.path.join(folder, file))
            if mfcc is not None:
                X.append(mfcc)
                y.append(label)

X = np.array(X)
X = X[..., np.newaxis]  # Add channel dimension for CNN
y = to_categorical(y, num_classes=2)

print("Dataset shape:", X.shape, y.shape)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# cnn model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=X_train.shape[1:]),
    MaxPooling2D((2,2)),
    Dropout(0.3),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Dropout(0.3),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


# Train the model
history = model.fit(X_train, y_train, epochs=15, batch_size=32,
                    validation_data=(X_test, y_test))

#Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# Save the model
model.save("fake_audio_detector.h5")
