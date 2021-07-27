data = ""
dict_lists_consumption = dict()
start_point = 0
names = list()
past_post = ""
while data != "FIM":
    data = input()
    if data != "FIM":
        data = data.split()
        if data[2] not in names:
            names.append(data[2])
        if start_point != 0:
            distance = float(data[0]) - float(start_point)
            consumption = float(data[1])
            consumption_media = distance/consumption
            if past_post not in dict_lists_consumption:
                dict_lists_consumption[past_post] = [float(consumption_media)]
            else:
                dict_lists_consumption[past_post].append(float(consumption_media))
        start_point = data[0]
        past_post = data[2]
i = 0
names.sort()

while i < len(names):
    total_media = sum(dict_lists_consumption[names[i]]) / len(dict_lists_consumption[names[i]])
    print(f"{names[i]}: {'{:.2f}'.format(total_media)}")
    i += 1