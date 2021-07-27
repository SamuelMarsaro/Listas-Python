email = input()
while email != "sair":
    check_a = email.split("@")
    if len(check_a) == 2 and "" not in check_a:
        check_points = check_a[1].split(".")
        if len(check_points) == 3 and "" not in check_points:
            print("certo")
        else:
            print("errado")
    else:
        print("errado")
    email = input()