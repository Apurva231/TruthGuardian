from pydantic import BaseModel
from typing import Any

class TextInput(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    verdict: str
    confidence: float
    raw: Any  # to include raw model output or error details
