import uuid
from typing import Dict, List

BATCH_JOBS: Dict[str, dict] = {}

def create_batch_job(total_files: int) -> str:
    job_id = str(uuid.uuid4())
    BATCH_JOBS[job_id] = {
        "status": "processing",
        "total": total_files,
        "processed": 0,
        "results": []
    }
    return job_id

def update_batch_job(job_id: str, result: dict):
    job = BATCH_JOBS[job_id]
    job["processed"] += 1
    job["results"].append(result)
    if job["processed"] >= job["total"]:
        job["status"] = "completed"

def get_batch_job(job_id: str):
    return BATCH_JOBS.get(job_id)
