from langchain_text_splitters import RecursiveCharacterTextSplitter



class ChunkService:


    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=1200,

            chunk_overlap=200,

            separators=[
                "\n\n",
                "\n",
                ".",
                " ",
                ""
            ]

        )



    def create_chunks(
            self,
            documents
    ):


        chunks = []


        for doc in documents:


            split_texts = self.splitter.split_text(
                doc["content"]
            )


            for index, text in enumerate(split_texts):


                chunks.append({

                    "content": text,

                    "page_number":
                    doc.get(
                        "page_number",
                        None
                    ),

                    "source":
                    doc.get(
                        "source",
                        "unknown"
                    ),

                    "chunk_id":
                    index

                })


        return chunks