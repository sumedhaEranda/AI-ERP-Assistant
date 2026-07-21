from app.services.parser import PDFParser
from app.services.chunk_service import ChunkService
from app.vectorstore.chroma_db import save_documents



class DocumentProcessor:



    def __init__(self):

        self.parser = PDFParser()

        self.chunker = ChunkService()



    def process_document(
            self,
            file_path
    ):


        # 1. Extract PDF text

        documents = self.parser.extract_text(
            file_path
        )


        if not documents:

            raise Exception(
                "No text found in PDF"
            )



        # 2. Create chunks

        chunks = self.chunker.create_chunks(
            documents
        )



        # 3. Save into ChromaDB

        save_documents(
            chunks
        )


        return {

            "pages":
            len(documents),

            "chunks":
            len(chunks),

            "status":
            "processed"

        }