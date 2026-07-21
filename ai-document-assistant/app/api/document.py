from fastapi import APIRouter
import os

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_FOLDER = "uploaded_documents"


@router.get("/")
async def get_documents():

    if not os.path.exists(UPLOAD_FOLDER):

        return []

    files = []

    for file in os.listdir(UPLOAD_FOLDER):

        files.append(
            {
                "file_name": file
            }
        )

    return files