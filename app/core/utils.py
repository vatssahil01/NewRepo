import os
import shutil

def save_temp_file(upload_file):
    path = f"temp_{upload_file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return path

def cleanup_file(path):
    if os.path.exists(path):
        os.remove(path)
