import flask, os
from shop_page.models import Product
from project.settings import DB
def render_admin_page():
    if flask.request.method == "POST":
        try:
            if flask.request.form.get("del") == None:
                product = Product(
                    name = flask.request.form["name"],
                    description = flask.request.form["description"],
                    price = flask.request.form["price"],
                    discount = flask.request.form["discount"],
                    count = flask.request.form["count"]
                )
                DB.session.add(product)
                DB.session.commit()
                image = flask.request.files["image"]
                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/images/{product.name}.jpg"))
            else:
                product_id = int(flask.request.form["del"])
                product_del = Product.query.get(product_id)
                if Product.query.get(product_id):
                    DB.session.delete(product_del)
                    DB.session.commit()
                    os.remove(os.path.abspath(__file__ + f"/../../shop_page/static/images/{product_del.name}.jpg"))
        except Exception as e:
            print(e)
        
    return flask.render_template(template_name_or_list = "admin.html", products = Product.query.all())