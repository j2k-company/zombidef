from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.model.base import Coordinate


@dataclass
class Base:
    attack: int
    health: int
    id: str
    is_head: bool
    last_attack: Coordinate
    x: int
    y: int
    range: int
    x: int
    y: int


@dataclass
class Enemy:
    attack: int
    health: int
    is_head: bool
    last_attack: Coordinate
    name: str
    x: int
    y: int


@dataclass
class Player:
    enemy_block_kills: int
    game_ended_at: datetime
    gold: int
    name: str
    points: int
    zombie_kills: int


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


@dataclass
class Units:
    base: List[Base]
    enemy_blocks: List[Enemy]
    player: Player
    realm_name: str
    turn: int
    turn_ends_in_ms: int
    zombies: List[Zombie]
