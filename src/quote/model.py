from dataclasses import dataclass


@dataclass
class Quote:
    content: str
    source: str
