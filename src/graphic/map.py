from src.config import Tiles, z_to_color
from src.model.unit import Units
from src.model.world import CellType


class Map:
    def __init__(self):
        self.map = None
        self.real_map = None
        self.max_dist = 0
        self.enemies = []

    def create_map(self, zpots):
        self.max_dist = max(max(zpots, key=lambda x: x.x).x, max(zpots, key=lambda x: x.y).y) + 32
        self.map = [[Tiles.void for _ in range(self.max_dist)] for _ in range(self.max_dist)]
        for zpot in zpots:
            match zpot.type:
                case CellType.WALL.value:
                    self.map[zpot.y][zpot.x] = Tiles.wall
                case CellType.DEFAULT.value:
                    self.map[zpot.y][zpot.x] = Tiles.zombie_zpot

    def update_map(self, units: Units):
        self.real_map = units
        self.enemies = []
        for unit in units.base:
            self.map[unit.y][unit.x] = Tiles.main_base if unit.is_head else Tiles.base
        if units.enemy_blocks:
            for unit in units.enemy_blocks:
                self.map[unit.y][unit.x] = Tiles.enemy_main_base if unit.is_head else Tiles.enemy_base
        if units.zombies:
            for unit in units.zombies:
                self.map.enemies.append(z_to_color(unit))

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

    def get_main_base(self):
        for u in self.real_map.base:
            if u.is_head:
                return u
