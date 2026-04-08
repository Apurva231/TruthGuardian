# 🛡️ Truth Guardian — Fake News & Rumour Detector

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

A **multi-modal fake news detection system** that identifies and flags misinformation from **text, audio, and images** in real time — powered by NLP, deep learning, and deepfake detection.

[Features](#-features) • [Tech Stack](#-tech-stack) • [Project Structure](#-project-structure) • [Getting Started](#-getting-started) • [API Reference](#-api-reference)

</div>

---

## ✨ Features

| Module | Description |
|---|---|
| 📝 **Text Analysis** | NLP-based fake news classification using a trained deep learning model |
| 🎵 **Audio Detection** | CNN-based model to detect AI-generated or manipulated audio (deepfake audio) |
| 🖼️ **Image Detection** | Facial landmark analysis to detect deepfake images and videos |
| 🤖 **Chatbot** | Conversational interface for guided fact-checking |
| 📊 **Real-time Results** | Instant prediction scores with confidence levels |
| 🌐 **REST API** | Clean Flask API consumed by a React frontend |

---

## 🧰 Tech Stack

**Backend**
- Python, Flask
- TensorFlow / Keras (`.h5` models)
- scikit-learn, NLTK (NLP pipeline)
- OpenCV, dlib (facial landmark detection)
- Librosa (audio feature extraction)
- MongoDB (via PyMongo)

**Frontend**
- React 18
- Axios (API calls)
- CSS Modules

**ML Models**
- `text_detector_model.h5` — Fake text classifier
- `fake_audio_detector.h5` — CNN audio deepfake detector
- `tokenizer.pkl` — Text tokenizer for NLP preprocessing

---

## 📁 Project Structure

```
FAKE_RUMOR_DETECTION/
│
├── audio_detect/               # Audio deepfake detection module
│   ├── for-2seconds/testing/   # Test audio samples (fake / real)
│   ├── audio.py                # Audio feature extraction
│   ├── chunks.py               # Audio chunking logic
│   ├── cnn_model.py            # CNN model definition
│   └── prediction.py          # Audio prediction pipeline
│
├── database/
│   └── mongo.py               # MongoDB connection & helpers
│
├── deepfake_detector/
│   └── detect_face_landmarks.py  # Facial landmark deepfake detection
│
├── models/
│   ├── audio_model.py         # Audio model loader
│   └── schema.py              # DB schema definitions
│
├── routes/
│   ├── audio_analysis.py      # /api/audio endpoint
│   ├── image_analysis.py      # /api/image endpoint
│   └── text_analysis.py       # /api/text endpoint
│
├── services/
│   └── nlp.py                 # NLP preprocessing service
│
├── truth-guardian/             # React frontend
│   └── src/
│       ├── components/        # Reusable UI components
│       ├── pages/             # Route-level page components
│       └── App.js             # Root component
│
├── chatbot.py                 # Chatbot logic
├── image_detection.py         # Image analysis entry point
├── main.py                    # Flask app entry point
├── train_text_model.py        # Script to train the text model
├── fact_check_model.py        # Fact-checking model
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not committed)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- MongoDB Atlas account (or local MongoDB)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fake-rumor-detection.git
cd fake-rumor-detection
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key
```

Start the Flask server:

```bash
python main.py
```

The API will be running at `http://localhost:5000`

### 3. Frontend Setup

```bash
cd truth-guardian
npm install
npm start
```

The React app will be running at `http://localhost:3000`

---

## 🔌 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/text` | Analyze text for fake news |
| `POST` | `/api/audio` | Analyze audio for deepfake |
| `POST` | `/api/image` | Analyze image for deepfake |

### Example — Text Analysis

```bash
curl -X POST http://localhost:5000/api/text \
  -H "Content-Type: application/json" \
  -d '{"text": "Breaking: Scientists discover water on Mars!"}'
```

**Response:**
```json
{
  "prediction": "FAKE",
  "confidence": 0.87,
  "message": "This content is likely fabricated."
}
```

---

## 🤖 Training the Models

To retrain the text classification model:

```bash
python train_text_model.py
```

> ⚠️ Pre-trained model files (`*.h5`, `*.pkl`) are **not included** in the repository due to file size. Contact the maintainer or retrain using the provided scripts.

---

## 🧪 Running Tests

```bash
# Test text model
python test_text_model.py

# Test audio detection
cd audio_detect
python prediction.py
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👥 Authors

> Built with ❤️ as part of a multi-modal misinformation detection research project.

---

<div align="center">
  <sub>If this project helped you, please consider giving it a ⭐</sub>
</div>