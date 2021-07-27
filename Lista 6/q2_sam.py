sandwiches=int(input())
CHEESE_WEIGHT = 50
HAM_WEIGHT = 50
HAMBURGUER_WEIGHT = 100
cheese_to_buy = sandwiches*2*CHEESE_WEIGHT/1000
ham_to_buy = sandwiches*HAM_WEIGHT/1000
meat_to_buy = sandwiches*HAMBURGUER_WEIGHT/1000
print(cheese_to_buy, "kg de queijo")
print(ham_to_buy, "kg de presunto")
print(meat_to_buy, "kg de carne")