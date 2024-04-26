import home_page, registration_page

home_page.home.add_url_rule(rule = "/", view_func = home_page.show_home_page)

# home_page.home.add_url_rule(rule = "/", view_func = registration_page.show_registration_page)