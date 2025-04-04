from fastapi import APIRouter, UploadFile, File
from services.image import analyze_image
from services.save_result import save_to_db

router = APIRouter()

@router.post("/analyze_image")
async def analyze_image_route(file: UploadFile = File(...)):
    result = await analyze_image(file)
    return result
    save_to_db(result)  
