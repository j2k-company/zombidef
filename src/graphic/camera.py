from enum import Enum

from pygame.draw import rect
from pygame import K_UP, K_LEFT, K_DOWN, K_RIGHT, K_e

from src.config import TILE, Tiles


class Direction(Enum):
    up = K_UP
    down = K_DOWN
    left = K_LEFT
    right = K_RIGHT
    go_to_base = K_e


class Camera:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0

    def keyboard_control(self, button: int, max_dist, main_base=None):
        match button:
            case Direction.up.value:
                if self.offset_y > 0:
                    self.offset_y -= 1
            case Direction.down.value:
                if self.offset_y + 32 < max_dist:
                    self.offset_y += 1
            case Direction.left.value:
                if self.offset_x > 0:
                    self.offset_x -= 1
            case Direction.right.value:
                if self.offset_x + 32 < max_dist:
                    self.offset_x += 1
            case Direction.go_to_base.value:
                self.offset_x = main_base.x
                self.offset_y = main_base.y

    def read_response(self, response: dict):
        ...

    def custom_draw(self, sc, game_map):
        for y in range(self.offset_y, self.offset_y + 32):
            for x in range(self.offset_x, self.offset_x + 32):
                relative_x = (x - self.offset_x) * TILE
                relative_y = (y - self.offset_y) * TILE
                if game_map.map[y][x] is None:
                    game_map.map[y][x] = Tiles.void
                rect(sc, game_map.map[y][x].value, (relative_x, relative_y, relative_x + TILE, relative_y + TILE))
        for i in game_map.enemies:
            if i.x in range(self.offset_y, self.offset_y + 32) and i.y in range(self.offset_y, self.offset_y + 32):
                relative_x = (i.x - self.offset_x) * TILE
                relative_y = (i.y - self.offset_y) * TILE
                rect(sc, i.color, (relative_x, relative_y, relative_x + TILE * 0.5, relative_y + TILE * 0.5))
