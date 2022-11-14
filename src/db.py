from .model import Tweet

import sqlite3


def create_tweet_table(con):
    try:
        cur = con.cursor()
        cur.execute("CREATE TABLE tweet(id int, date text)")
    except Exception as e:
        print(e)


def connect_db(db_source):
    try:
        con = sqlite3.connect(db_source)
        return con
    except Exception as e:
        print(e)


def insert_tweet_to_db(con, tweet_id):
    try:
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO tweet VALUES ('{tweet_id}', datetime('now'))")
    except Exception as e:
        print(e)


def get_latest_tweet(con):
    try:
        cur = con.cursor()
        cur.execute(
            "SELECT id, date FROM tweet WHERE date = (SELECT MAX(date) FROM tweet)")
        rows = cur.fetchall()
        if len(rows) == 0:
            raise "Empty Table"

        tweet_id, tweet_date = rows[0]
        return Tweet(tweet_id, tweet_date)
    except Exception as e:
        print(e)


def check_tweet_table(con):
    cur = con.cursor()
    res = cur.execute("SELECT * FROM tweet")
    for row in res:
        print(row)
