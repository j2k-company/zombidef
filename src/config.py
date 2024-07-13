from dataclasses import dataclass

import pygame
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT, K_1, K_2, K_3, K_4, K_e

from src.model.unit import Zombie

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

TILE = 16
FPS = 60

CAMERA_CONTROL = [K_UP, K_LEFT, K_DOWN, K_RIGHT, K_e]
PLAYER_CONTROL = [K_1, K_2, K_3, K_4]


@dataclass
class ZombieColor:
    attack: int
    direction: str
    health: int
    id: str
    speed: int
    color: tuple
    type: str
    wait_turns: int
    x: int
    y: int


def z_to_color(z: Zombie):
    if z.type == 'normal':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (0, 255, 0), z.type, z.wait_turns, z.x, z.y)
    elif z.type == 'fast':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (0, 0, 255), z.type, z.wait_turns, z.x, z.y)
    elif z.type == 'bomber':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (80, 80, 80), z.type, z.wait_turns, z.x, z.y)
    elif z.type == 'liner':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (80, 255, 255), z.type, z.wait_turns, z.x,
                           z.y)
    elif z.type == 'juggernaut':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (255, 255, 80), z.type, z.wait_turns, z.x,
                           z.y)
    elif z.type == 'chaos_knight':
        return ZombieColor(z.attack, z.direction, z.health, z.id, z.speed, (255, 80, 255), z.type, z.wait_turns, z.x,
                           z.y)


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
