from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Author(BaseModel):
    name: str
    affiliation: Optional[str] = None
    orcid: Optional[str] = None

class DocumentMetadata(BaseModel):
    title: str
    authors: List[Author]
    journal: str
    publication_date: date
    doi: Optional[str] = None

class DocumentSections(BaseModel):
    abstract: Optional[str]
    methodology: Optional[str]
    results: Optional[str]
    conclusions: Optional[str]
    raw_text: str
