from enum import Enum

from pygame.draw import rect
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT

from src.config import TILE


class Direction(Enum):
    up = K_UP
    down = K_DOWN
    left = K_LEFT
    right = K_RIGHT


class Camera:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0

    def keyboard_control(self, button: int):
        match button:
            case Direction.up.value:
                if self.offset_y > 0:
                    self.offset_y -= 1
            case Direction.down.value:
                self.offset_y += 1
            case Direction.left.value:
                if self.offset_x > 0:
                    self.offset_x -= 1
            case Direction.right.value:
                self.offset_x += 1

    def custom_draw(self, sc, game_map):
        for y in range(self.offset_y, self.offset_y + 16):
            for x in range(self.offset_x, self.offset_x + 16):
                relative_x = (x - self.offset_x) * TILE
                relative_y = (y - self.offset_y) * TILE
                rect(sc, game_map[y][x].value, (relative_x, relative_y, relative_x + TILE, relative_y + TILE))
