from enum import Enum

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
        global_position = (offset_x + mouse_position[0] // TILE, offset_y + mouse_position[1] // TILE)
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
