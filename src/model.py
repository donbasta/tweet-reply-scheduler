from dataclasses import dataclass
from datetime import datetime

import requests


@dataclass
class Tweet:
    id: str
    date: datetime


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['authorization'] = "Bearer " + self.token
        return r
