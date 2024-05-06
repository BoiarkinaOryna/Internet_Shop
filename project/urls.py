import home_page, registration_page, authorization_page
from .settings import shop

print("add_url_rule")
home_page.home.add_url_rule(rule = "/", view_func = home_page.show_home_page, methods = ["GET", "POST"])

registration_page.registr.add_url_rule(rule = "/registration", view_func = registration_page.show_registration_page, methods = ["GET", "POST"])

authorization_page.auth.add_url_rule(rule = "/authorization", view_func = authorization_page.show_authorization_page, methods = ["GET", "POST"])

print("register blueprint")
shop.register_blueprint(blueprint = home_page.home)

shop.register_blueprint(blueprint = registration_page.registr)

shop.register_blueprint(blueprint = authorization_page.auth)