from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

papers = [
    {
        "filename": "telemedicine_diabetes.pdf",
        "title": "Telemedicine Follow-Up in Type 2 Diabetes",
        "result": "Telemedicine follow-up showed statistically significant improvement in HbA1c levels (p < 0.01)."
    },
    {
        "filename": "hypertension_management.pdf",
        "title": "Remote Monitoring in Hypertension Management",
        "result": "Systolic blood pressure reduction was statistically significant in the intervention group (p < 0.05)."
    },
    {
        "filename": "cardiac_rehab.pdf",
        "title": "Digital Cardiac Rehabilitation Outcomes",
        "result": "No statistically significant difference was observed between digital and traditional rehabilitation (p = 0.12)."
    },
    {
        "filename": "mental_health_telecare.pdf",
        "title": "Telepsychiatry for Anxiety Disorders",
        "result": "Patients receiving telepsychiatry reported significantly reduced anxiety scores (p < 0.01)."
    }
]

for paper in papers:
    c = canvas.Canvas(paper["filename"], pagesize=A4)
    text = c.beginText(40, 800)

    text.textLine(paper["title"])
    text.textLine("")
    text.textLine("Abstract")
    text.textLine("This is a synthetic, publicly usable clinical research paper for demonstration purposes.")
    text.textLine("")
    text.textLine("Methodology")
    text.textLine("Randomized controlled study with adult participants over a six-month period.")
    text.textLine("")
    text.textLine("Results")
    text.textLine(paper["result"])
    text.textLine("")
    text.textLine("Conclusion")
    text.textLine("The study demonstrates clinical relevance for digital health interventions.")

    c.drawText(text)
    c.save()

print("Batch PDFs generated successfully.")
