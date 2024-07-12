
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Round:
    duration: int
    end_at: datetime
    name: str
    repeat: str
    start_at: datetime
    status: str

@dataclass
class Game:
    game_name: str
    now: datetime
    rounds: List[Round]
