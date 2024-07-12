from dataclasses import dataclass
from typing import List

from dataclasses_json import LetterCase, dataclass_json

from src.model.base import Coordinate


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class AttackCommand:
    block_id: str
    target: Coordinate


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Command:
    attack: List[AttackCommand]
    build: List[Coordinate]
    move_base: Coordinate
