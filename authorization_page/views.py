import flask
import flask_login
from registration_page.models import User
from project.settings import DB

def show_authorization_page():
    print(User.query.all())
    if flask.request.method == "POST":
        if flask_login.current_user.is_authenticated:
            return "Ви вже авторизовані"
        else:
            for user in User.query.filter_by(name = flask.request.form['name']):
                if user.password == flask.request.form['password']:
                    flask_login.login_user(user)
                    return "ERROR"
                
    return flask.render_template(template_name_or_list = "authorization.html")