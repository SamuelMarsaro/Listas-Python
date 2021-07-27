qnt_products = int(input())
i = 0
products = dict()
while i < qnt_products:
    code_product = float(input())
    name_product = input()
    price_product = float(input())
    products[code_product] = price_product
    i += 1
client_code = float(1)
final_price = 0
while client_code != 0.0:
    client_code = float(input())
    if client_code != 0.0:
        qnt_client = float(input())
        if client_code in products and qnt_client > 0.0:
            final_price += products[client_code] * qnt_client
print('{:.2f}'.format(final_price))