import pygame
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT


pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

TILE = 32
FPS = 60

CAMERA_CONTROL = [K_UP, K_LEFT, K_DOWN, K_RIGHT]


class Tiles(Enum):
    void = (0, 0, 0)
    wall = (80, 80, 80)
    zombie_spot = (20, 255, 20)
    base = (0, 137, 255)
    main_base = (0, 26, 255)
    enumy_base = (255, 0, 0)


class Settings(BaseSettings):
    """model which contain required environment variables"""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    token: str
