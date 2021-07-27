product_prices = {'1': 5.50, '2': 6.00, '3': 7.50, '4': 1.99, '5': 4.00, '6': 6.70, '7': 1.20, '8': 2.80, '9': 5.30, '10': 5.00, '11': 3.00, '12': 2.00, '13': 3.50, '14': 0.80, '15': 1.00, '16': 0.80, '17': 5.40, '18': 1.90, '19': 5.00, '20': 10.00, '21': 0.50, '22': 0.50, '23': 5.00, '24': 4.50, '25': 1.99, '26': 2.90, '27': 0.30}
value = 0
i = 0
qnt_proucts = input()
qnt_proucts = qnt_proucts.split(",")
while i < len(product_prices):
    value += float(qnt_proucts[i]) * float(product_prices[f"{i + 1}"])
    i += 1
doacao = float(input())
qnt_cestas = float(doacao / value)
print("O valor da cesta básica ficou em:", 'R${:.2f}'.format(value))
print(f"Com o valor doado pode ser comprada {int(qnt_cestas)} cestas básicas")