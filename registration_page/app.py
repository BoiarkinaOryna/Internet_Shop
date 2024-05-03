import flask

registr = flask.Blueprint(
    name = "registration",
    import_name = "registration",
    template_folder = "registration_page/templates",
    static_folder = "registration_page/static",
    static_url_path = "/registration/static"
)