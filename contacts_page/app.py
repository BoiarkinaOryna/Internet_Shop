import flask

contacts = flask.Blueprint(
    name = "contacts",
    import_name = "app",
    static_folder = "contacts_page/static",
    template_folder = "contacts_page/templates",
    static_url_path = "/contacts_page/static"
)