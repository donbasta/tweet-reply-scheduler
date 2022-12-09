from .api import *
from .repo import *
from .model import *

from ..context import get_context
from ..db import *

from ..data import *


def post_new_tweet_reply():
    try:
        ctx = get_context()
        con = ctx["DB"]

        check_tweet_table(con)

        latest_tweet = get_latest_tweet(con)
        latest_tweet_id = latest_tweet.id
        new_tweet = post_reply_to_tweet(
            ctx, latest_tweet_id, get_tweet_text(latest_tweet.date))
        new_tweet_id = new_tweet['id']
        insert_tweet_to_db(con, new_tweet_id)

    except Exception as e:
        print(e)

    finally:
        con.commit()
