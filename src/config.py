from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://mongodb:27017"
    APP_TITLE: str = "ToDo Application"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
