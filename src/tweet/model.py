from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tweet:
    id: str
    date: datetime
