from dataclasses import dataclass
from datetime import datetime
from marshmallow import fields

from dataclasses_json import LetterCase, config, dataclass_json


datetime_metadata = config(
    encoder=datetime.isoformat,
    decoder=datetime.fromisoformat,
    mm_field=fields.DateTime(format='iso')
)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Coordinate:
    x: int
    y: int
