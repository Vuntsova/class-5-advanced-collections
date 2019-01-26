from data import products_string
from step_1 import transform_products_to_list


def group_products_by_customer(products_string):
    products_list = transform_products_to_list(products_string)
    products_dict = {}
    for product in products_list:
        customer_id = product[-2]
        products_dict.setdefault(customer_id, [])
        products_dict[customer_id].append(product)
            
    
    return products_dict

print(group_products_by_customer(products_string))
