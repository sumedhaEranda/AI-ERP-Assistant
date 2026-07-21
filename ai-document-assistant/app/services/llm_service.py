from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()


class LLMService:


    def __init__(self):

        self.llm = ChatGroq(

            model=os.getenv(
                "LLM_MODEL",
                "llama-3.1-8b-instant"
            ),

            temperature=0.2,

            api_key=os.getenv(
                "GROQ_API_KEY"
            )

        )


    def generate_answer(
            self,
            context,
            question
    ):


        prompt = f"""

You are an AI assistant for external system user manuals.

Rules:
- Answer only using the provided document context.
- Do not make assumptions.
- If the answer is not available in the document,
  say "Information not found in the document."


Document Context:

{context}


User Question:

{question}

"""


        response = self.llm.invoke(
            prompt
        )


        return response.content