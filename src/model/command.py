from dataclasses import dataclass
from typing import List

from src.model.base import Coordinate


@dataclass
class AttackCommand:
    block_id: str
    target: Coordinate


@dataclass
class Command:
    attack: List[AttackCommand]
    build: List[Coordinate]
    move_base: Coordinate
