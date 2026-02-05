# app/core/extractor.py
import re
from app.models.extraction import KeyFinding

def extract_p_values(text: str):
    return re.findall(r"p\s*[<=>]\s*0\.\d+", text)

def extract_key_findings(results: str):
    if not results:
        return []

    sentences = results.split(".")
    findings = []
    for s in sentences:
        if "significant" in s.lower():
            findings.append(KeyFinding(text=s.strip(), confidence=0.7))
    return findings
