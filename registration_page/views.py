import flask

def show_registration_page():
    return flask.render_template(template_name_or_list = "registration.html")