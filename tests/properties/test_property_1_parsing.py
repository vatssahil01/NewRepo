from hypothesis import given, strategies as st
from app.core.parser import extract_section

# Feature: clinical-research-assistant, Property 1
@given(st.text())
def test_document_processing_completeness(text):
    result = extract_section(text, "abstract")
    assert result is None or isinstance(result, str)
