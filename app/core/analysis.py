# app/core/analysis.py
def compute_confidence(findings, p_values):
    score = 0.4
    if p_values:
        score += 0.3
    if len(findings) > 2:
        score += 0.3
    return round(min(score, 1.0), 2)
