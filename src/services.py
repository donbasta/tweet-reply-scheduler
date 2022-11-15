from .quote.usecase import *
from .tweet.usecase import *
from .context import get_context


def check_tables():
    try:
        ctx = get_context()
        con = ctx["DB"]

        cur = con.cursor()
        cur.execute(
            "SELECT name FROM  sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(e)
    finally:
        pass
        # con.commit()
