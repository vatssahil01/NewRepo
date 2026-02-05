from pydantic import BaseModel
from typing import Optional

class StatisticalResult(BaseModel):
    type: str
    value: str
    significant: bool

class KeyFinding(BaseModel):
    text: str
    confidence: float
