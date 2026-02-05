from app.models.enums import AudienceType

def generate_summary(findings, audience: AudienceType):
    texts = [f.text for f in findings]

    if not texts:
        return "No statistically significant findings were identified in this study."

    if audience == AudienceType.clinician:
        return (
            "Clinical Summary:\n"
            f"The study reports clinically meaningful outcomes. "
            f"Key results indicate that {texts[0].lower()}. "
            "These findings suggest potential improvements in patient care and treatment outcomes."
        )

    if audience == AudienceType.researcher:
        return (
            "Research Summary:\n"
            "This study presents statistically evaluated outcomes derived from a controlled methodology. "
            f"Primary findings show that {texts[0].lower()}. "
            "Further investigation is recommended to validate long-term effectiveness and generalizability."
        )

    # ADMINISTRATOR (IMPORTANT FIX)
    return (
        "Administrative Summary:\n"
        "This study evaluates a digital health intervention using a controlled study design. "
        f"The primary outcome demonstrates that {texts[0].lower()}. "
        "From an operational perspective, these results indicate potential for scalable implementation, "
        "reduced in-person resource utilization, and improved efficiency in care delivery."
    )
