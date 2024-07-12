from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

TILE = 32
FPS = 60


class Tiles(Enum):
    void = (0, 0, 0)
    wall = (80, 80, 80)
    zombie_spot = (20, 255, 20)
    base = (0, 137, 255)
    enumy_base = (255, 0, 0)


class Settings(BaseSettings):
    """model which contain required environment variables"""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    token: str
