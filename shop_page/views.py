import flask, pandas, os
from project.settings import DB
from .models import Product
def show_shop_page():
    path_xlsx = os.path.abspath(__file__  + "/../phones_flask_project.xlsx")

    read_xlsx = pandas.read_excel(
        io = path_xlsx,
        header = None,
        names = ["name", "price", "description", "count"]
    )   
        

    for row in read_xlsx.iterrows():
        data = row[1]
        product = Product(
            name = data["name"],
            price = data["price"],
            description = data["description"],
            count = data["count"]
            # image = data["image"]      
        )
        # print("            1:", DB.session.query(Product).filter_by(name = product.name), "\n", "                    2:", DB.session.query(Product))
        # if not DB.session.query(Product).filter_by(name = data["name"]):
        DB.session.add(product)
    try:
        DB.session.commit()
    except:
        return "Error"
    return flask.render_template(template_name_or_list = "shop.html", products = Product.query.all())