from fastapi import FastAPI
from routes import image_analysis, text_analysis

app = FastAPI()

app.include_router(text_analysis.router)
app.include_router(image_analysis.router)

@app.get("/")
def root():
    return {"message": "Fake News API is running"}
