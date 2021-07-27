stock_code = ""
stocks = dict()
history_values = dict()
while stock_code != "fim":
    stock_code = input()
    if stock_code != "fim":
        stock_definition = input()
        stock_price = float(input())
        stock_qnt = int(input())
        stocks[stock_code] = [stock_definition, stock_price, stock_qnt]
        history_values[stock_code] = [stock_price]

code_stock = ""
last_code = dict()
while code_stock != "fim":
    code_stock = input()
    if code_stock != "fim":
        code_price = float(input())
        history_values[code_stock].append(code_price)
        media_price = sum(history_values[code_stock][-10:])/len(history_values[code_stock][-10:])
        if code_price > media_price or code_price > stocks[code_stock][1]:
            print("Venda")
        else:
            print("Compra")
        stocks[code_stock][1] = code_price