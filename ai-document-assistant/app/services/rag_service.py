from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService


class RAGService:


    def __init__(self):

        self.retriever = RetrievalService()

        self.llm = LLMService()



    def ask_question(self, question):


        documents = self.retriever.search(
            question
        )


        context = "\n\n".join(
            [
                doc.page_content
                for doc in documents
            ]
        )


        answer = self.llm.generate_answer(
            context,
            question
        )


        return answer