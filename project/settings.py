import flask 
import home_page
import registration_page

shop = flask.Flask(
    import_name = "settings",
    template_folder = "project/templates"
)

shop.register_blueprint(blueprint = home_page.home)

shop.register_blueprint(blueprint = registration_page.registr)