from dataclasses import dataclass
from enum import Enum
from typing import List

from dataclasses_json import LetterCase, dataclass_json


class CellType(Enum):
    WALL = "wall"
    DEFAULT = "default"


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Zpot:
    x: int
    y: int
    type: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class World:
    realm_name: str
    zpots: List[Zpot]
