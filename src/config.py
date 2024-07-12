from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """model which contain required environment variables"""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    token: str