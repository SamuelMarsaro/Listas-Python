cars_infractions = infraction_types = ""
infractions_per_car = codes_infractions = dict()
cars_plates = list()
i = 0
while infraction_types != "*":
    infraction_types = input()
    if infraction_types != "*":
        infraction_types = infraction_types.split()
        codes_infractions[infraction_types[0]] = infraction_types[1:]

while cars_infractions != "*":
    cars_infractions = input()
    if cars_infractions != "*":
        cars_infractions = cars_infractions.split()
        cars_plates.append(cars_infractions[0])
        cars_plates.sort()
        infractions_per_car[cars_infractions[0]] = cars_infractions[1:]

while i < len(cars_plates):
    total_value = total_points = j = k = 0
    while j < len(infractions_per_car[cars_plates[i]]):
        price = float(codes_infractions[infractions_per_car[cars_plates[i]][j]][0])
        total_value += price
        j += 1
    while k < len(infractions_per_car[cars_plates[i]]):
        points = int(codes_infractions[infractions_per_car[cars_plates[i]][k]][1])
        total_points += points
        k += 1
    print(cars_plates[i], '{:.2f}'.format(total_value), total_points)
    i += 1