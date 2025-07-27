from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
import uuid
from app.services.save_file import save_uploaded_file

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    userid = "test_id"
    file_id = str(uuid.uuid4())
    save_path = save_uploaded_file(file, userid, file_id)
    return JSONResponse(content={"status": "success", "path": save_path})
