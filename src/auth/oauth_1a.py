import hmac
import hashlib
import base64
import re
import secrets
import time
import urllib.parse


def make_digest(message, key):
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature = digester.digest()
    signature = base64.urlsafe_b64encode(signature)
    return str(signature, 'UTF-8')


def create_signature_oauth1a(ctx, http_method="", base_url=""):
    oauth_parameters = {
        "oauth_consumer_key": ctx["API_KEY"],
        "oauth_nonce": re.sub('[\W_]+', '', secrets.token_urlsafe()),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": ctx["API_KEY_SECRET"],
        "oauth_version": "1.0",
    }

    dst = ""
    for k, v in oauth_parameters.items():
        k_encode = urllib.parse.quote(k)
        v_encode = urllib.parse.quote(v)

        f = f'{k_encode}={v_encode}'
        dst += f
        if k != "oauth_version":
            dst += "&"

    signature_base_string = http_method.upper()
    signature_base_string += "&"
    signature_base_string += urllib.parse.quote(base_url)
    signature_base_string += "&"
    signature_base_string += urllib.parse.quote(dst)
    print("signature base string:", signature_base_string, "\n")

    consumer_secret = ctx["API_KEY_SECRET"]
    user_oauth_token_secret = ctx["USER_KEY_SECRET"]
    signing_key = f"{urllib.parse.quote(consumer_secret)}&{urllib.parse.quote(user_oauth_token_secret)}"
    print("signing key:", signing_key, "\n")

    signature = make_digest(signature_base_string, signing_key)
    print("signature:", signature, "\n")
    return signature


def create_authorization_header_oauth1a(ctx, http_method, url):
    oauth_parameters = {
        "oauth_consumer_key": ctx["API_KEY"],
        "oauth_nonce": re.sub('[\W_]+', '', secrets.token_urlsafe()),
        "oauth_signature": create_signature_oauth1a(ctx, http_method, url),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_token": ctx["API_KEY_SECRET"],
        "oauth_version": "1.0",
    }
    dst = "OAuth "
    for k, v in oauth_parameters.items():
        k_encode = urllib.parse.quote(k)
        v_encode = urllib.parse.quote(v)

        f = f'{k_encode}="{v_encode}"'
        dst += f
        if k != "oauth_version":
            dst += ", "
    return dst
