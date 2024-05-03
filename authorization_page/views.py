import flask

def show_authorization_page():
    
    return flask.render_template(template_name_or_list = "authorization.html")