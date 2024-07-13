from enum import Enum
from math import sqrt

from pygame import K_1, K_2, K_3, K_4
from pygame.mouse import get_pos

from src.config import TILE
from src.graphic.map import Map
from src.model.base import Coordinate
from src.model.command import Command, AttackCommand
from src.model.unit import Base


class Motion(Enum):
    build = K_1
    attack = K_2
    move_base = K_3
    clear_buffer = K_4


class Player:
    def __init__(self, game_map: Map):
        self.game_map = game_map
        self.command_buffer = None
        self.attacking_block: Base = None

    def keyboard_control(self, button: int, offset_x, offset_y):
        mouse_position = get_pos()
        global_position = (offset_x + mouse_position[0] % 32, offset_y + mouse_position[1] % 32)
        match button:
            case Motion.build.value:
                self.get_command_buffer().build.append(Coordinate(global_position[0], global_position[1]))
            case Motion.attack.value:
                if self.attacking_block:
                    self.get_command_buffer().attack.append(
                        AttackCommand(self.attacking_block.id, Coordinate(global_position[0], global_position[1])))
                else:
                    self.attacking_block = self.game_map.get_block(global_position[0], global_position[1])
            case Motion.move_base.value:
                self.get_command_buffer().move_base = Coordinate(global_position[0], global_position[1])
            case Motion.clear_buffer.value:
                self.command_buffer = None

    def get_command_buffer(self):
        if self.command_buffer is None:
            self.command_buffer = Command([], [], Coordinate(-1, -1))
        return self.command_buffer

    def update(self):
        if self.game_map.real_map is None:
            return
        for b in self.game_map.real_map.base:
            if b.is_head:
                dist = 8
            else:
                dist = 5
            zombies = filter(lambda z: dist >= sqrt(abs(b.x - z.x) ^ 2 + abs(b.y - z.y) ^ 2),
                             self.game_map.real_map.zombies)
            zombies = sorted(zombies, key=lambda z: sqrt(abs(b.x - z.x) ^ 2 + abs(b.y - z.y) ^ 2))
            self.get_command_buffer().attack.append(AttackCommand(b.id, Coordinate(zombies[0].x, zombies[1].y)))
