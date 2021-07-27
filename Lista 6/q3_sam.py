users_answer = "S"
fatal_accidents_country = 0
total_accidents_country = 0
no_victims_accidents = 0
total_vehicles_country = 0
total_accidents_city = 0
more_accidents = 0
less_accidents = 9999999
total_city = 0
non_fatal_accidents_country = 0
no_victims_accidents_country = 0
biggest_ivt = 0
smallest_ivt = 100000
city_less_accidents = "a"
city_more_accidents = "a"
i = 0
city_list = list()
vahicles_qnt_list = list()
fatal_accidents_list= list()
non_fatal_accidents_list = list()
no_victims_accidents_list = list()
ivt_list = list()
while users_answer != "N":
    city_name = str(input())
    city_list.append(city_name)
    vehicles_qnt = int(input())
    no_victims_accidents_list.append(vehicles_qnt)
    fatal_accidents = int(input())
    fatal_accidents_list.append(fatal_accidents)
    non_fatal_accidents = int(input())
    non_fatal_accidents_list.append(non_fatal_accidents)
    no_victims_accidents = int(input())
    no_victims_accidents_list.append(no_victims_accidents)
    total_accidents_city = fatal_accidents + non_fatal_accidents + no_victims_accidents
    fatal_accidents_country += fatal_accidents
    non_fatal_accidents_country += non_fatal_accidents
    no_victims_accidents_country += no_victims_accidents
    total_accidents_country += total_accidents_city
    total_vehicles_country += vehicles_qnt
    total_city += 1
    if total_accidents_city > more_accidents:
        more_accidents = total_accidents_city
        city_more_accidents = city_name
    if total_accidents_city < less_accidents:
        less_accidents = total_accidents_city
        city_less_accidents = city_name
    media_vehicles = total_vehicles_country/total_city
    media_fatal_accidents = fatal_accidents_country/total_city
    media_non_fatal_accidents = non_fatal_accidents_country/total_city
    media_no_victims_accidents = no_victims_accidents_country / total_city
    ivt = (5 * fatal_accidents + 3 * non_fatal_accidents + 1 * no_victims_accidents) / vehicles_qnt
    if ivt > biggest_ivt:
        city_biggest_ivt = city_name
        biggest_ivt = ivt
        city_biggest_ivt_fatal = fatal_accidents
        city_biggest_ivt_non_fatal = non_fatal_accidents
        city_biggest_ivt_no_victims = no_victims_accidents
        vehicles_biggest_ivt = vehicles_qnt
    if ivt < smallest_ivt:
        city_smallest_ivt = city_name
        smallest_ivt = ivt
        city_smallest_ivt_fatal = fatal_accidents
        city_smallest_ivt_non_fatal = non_fatal_accidents
        city_smallest_ivt_no_victims = no_victims_accidents
        vehicles_smallest_ivt = vehicles_qnt
    users_answer = str(input())
print("4.a) A quantidade de veículos no país:", total_vehicles_country)
print("4.b) A quantidade de acidentes no país:", total_accidents_country)
print("4.c) A quantidade de acidentes com vítimas fatais no país:", fatal_accidents_country)
print("4.d) O município com maior número de acidentes:", city_more_accidents, f"({more_accidents})")
print("4.d) O município com menor número de acidentes:", city_less_accidents, f"({less_accidents})\n")
print("5.a) A média de veículos por municípios:", media_vehicles)
print("5.b) A média de acidentes com vítimas fatais por municípios:", media_fatal_accidents)
print("5.b) A média de acidentes com vítimas não-fatais por municípios:", media_non_fatal_accidents)
print(f"5.b) A média de acidentes sem vítimas por municípios: {media_no_victims_accidents}\n")
print(f"5.c) O maior IVT é de {biggest_ivt} e pertence ao município {city_biggest_ivt}")
print("5.d) Nome do município:", city_biggest_ivt)
print(f"5.d) Quantidade de veículos de {city_biggest_ivt}: {vehicles_biggest_ivt}")
print(f"5.d) Total de acidentes com vítimas fatais em {city_biggest_ivt}: {city_biggest_ivt_fatal}")
print(f"5.d) Total de acidentes com vítimas não-fatais em {city_biggest_ivt}: {city_biggest_ivt_non_fatal}")
print(f"5.d) Total de acidentes sem vítimas em {city_biggest_ivt}: {city_biggest_ivt_no_victims}\n")
print(f"5.c) O menor IVT é de {smallest_ivt} e pertence ao município {city_smallest_ivt}")
print(f"5.d) Nome do município: {city_smallest_ivt}")
print(f"5.d) Quantidade de veículos de {city_smallest_ivt}: {vehicles_smallest_ivt}")
print(f"5.d) Total de acidentes com vítimas fatais em {city_smallest_ivt}: {city_smallest_ivt_fatal}")
print(f"5.d) Total de acidentes com vítimas não-fatais em {city_smallest_ivt}: {city_smallest_ivt_non_fatal}")
print(f"5.d) Total de acidentes sem vítimas em {city_smallest_ivt}: {city_smallest_ivt_no_victims}")