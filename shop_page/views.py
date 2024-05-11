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
        )
        DB.session.add(product)
    try:
        DB.session.commit()
    except:
        return "Error"
    return flask.render_template(template_name_or_list = "shop.html", products = Product.query.all())