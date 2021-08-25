import urllib.request,json


# Getting api key
secret_key = None
# Getting the news base url
quote_api = None


def configure_request(app):
    global  secret_key, quote_api
    secret_key = app.config["SECRET_KEY"]
    quote_api = app.config["QUOTES_API"]
   