import flask, pandas, os
from project.settings import DB
from .models import Product
def show_shop_page():
    path_xlsx = os.path.abspath(__file__  + "/../phones_flask_project.xlsx")

    read_xlsx = pandas.read_excel(
        io = path_xlsx,
        # header = None,
        names = ["name", "price", "description", "count", "image"]
    )
    
    for row in read_xlsx.iterrows():
        row_data = row[1]
        print("read_xlsx.iterrows() :", read_xlsx.iterrows())
        print("row_data = ", row_data)
        product = Product(
            name = row_data['name'],
            price = row_data['price'],
            description = row_data['description'],
            count = row_data['count'],
            image = row_data['image']
        )
        DB.session.add(product)
    # try:
    DB.session.commit()
    # except (OperationalError):
    #     return "ERROR"

    return flask.render_template(template_name_or_list = "shop.html", product = Product.query.all())

    