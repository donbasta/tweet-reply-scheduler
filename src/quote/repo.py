import uuid

from .model import Quote


def create_quotes_table(con):
    try:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS quote(id text, quote_content text, quote_source text, is_posted int)")
    except Exception as e:
        print("ERROR:", e)


def insert_quote_to_db(con, quote):
    try:
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO quote VALUES ('{uuid.uuid4().hex}', '{quote.content}', '{quote.source}', 0)")
    except Exception as e:
        print(e)


def get_unposted_quote(con):
    try:
        cur = con.cursor()
        cur.execute(
            f"SELECT * FROM quotes WHERE is_posted = 0 LIMIT 1"
        )
        rows = cur.fetchall()
        if len(rows) == 0:
            raise "No available new quotes for today, please insert new quotes :("

        assert len(rows) == 1
        quote_id, quote_content, quote_source, _ = rows[0]
        update_quote_posted_status_as_true(con, quote_id)

        return Quote(quote_content, quote_source)
    except Exception as e:
        print(e)
    finally:
        pass


def update_quote_posted_status_as_true(con, id):
    try:
        cur = con.cursor()
        cur.execute(
            f"UPDATE quote SET is_posted = 1 WHERE id = {id}"
        )
    except Exception as e:
        print(e)
    finally:
        con.commit()


def check_quote_table(con):
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM quote")
        for row in res:
            print(row)
    except Exception as e:
        print(e)
