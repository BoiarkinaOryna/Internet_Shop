import flask_login
from .settings import project_login

project_log.secret_key = "key"

login = flask_login.LoginManager(app = project_log)

@login.user_loader
def load(id):
    return User.query.get(id)
