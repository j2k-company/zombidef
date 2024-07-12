from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from dataclasses_json import LetterCase, dataclass_json

from src.model.base import datetime_metadata


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Round:
    duration: int
    end_at: datetime = field(metadata=datetime_metadata)
    name: str
    start_at: datetime = field(metadata=datetime_metadata)
    status: str
    repeat: Optional[int] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Game:
    game_name: str
    now: datetime = field(metadata=datetime_metadata)
    rounds: List[Round]
