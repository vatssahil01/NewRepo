# app/core/privacy.py
import re

PHI_PATTERNS = [
    r"\b\d{10}\b",       # phone numbers
    r"\b\d{12}\b",       # aadhaar-like
    r"patient name",
    r"date of birth"
]

def validate_privacy(text: str) -> bool:
    for pattern in PHI_PATTERNS:
        if re.search(pattern, text.lower()):
            return False
    return True

