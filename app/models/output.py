from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.models.enums import AudienceType

class GeneratedOutput(BaseModel):
    audience: AudienceType
    summary: str
    confidence_score: float
    citations: List[str]
    timestamp: datetime
