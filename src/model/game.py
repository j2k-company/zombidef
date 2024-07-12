from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from dataclasses_json import LetterCase, dataclass_json

from src.model.base import datetime_metadata


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Round:
    duration: int
    end_at: datetime = field(metadata=datetime_metadata)
    name: str
    repeat: str
    start_at: datetime = field(metadata=datetime_metadata)
    status: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Game:
    game_name: str
    now: datetime = field(metadata=datetime_metadata)
    rounds: List[Round]
