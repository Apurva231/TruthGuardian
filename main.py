from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import image_analysis, text_analysis, audio_analysis

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] to allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text_analysis.router)
app.include_router(image_analysis.router)
app.include_router(audio_analysis.router)

@app.get("/")
def root():
    return {"message": "Fake News API is running"}

from fastapi.middleware.cors import CORSMiddleware

