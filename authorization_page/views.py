import flask
import flask_login
from registration_page.models import User
from project.settings import DB
from flask_login import current_user

def render_authorization_page():
    # print("User.query:", User.query.all())
    if flask.request.method == "POST":
        # if flask_login.current_user.is_authenticated:
            

            # print("Ви вже авторизовані")
            # return "Ви вже авторизовані"
        # else:
        for user in User.query.filter_by(name = flask.request.form.get("name")):
            if user.password == flask.request.form['password']:
                flask_login.login_user(user)
                return flask.redirect("/")
        # user_name = None
        # if flask_login.current_user.is_authenticated:
        #     user_name = flask_login.current_user.name
                    
                
    return flask.render_template(template_name_or_list = "authorization.html")