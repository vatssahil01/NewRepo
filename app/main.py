from fastapi import FastAPI, UploadFile, File, HTTPException
from datetime import datetime
from app.core.parser import parse_pdf
from app.core.privacy import validate_privacy
from app.core.extractor import extract_key_findings, extract_p_values
from app.core.analysis import compute_confidence
from app.core.summarizer import generate_summary
from app.core.citations import generate_citation
from app.audit.logger import log_event
from app.models.enums import AudienceType
from app.models.output import GeneratedOutput

from typing import List
from app.core.batch import create_batch_job, update_batch_job

from app.core.batch import get_batch_job


import shutil
import os

app = FastAPI(title="Clinical Research Documentation Assistant")

@app.post("/process")
async def process_document(
    file: UploadFile = File(...),
    audience: AudienceType = AudienceType.clinician
):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    sections = parse_pdf(file_path)

    if not validate_privacy(sections.raw_text):
        os.remove(file_path)
        raise HTTPException(status_code=400, detail="Privacy violation detected")

    findings = extract_key_findings(sections.results)
    p_values = extract_p_values(sections.raw_text)

    confidence = compute_confidence(findings, p_values)
    summary = generate_summary(findings, audience)

    citation = generate_citation("Uploaded Paper", "Public Journal")

    log_event("Document processed successfully")

    os.remove(file_path)

    return GeneratedOutput(
        audience=audience,
        summary=summary,
        confidence_score=confidence,
        citations=[citation],
        timestamp=datetime.utcnow()
    )


@app.post("/process-batch")
async def process_batch(files: List[UploadFile] = File(...)):
    job_id = create_batch_job(len(files))

    for file in files:
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        sections = parse_pdf(file_path)

        if not validate_privacy(sections.raw_text):
            os.remove(file_path)
            continue

        findings = extract_key_findings(sections.results)
        p_values = extract_p_values(sections.raw_text)

        confidence = compute_confidence(findings, p_values)
        summary = generate_summary(findings, AudienceType.researcher)

        result = {
            "file": file.filename,
            "summary": summary,
            "confidence": confidence
        }

        update_batch_job(job_id, result)
        os.remove(file_path)

    return {
    "job_id": job_id,
    "status": "completed",
    "processed_files": len(files),
    "details": get_batch_job(job_id)["results"]
}




@app.get("/")
def health():
    return {"status": "ok"}

