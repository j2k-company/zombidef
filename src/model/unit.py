from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import LetterCase, dataclass_json

from src.model.base import Coordinate, datetime_metadata


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Base:
    attack: Optional[int] = None
    health: Optional[int] = None
    id: Optional[str] = None
    last_attack: Optional[Coordinate] = None
    x: Optional[int] = None
    y: Optional[int] = None
    range: int = 0
    x: Optional[int] = None
    y: Optional[int] = None
    is_head: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Enemy:
    attack: Optional[int] = None
    health: Optional[int] = None
    last_attack: Optional[Coordinate] = None
    name: Optional[str] = None
    x: Optional[int] = None
    y: Optional[int] = None
    is_head: bool = False


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Player:
    game_ended_at: datetime = field(metadata=datetime_metadata)
    gold: int
    name: Optional[str] = None
    enemy_block_kills: int = 0
    points: int = 0
    zombie_kills: int = 0


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
    player: Player
    realm_name: str
    turn: int
    turn_ends_in_ms: int
    enemy_blocks: Optional[List[Enemy]] = tuple()
    zombies: Optional[List[Zombie]] = tuple()
    base: Optional[List[Base]] = tuple()
