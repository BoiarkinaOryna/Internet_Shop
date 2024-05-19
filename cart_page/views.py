import flask
from shop_page.models import Product
def show_cart_page():
    if flask.request.cookies:
        print(flask.request.cookies.get("product").split(" "))
        products = flask.request.cookies.get("product").split(" ")
        list_products = []
        repeat_id = []
        products_quantity = {}
        for id_product in products:
            print("products =", products)
            count_products = products.count(id_product)
            if id_product not in repeat_id:
                print("list_products = ", list_products)
                print("Product.query.get(id_product) =", Product.query.get(id_product))
                list_products.append(Product.query.get(id_product))
                repeat_id.append(id_product)
                print("Product.query.get(id_product)).split(';')[0].split('- ')", str(Product.query.get(id_product)).split(";")[0].split("- "))
                chosen_element = str(Product.query.get(id_product)).split(";")[0].split("- ")[1]
                print("chosen_element =", chosen_element)
                # print("products_quantity[chosen_element] =", products_quantity[chosen_element])
                try:
                    products_quantity[chosen_element] += 1
                except:
                    products_quantity[chosen_element] = 1
                print("products_quantity =", products_quantity)
                print("list_products[-1] = ", list_products[-1])
                if list_products[-1].count <= count_products:
                    list_products[-1].count = count_products
        # for element in products:
        #     # products_quantity[element] = element
        #     products_quantity.append(Product.query.get(element))
        #     # print("products_quantity[element] =", products_quantity[element])
        #     print("products_quantity =", products_quantity)
        return flask.render_template(template_name_or_list = "cart.html", products = list_products, quantity = products_quantity)
    else:    
        return flask.render_template(template_name_or_list = "cart.html")