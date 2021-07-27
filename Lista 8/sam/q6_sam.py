product_and_price = ""
products_and_prices = dict()
products = list()
while product_and_price != "*":
    product_and_price = input()
    if product_and_price != "*":
        product_and_price = product_and_price.split()
        products.append(" ".join(product_and_price[:-1]))
        products_and_prices[" ".join(product_and_price[:-1])] = float(product_and_price[-1])
i = 0
answer = ""
total_price = 0
while answer != "total":
    answer = input()
    if " " in answer:
        answer = answer.split()
    if answer[0] == "retire":
        del products_and_prices[" ".join(answer[1:])]
        products.remove(" ".join(answer[1:]))
    if answer == "quantidade":
        print(len(products_and_prices))
    if answer == "total":
        while i < len(products_and_prices):
            total_price += products_and_prices[products[i]]
            i += 1
        print('{:.2f}'.format(total_price))