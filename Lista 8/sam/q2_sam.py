name_qnt = input()
qnt_per_name = dict()
while name_qnt != "*":
    name_qnt = name_qnt.split(",")
    qnt_per_name[name_qnt[0]] = name_qnt[1]
    name_qnt = input()

qnt_pacient = 1
i = 0
total_c_client = 0
while qnt_pacient != 0:
    qnt_pacient = int(input())
    if qnt_pacient != 0:
        while i < qnt_pacient:
            qnt_name_client = input()
            qnt_name_client = qnt_name_client.split()
            if len(qnt_name_client) > 2:
                x = qnt_name_client[0]
                qnt_name_client.remove(x)
                name_product = " ".join(qnt_name_client)
                qnt_name_client = [x, name_product]
            total_c = int(int(qnt_name_client[0]) * int(qnt_per_name[qnt_name_client[1]]))
            total_c_client += total_c
            i = i + 1
        if total_c_client > 130:
            print(f"Menos {total_c_client - 130} mg")
        if 110 <= total_c_client <= 130:
            print(f"{total_c_client} mg")
        if total_c_client < 110:
            print(f"Mais {110 - total_c_client} mg")
        total_c_client = 0
        i = 0