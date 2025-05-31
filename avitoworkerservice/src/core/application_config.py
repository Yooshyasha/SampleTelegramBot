from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()

class ApplicationConfig(BaseSettings):
    JWT_SECRET: str = os.getenv("JWT_SECRET", "")

    EUREKA_DEFAULT_ZONE: str = os.getenv("EUREKA_DEFAULT_ZONE", "http://localhost:8761/eureka")

    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    
    shutdown_timeout: int = 5