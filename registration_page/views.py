import flask
from .models import User
from project.settings import DB

def show_registration_page():
    print(User.query.all())
    print("flask.request.method =", flask.request.method)
    if flask.request.method == "POST":
        print("Post")
        if flask.request.form['password1'] == flask.request.form['password2']:   
            users = User( 
                name = flask.request.form['name'],
                email = flask.request.form['email'],
                password = flask.request.form['password1'],
                password_confirmation = flask.request.form["password2"]

            )
            try:
                DB.session.add(users)
                DB.session.commit()
            except:
                return "ERROR"
            else:
                pass
    return flask.render_template(template_name_or_list = "registration.html")