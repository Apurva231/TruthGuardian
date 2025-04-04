from fastapi import APIRouter, Request
from models.schema import TextInput, AnalysisResult
from services.nlp import analyze_text
from services.save_result import save_to_db

router = APIRouter()

@router.post("/analyze_text", response_model=AnalysisResult)
async def analyze_text_route(input_data: TextInput):
    result = analyze_text(input_data.text)
    return result
    save_to_db(result)
