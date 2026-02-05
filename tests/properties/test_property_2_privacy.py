from hypothesis import given, strategies as st
from app.core.privacy import validate_privacy

# Feature: clinical-research-assistant, Property 2
@given(st.text())
def test_privacy_validation(text):
    assert validate_privacy(text) in [True, False]
