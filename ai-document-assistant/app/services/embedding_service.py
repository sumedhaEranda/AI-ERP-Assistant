from langchain_community.embeddings import HuggingFaceEmbeddings



class EmbeddingService:


    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(

            model_name="sentence-transformers/all-MiniLM-L6-v2"

        )


    def create_embeddings(
            self,
            chunks
    ):


        texts = []


        for chunk in chunks:

            texts.append(
                chunk["content"]
            )


        vectors = self.embedding_model.embed_documents(
            texts
        )


        return vectors