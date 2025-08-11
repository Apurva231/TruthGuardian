from tensorflow.keras.models import load_model
import pickle

def predict_claim_model(text):
    # load model
    # tokenizer -> encode -> predict
    model = load_model("text_detector_model.h5")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    # Return "FAKE" or "REAL"
    return "REAL"  # Placeholder
