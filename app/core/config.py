from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    ENV: str

    VECTOR_DB: str

    LLM_MODEL: str

    EMBEDDING_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()