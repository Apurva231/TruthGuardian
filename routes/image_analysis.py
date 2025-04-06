from fastapi import APIRouter, UploadFile, File
from image_detection import analyze_face_image
from database.mongo import fs, image_results_collection

router = APIRouter()

@router.post("/api/image-detect")
async def analyze_image_route(file: UploadFile = File(...)):
    file_bytes = await file.read()

    # Analyze image
    result = analyze_face_image(file_bytes)

    # Store image in GridFS
    image_id = fs.put(file_bytes, filename=file.filename, content_type=file.content_type)

    # Store result in MongoDB
    record = {
        "image_id": image_id,
        "filename": file.filename,
        "content_type": file.content_type,
        "label": result["label"],
        "confidence": result["confidence"]
    }
    image_results_collection.insert_one(record)

    return result
