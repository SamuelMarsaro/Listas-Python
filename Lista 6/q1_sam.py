dead_kids = int(input())
i = 0
male_kids = 0
feminine_kids = 0
short_life = 0
percent_feminine = 0
percent_male = 0
percent_short_life = 0
if dead_kids > 0:
    while i < dead_kids:
        i += 1
        sex = input()
        if sex == 'M':
            male_kids += 1
        else:
            feminine_kids += 1
        lifetime = int(input())
        if lifetime <= 24:
            short_life += 1
    percent_feminine = (feminine_kids / dead_kids) * 100
    percent_male = (male_kids / dead_kids) * 100
    percent_short_life = (short_life / dead_kids) * 100
    print(f'a) {percent_feminine}% das crianças eram do sexo feminino.')
    print(f'b) {percent_male}% das crianças eram do sexo masculino.')
    print(f'c) {percent_short_life}% das crianças viveram 24 meses ou menos.')
else:
    print('Informe um número positivo')