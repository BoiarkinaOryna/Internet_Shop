import flask_login
# import flask
from .settings import shop
from registration_page.models import User
# import requests

# shop = flask.Flask(__name__)
# url = 'http://127.0.0.1:5000/registration'
shop.secret_key = "067bbv48jbvd3sill911vbhtfjklks378zwr6h9"

# response = requests.put(url)
# response = requests.post(url = url, data = flask.request.form)

# if response.status_code == 405:
#     print("Error 405: Method Not Allowed")
# else:
#     print("Unexpected response:", response.status_code)
    
login = flask_login.LoginManager(shop)
login.init_app(shop)

@login.user_loader
def load(id):
    return User.query.get(id)
