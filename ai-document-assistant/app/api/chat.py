from fastapi import APIRouter, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


rag_service = None



@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest
):

    global rag_service

    try:

        if rag_service is None:

            rag_service = RAGService()


        answer = rag_service.ask_question(
            request.question
        )


        return ChatResponse(

            question=request.question,

            answer=answer

        )


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )