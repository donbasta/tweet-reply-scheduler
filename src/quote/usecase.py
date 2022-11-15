from .model import *
from .repo import *

from ..context import get_context
from ..db import *
from ..api import *
from ..data import *


def add_quote(content, source=None):
    quote = Quote(content, source)

    try:
        ctx = get_context()
        con = ctx["DB"]

        insert_quote_to_db(con, quote)
    except Exception as e:
        print(e)
    finally:
        con.commit()


def see_quote():
    try:
        ctx = get_context()
        con = ctx["DB"]

        check_quote_table(con)
    except Exception as e:
        print(e)
