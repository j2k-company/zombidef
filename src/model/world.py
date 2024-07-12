from dataclasses import dataclass
from enum import Enum
from typing import List


class CellType(Enum):
    WALL = "wall"
    DEFAULT = "default"


@dataclass
class Zpot:
    x: int
    y: int
    type: str


@dataclass
class World:
    realm_name: str
    zpots: List[Zpot]
