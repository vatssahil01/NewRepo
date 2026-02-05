# app/core/parser.py
import pdfplumber
from app.models.document import DocumentSections

def extract_section(text: str, keyword: str):
    text = text.lower()
    if keyword not in text:
        return None
    start = text.find(keyword)
    return text[start:start + 1000]

def parse_pdf(file_path: str) -> DocumentSections:
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    return DocumentSections(
        abstract=extract_section(full_text, "abstract"),
        methodology=extract_section(full_text, "method"),
        results=extract_section(full_text, "result"),
        conclusions=extract_section(full_text, "conclusion"),
        raw_text=full_text
    )
