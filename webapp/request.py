import urllib.request,json

# Getting api key
secret_key = None

def configure_request(app):
    global  secret_key
    secret_key = app.config["SECRET_KEY"]
    
   