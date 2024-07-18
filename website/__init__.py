from flask import Flask

from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.services.databases import Databases


client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('669471b2001b22338164')
client.set_key('be9003b6a6e3fbbea865b8a440d8ee7b7a76ebf27ee33af9c6d737f790db1eb612da03844aa1f285ba20aecce718df86c9e9dbf5947d8aa22e4400cd9b94a635dc1238a1278a3acb8b8595ead72f1ff56cdeb86b1c81b4e2c7c440fc733de85d0d8675e68ec26a2a9738584dee02adf0f09e907b348598df7fb8930c38e9d871')

account = Account(client)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "fgnurr449KFNIifoge4prfff"

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app