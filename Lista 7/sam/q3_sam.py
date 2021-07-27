word = input()
while word != "SAIR" or word != "FIM":
    word = word.replace("4", "A")
    word = word.replace("5", "S")
    word = word.replace("1", "I")
    word = word.replace("3", "E")
    word = word.upper()
    print(word)
    word = input()