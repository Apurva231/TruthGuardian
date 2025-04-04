from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from google.cloud import vision
import io
import os

app = FastAPI()

# Set credentials for Google Cloud Vision
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

client = vision.ImageAnnotatorClient()

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save uploaded file
    contents = await file.read()
    with open(f"uploaded_{file.filename}", "wb") as f:
        f.write(contents)

    # Read file as bytes for Vision API
    image = vision.Image(content=contents)

    # Use Vision API to get labels
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Extract label descriptions
    descriptions = [label.description.lower() for label in labels]

    # Define suspicious/fake-related keywords
    suspicious_keywords = ["manipulated", "photoshopped", "edited", "fake", "hoax", "forged", "meme", "spoof"]

    # Check if any label matches suspicious keywords
    is_fake = any(keyword in desc for desc in descriptions for keyword in suspicious_keywords)

    # Add reason
    reason = "Suspicious content detected" if is_fake else "No suspicious content detected"

    return JSONResponse(content={
        "filename": file.filename,
        "labels": descriptions,
        "is_fake": is_fake,
        "reason": reason
    })
