from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    verdict: str
    confidence: int
    reasons: List[str]
    source_links: List[str]
