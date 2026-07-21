from langchain_chroma import Chroma

db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./vector_db"
)

db.persist()