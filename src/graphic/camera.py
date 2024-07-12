from enum import Enum

from pygame.draw import rect
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT

from src.config import TILE


class Direction(Enum):
    UP = K_UP
    DOWN = K_DOWN
    LEFT = K_LEFT
    RIGHT = K_RIGHT


class Camera:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0

    def keyboard_control(self, button: int):
        match button:
            case Direction.UP.value:
                if self.offset_y > 0:
                    self.offset_y -= 1
            case Direction.DOWN.value:
                self.offset_y += 1
            case Direction.LEFT.value:
                if self.offset_x > 0:
                    self.offset_x -= 1
            case Direction.RIGHT.value:
                self.offset_x += 1

    def custom_draw(self, sc, game_map):
        for y in range(self.offset_y, self.offset_y + 16):
            for x in range(self.offset_x, self.offset_x + 16):
                relative_x = (x - self.offset_x) * TILE
                relative_y = (y - self.offset_y) * TILE
                rect(sc, game_map[y][x].value, (relative_x, relative_y, relative_x + TILE, relative_y + TILE))
