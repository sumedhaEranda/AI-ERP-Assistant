from pypdf import PdfReader
import os



class PDFParser:



    def extract_text(
            self,
            file_path
    ):


        documents = []


        reader = PdfReader(
            file_path
        )


        file_name = os.path.basename(
            file_path
        )


        for page_number, page in enumerate(
            reader.pages,
            start=1
        ):


            text = page.extract_text()


            if text and text.strip():


                documents.append({

                    "content": text.strip(),

                    "page_number": page_number,

                    "source": file_name

                })


        return documents