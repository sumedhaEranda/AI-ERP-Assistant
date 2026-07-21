# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.upload import router as upload_router
# from app.api.chat import router as chat_router
# from app.api.document import router as document_router


# app = FastAPI(
#     title="AI Document Assistant",
#     description="AI system to understand PDF manuals and answer workflow questions",
#     version="1.0.0"
# )


# # CORS (React frontend connection)
# app.add_middleware(
#     CORSMiddleware,

#     allow_origins=[
#         "http://localhost:3000"
#     ],

#     allow_credentials=True,

#     allow_methods=[
#         "*"
#     ],

#     allow_headers=[
#         "*"
#     ]
# )


# # Register API Routes

# app.include_router(
#     upload_router
# )

# app.include_router(
#     chat_router
# )

# app.include_router(
#     document_router
# )


# # Health Check API

# @app.get("/")
# async def root():

#     return {
#         "application":
#         "AI Document Assistant",

#         "status":
#         "Running",

#         "version":
#         "1.0.0"
#     }



# @app.get("/health")
# async def health_check():

#     return {
#         "status":"OK"
#     }


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.document import router as document_router


app = FastAPI(
    title="AI Document Assistant",
    description="AI system to understand PDF manuals and answer workflow questions",
    version="1.0.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Routes

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(document_router)



@app.get("/")
async def root():

    return {
        "application": "AI Document Assistant",
        "status": "Running",
        "version": "1.0.0"
    }



@app.get("/health")
async def health_check():

    return {
        "status": "OK"
    }