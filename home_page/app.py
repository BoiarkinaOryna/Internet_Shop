import flask

home = flask.Blueprint(
    name = "home",
    import_name = "home_app",
    template_folder = "home_page/templates",
    static_folder = "home_page/static"
)