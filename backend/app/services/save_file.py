import os
from fastapi import UploadFile

def save_uploaded_file(file: UploadFile, user_id: str, file_id: str):
    upload_dir = f"/app/data/uploads/{user_id}"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, f"{file_id}_{file.filename}")
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
