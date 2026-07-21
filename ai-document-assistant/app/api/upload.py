from fastapi import APIRouter, UploadFile, File

import os
import shutil


from app.services.document_processor import DocumentProcessor


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


UPLOAD_FOLDER = "uploaded_documents"



processor = DocumentProcessor()



@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...)
):


    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )


    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    # IMPORTANT
    # Process PDF

    result = processor.process_document(
        file_path
    )


    return {

        "file_name": file.filename,

        "file_path": file_path,

        "status": "processed",

        "pages": result["pages"],

        "chunks": result["chunks"]

    }