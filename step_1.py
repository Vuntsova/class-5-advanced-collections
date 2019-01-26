# The first step is to parse the raw string into a list containing products (as lists). It'll end up being a nested collections (a list of lists).

from data import products_string

def transform_products_to_list(products_string):
    
    products_list = []
    products_string = products_string.split("\n")
    for product in products_string:
        if len(product) > 0:
            product = product.split(",")
            products_list.append(product)
    return products_list
