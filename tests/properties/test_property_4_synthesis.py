from hypothesis import given, strategies as st
from app.core.summarizer import generate_summary
from app.models.enums import AudienceType

# Feature: clinical-research-assistant, Property 4
@given(st.lists(st.text()))
def test_synthesis_generation(findings):
    class Dummy:
        def __init__(self, t):
            self.text = t

    dummy_findings = [Dummy(f) for f in findings]
    summary = generate_summary(dummy_findings, AudienceType.clinician)
    assert isinstance(summary, str)
