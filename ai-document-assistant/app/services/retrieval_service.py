from app.vectorstore.chroma_db import get_vector_db


class RetrievalService:


    def __init__(self):

        self.db = get_vector_db()



    def search(
            self,
            question,
            limit=5
    ):


        results = self.db.similarity_search_with_score(
            question,
            k=limit
        )


        documents = []


        for doc, score in results:


            documents.append(doc)


        return documents