from requests_oauthlib import OAuth1

import json
import requests


def post_reply_to_tweet(ctx, parent_id, text):
    url = f'https://api.twitter.com/2/tweets'

    request_token_url = "https://api.twitter.com/oauth/request_token"

    consumer_key = ctx["API_KEY"]
    consumer_secret = ctx["API_KEY_SECRET"]

    # oauth = OAuth1Session(ctx["API_KEY"], client_secret=ctx["API_KEY_SECRET"])
    # try:
    #     fetch_response = oauth.fetch_request_token(request_token_url)
    # except ValueError:
    #     print(
    #         "There may have been an issue with the consumer_key or consumer_secret you entered."
    #     )
    # resource_owner_key = fetch_response.get("oauth_token")
    # resource_owner_secret = fetch_response.get("oauth_token_secret")

    # base_authorization_url = "https://api.twitter.com/oauth/authorize"
    # authorization_url = oauth.authorization_url(base_authorization_url)
    # #print("Please go here and authorize: %s" % authorization_url)
    # verifier = input("Paste the PIN here: ")

    # access_token_url = "https://api.twitter.com/oauth/access_token"
    # oauth = OAuth1Session(
    #     consumer_key,
    #     client_secret=consumer_secret,
    #     resource_owner_key=resource_owner_key,
    #     resource_owner_secret=resource_owner_secret,
    #     verifier=verifier,
    # )
    # oauth_tokens = oauth.fetch_access_token(access_token_url)
    # # access_token = oauth_tokens["oauth_token"]
    # # access_token_secret = oauth_tokens["oauth_token_secret"]
    access_token = ctx["USER_KEY"]
    access_token_secret = ctx["USER_KEY_SECRET"]

    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # auth = OAuth1(ctx["API_KEY"], ctx["API_KEY_SECRET"],
    #              ctx["USER_KEY"], ctx["USER_KEY_SECRET"])
    # oauth_signature = create_authorization_header_oauth1a(ctx, 'POST', url)
    # oauth_signature = create_signature_oauth1a(ctx, 'POST', url)
    # print("the oauth signature is: ", oauth_signature)
    headers = {
        "Content-type": "application/json",
    }
    data = {
        "text": text,
        "reply": {
            "in_reply_to_tweet_id": parent_id
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=oauth)
    print(r.status_code)
    print(r.json())
    return r.json()['data']


def get_tweet(auth, id):
    r = requests.get(
        f'https://api.twitter.com/2/tweets?ids={id}&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username',
        auth=auth
    )
    data = r.json()
    print(json.dumps(data, indent=2))
    return data
