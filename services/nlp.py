# services/nlp.py
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from preprocess_kgptalkie import remove_special_chars
from models.schema import AnalysisResult

# Load model and tokenizer once
model = load_model("text_detector_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

maxlen = 1000

def analyze_text(text: str) -> AnalysisResult:
    cleaned = remove_special_chars(text.lower())
    seq = tokenizer.texts_to_sequences([cleaned.split()])
    padded = pad_sequences(seq, maxlen=maxlen)

    prediction = model.predict(padded)[0][0]
    verdict = "FAKE" if prediction < 0.5 else "REAL"
    confidence = f"{(prediction if verdict == 'REAL' else 1 - prediction) * 100:.2f}%"

    suggestions = [
        "Check if this info appears on verified news portals.",
        "Search for official press releases.",
        "Look for fact-check articles."
    ]

    return AnalysisResult(label=verdict, score=confidence, suggestions=suggestions)
