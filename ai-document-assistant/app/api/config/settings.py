from pydantic_settings import BaseSettings



class Settings(BaseSettings):


    OPENAI_API_KEY: str


    VECTOR_DB_PATH: str = "vector_db"


    UPLOAD_FOLDER: str = "uploaded_documents"



    class Config:

        env_file = ".env"



settings = Settings()