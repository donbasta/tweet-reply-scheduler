import os

from dotenv import load_dotenv

from .db import connect_db
from .auth.bearer_auth import BearerAuth


def get_context():
    load_dotenv()
    con = connect_db("data.db")
    bearer_token = os.getenv("BEARER_TOKEN")
    api_key = os.getenv("API_KEY")
    api_key_secret = os.getenv("API_KEY_SECRET")
    user_key = os.getenv("USER_KEY")
    user_key_secret = os.getenv("USER_KEY_SECRET")
    bearer_auth = BearerAuth(bearer_token)
    return {
        "API_KEY": api_key,
        "API_KEY_SECRET": api_key_secret,
        "USER_KEY": user_key,
        "USER_KEY_SECRET": user_key_secret,
        "BEARER_TOKEN": bearer_token,
        "AUTH": bearer_auth,
        "DB": con
    }
