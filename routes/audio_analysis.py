# backend/routes/audio_analysis.py

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from models.audio_model import predict_audio
from database.mongo import audio_results_collection

router = APIRouter(prefix="/api")


@router.post("/audio-detect")
async def audio_detect(audio: UploadFile = File(...)):
    try:
        temp_path = f"temp_{audio.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)

        label, score = predict_audio(temp_path)

        # Store result in MongoDB
        result = {
            "filename": audio.filename,
            "label": label,
            "score": score,
        }
        audio_results_collection.insert_one(result)

        os.remove(temp_path)
        return JSONResponse(content={
            "label": label,
            "score": score,
            "notes": ["Model trained on 2-second audio clips", "MFCC-based classification"]
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
