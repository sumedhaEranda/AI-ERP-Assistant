from pydantic import BaseModel



class DocumentChunk(BaseModel):

    id: str | None = None


    document_name: str


    page_number: int


    content: str


    embedding: list[float] | None = None


    metadata: dict = {}