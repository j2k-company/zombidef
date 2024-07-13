import pygame
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT, K_1, K_2, K_3, K_4, K_e

from src.model.unit import Base, Enemy

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

TILE = 32
FPS = 60

CAMERA_CONTROL = [K_UP, K_LEFT, K_DOWN, K_RIGHT, K_e]
PLAYER_CONTROL = [K_1, K_2, K_3, K_4]


def real_to_color(real_cell):
    if real_cell is Base:
        if real_cell.is_head:
            return Tiles.main_base
        else:
            return Tiles.base
    elif real_cell is Enemy:
        if real_cell.is_head:
            return Tiles.enemy_main_base
        else:
            return Tiles.enemy_base


class Tiles(Enum):
    void = (0, 0, 0)
    wall = (80, 80, 80)
    zombie_zpot = (20, 255, 20)
    base = (0, 137, 255)
    main_base = (0, 26, 255)
    enemy_base = (255, 50, 0)
    enemy_main_base = (255, 0, 0)


class Settings(BaseSettings):
    """model which contain required environment variables"""
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    token: str
