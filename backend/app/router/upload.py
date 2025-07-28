from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import uuid
from app.services.save_file import save_uploaded_file
from app.services.extract_text import extract_text
from app.services.create_chunks import create_chunks
from app.services.embed_index import embed_and_store

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    userid = "test_id"
    file_id = str(uuid.uuid4())
    save_path = save_uploaded_file(file, userid, file_id)
    
    try:
        text = extract_text(save_path)
        chunks = create_chunks(text)
        embed_and_store(file_id ,chunks, {"user_id": userid, "file_path": save_path})
    except ValueError as e:
        return JSONResponse(content={"status": "error", "message": str(e)})
    
    return JSONResponse(content={
        "status": "success", 
        "path": save_path, 
        "num_chunks": len(chunks)
        })
