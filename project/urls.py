import home_page, registration_page, authorization_page, shop_page, cart_page, contacts_page
from .settings import shop

print("add_url_rule")
home_page.home.add_url_rule(rule = "/", view_func = home_page.show_home_page, methods = ["GET", "POST"])

registration_page.registr.add_url_rule(rule = "/registration", view_func = registration_page.show_registration_page, methods = ["GET", "POST"])

authorization_page.auth.add_url_rule(rule = "/authorization", view_func = authorization_page.show_authorization_page, methods = ["GET", "POST"])

shop_page.shop.add_url_rule(rule = "/shop", view_func = shop_page.show_shop_page, methods = ["GET", "POST"])

cart_page.cart.add_url_rule(rule = "/cart", view_func = cart_page.show_cart_page, methods = ["GET", "POST"])

contacts_page.contacts.add_url_rule(rule = "/contacts", view_func = contacts_page.show_contacts_page, methods = ["POST", "GET"])

print("register blueprint")
shop.register_blueprint(blueprint = home_page.home)

shop.register_blueprint(blueprint = registration_page.registr)

shop.register_blueprint(blueprint = authorization_page.auth)

shop.register_blueprint(blueprint = shop_page.shop)

shop.register_blueprint(blueprint = cart_page.cart)

shop.register_blueprint(blueprint = contacts_page.contacts)