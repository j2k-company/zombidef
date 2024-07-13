from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import LetterCase, dataclass_json

from src.model.base import Coordinate, datetime_metadata


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Base:
    attack: int
    health: int
    id: str
    last_attack: Coordinate
    x: int
    y: int
    range: int
    x: int
    y: int
    is_head: Optional[bool] = False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Enemy:
    attack: int
    health: int
    last_attack: Coordinate
    name: str
    x: int
    y: int
    is_head: Optional[bool] = False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Player:
    enemy_block_kills: int
    game_ended_at: datetime = field(metadata=datetime_metadata)
    gold: int
    name: str
    points: int
    zombie_kills: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Zombie:
    attack: int
    direction: str
    health: int
    id: str
    speed: int
    type: str
    wait_turns: int
    x: int
    y: int


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Units:
    enemy_blocks: Optional[List[Enemy]]
    player: Player
    realm_name: str
    turn: int
    turn_ends_in_ms: int
    zombies: Optional[List[Zombie]]
    base: Optional[List[Base]] = None
