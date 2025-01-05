from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://mongodb:27017"
    APP_TITLE: str = "ToDo Application"


settings = Settings()
