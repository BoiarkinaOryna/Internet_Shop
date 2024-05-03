import flask

auth = flask.Blueprint(
    name = "authorization_page",
    import_name = "app",
    template_folder = "authorization_page/templates",
    static_folder = "authorization_page/static",
    static_url_path = "/authorization_page/static"
)