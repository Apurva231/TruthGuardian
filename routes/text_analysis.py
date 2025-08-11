from fastapi import APIRouter
from models.schema import TextInput, AnalysisResult
from services.nlp import analyze_text
from database.mongo import text_results_collection

router = APIRouter()

@router.post("/analyze_text", response_model=AnalysisResult)
async def analyze_text_route(input_data: TextInput):
    result = analyze_text(input_data.text)
    
    # Store result in MongoDB
    record = {
        "text": input_data.text,
        "verdict": result.verdict,
        "confidence": result.confidence
    }
    text_results_collection.insert_one(record)

    return result







