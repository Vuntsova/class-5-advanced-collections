from data import products_string
from step_1 import transform_products_to_list

def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    
    products_dict={}
    
    for product in products_list:
        customer_id=product[-2]
        invoice_id=product[0]
        quantity = product[3]
        price=product[-3]
        total = float(quantity)*float(price)
        
        products_dict.setdefault(customer_id, {})
        products_dict[customer_id].setdefault(invoice_id, 0)
        products_dict[customer_id][invoice_id] +=round(total, 2)
                                                              
    return products_dict

print(calculate_total_per_invoices(products_string))
        

