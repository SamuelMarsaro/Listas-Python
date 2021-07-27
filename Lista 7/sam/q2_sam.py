genetic_map = input()
base = input()
list_order = []
first = genetic_map[0]
i = 0
biggest_sequence = -1
big_sequence = 0
if base in genetic_map:
    # Finding the position and the lenght of the biggest base sequence
    for character in genetic_map[1:]:
        if character == first[-1]:
            first += character
        else:
            list_order.append(first)
            first = character
    list_order.append(first)
    while i < len(list_order):
        if base in list_order[i]:
            x = len(list_order[i])
            if x > biggest_sequence:
                biggest_sequence = x
                big_sequence = list_order[i]
        i = i + 1
    position_biggest_sequence = genetic_map.find(big_sequence)
    print(position_biggest_sequence)
    print(biggest_sequence)
else:
    print("ERRO")
