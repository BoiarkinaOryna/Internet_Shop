import flask

basket = flask.Blueprint(
    name = "basket",
    import_name = "basket_page",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/static"
)