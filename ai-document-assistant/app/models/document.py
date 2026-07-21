from pydantic import BaseModel
from datetime import datetime



class Document(BaseModel):

    id: int | None = None

    file_name: str

    file_path: str

    uploaded_by: str | None = None

    uploaded_date: datetime | None = None

    status: str = "uploaded"

    version: str = "1.0"