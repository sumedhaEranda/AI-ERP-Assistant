from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


VECTOR_DB_PATH = "vector_db"



def get_embedding_model():

    return HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )



def get_vector_db():

    embedding_model = get_embedding_model()


    db = Chroma(

        persist_directory=VECTOR_DB_PATH,

        embedding_function=embedding_model

    )


    return db



def save_documents(documents):


    embedding_model = get_embedding_model()


    texts = []

    metadatas = []



    for doc in documents:


        texts.append(

            doc["content"]

        )


        metadatas.append({

            "page_number":
            doc.get(
                "page_number",
                "unknown"
            ),

            "source":
            doc.get(
                "source",
                "unknown"
            ),

            "chunk_id":
            doc.get(
                "chunk_id",
                0
            )

        })



    db = Chroma.from_texts(

        texts=texts,

        embedding=embedding_model,

        metadatas=metadatas,

        persist_directory=VECTOR_DB_PATH

    )


    return db