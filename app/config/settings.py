from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    QDRANT_HOST = os.getenv("QDRANT_HOST", "http://localhost:6333")
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

settings = Settings()