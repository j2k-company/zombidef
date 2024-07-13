from src.config import Tiles, real_to_color
from src.model.unit import Units
from src.model.world import CellType


class Map:
    def __init__(self):
        self.map = None
        self.real_map = None

    def create_map(self, zpots):
        max_dist = max(max(zpots, key=lambda x: x.x).x, max(zpots, key=lambda x: x.y).y) + 10
        self.map = [[Tiles.void for _ in range(max_dist)] for _ in range(max_dist)]
        for zpot in zpots:
            match zpot.type:
                case CellType.WALL.value:
                    self.map[zpot.y][zpot.x] = Tiles.wall
                case CellType.DEFAULT.value:
                    self.map[zpot.y][zpot.x] = Tiles.zombie_zpot

    def update_map(self, units: Units):
        self.real_map = units
        for unit in units.base:
            self.map[unit.y][unit.x] = real_to_color(unit)
        for unit in units.enemy_blocks:
            self.map[unit.y][unit.x] = real_to_color(unit)

    def get_block(self, x, y):
        match self.map[y][x]:
            case Tiles.base | Tiles.main_base:
                for i in self.real_map.base:
                    if i.x == x and i.y == y:
                        return i
            case Tiles.enemy_base | Tiles.enemy_main_base:
                for i in self.real_map.enemy_blocks:
                    if i.x == x and i.y == y:
                        return i
