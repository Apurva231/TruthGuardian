# split_audio_chunks.py

import librosa
import numpy as np
import os
import soundfile as sf

def split_audio(audio_path, chunk_duration=2):
    y, sr = librosa.load(audio_path, sr=16000)
    chunk_samples = chunk_duration * sr
    total_chunks = len(y) // chunk_samples

    os.makedirs("chunks", exist_ok=True)
    chunk_paths = []

    for i in range(total_chunks):
        chunk = y[i * chunk_samples: (i + 1) * chunk_samples]
        out_path = f"chunks/chunk_{i}.wav"
        sf.write(out_path, chunk, sr)
        chunk_paths.append(out_path)

    return chunk_paths

if __name__ == "_main_":
    paths = split_audio("your_audio.wav")
    print(f"✅ Split into {len(paths)} chunks")