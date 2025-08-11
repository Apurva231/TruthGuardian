from models.schema import AnalysisResult
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import preprocess_kgptalkie as ps  # You used this for text cleaning

# Load model and tokenizer
model = load_model("text_detector_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAXLEN = 1000  # same as during training

def analyze_text(text: str) -> AnalysisResult:
    # 1. Preprocess input
    clean_text = ps.remove_special_chars(text.lower())
    
    # 2. Tokenize and pad
    seq = tokenizer.texts_to_sequences([clean_text])
    padded_seq = pad_sequences(seq, maxlen=MAXLEN)
    
    # 3. Predict
    prob = model.predict(padded_seq)[0][0]  # sigmoid output between 0 and 1
    confidence = f"{prob * 100:.2f}%" if prob > 0.5 else f"{(1 - prob) * 100:.2f}%"

    # 4. Interpret and suggest
    if prob >= 0.7:
        verdict = "REAL"
        suggestions = [
            "You may share this info, but still consider checking for updates.",
            "Stay informed with trusted news sources."
        ]
    elif prob <= 0.3:
        verdict = "FAKE"
        suggestions = [
            "Avoid sharing this info until verified.",
            "Check with official news portals.",
            "Look up the claim on fact-checking websites."
        ]
    else:
        verdict = "INCONCLUSIVE"
        suggestions = [
            "No supporting fact-checks or related news found.",
            "Try rephrasing or verifying manually."
        ]
        confidence = "N/A"

    return AnalysisResult(
        verdict=verdict,
        confidence=confidence,
        suggestions=suggestions
    )
