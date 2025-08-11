from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    verdict: str
    confidence: str  # confidence is a formatted string like "89.54%"
    suggestions: List[str]
