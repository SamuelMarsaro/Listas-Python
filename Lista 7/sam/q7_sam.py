name = ""
CONNECTIVES = ['da', 'de', 'di', 'do', 'du', 'e']
while name != "*":
    name = input()
    if name != "*":
        name = name.title()
        list_name = name.split()
        for CONNECTIVES in list_name:
            if 'Da' in list_name:
                j = list_name.index('Da')
                list_name[j] = 'da'
            if 'De' in list_name:
                j = list_name.index('De')
                list_name[j] = 'de'
            if 'Di' in list_name:
                j = list_name.index('Di')
                list_name[j] = 'di'
            if 'Do' in list_name:
                j = list_name.index('Do')
                list_name[j] = 'do'
            if 'Du' in list_name:
                j = list_name.index('Du')
                list_name[j] = 'du'
            if 'E' in list_name:
                j = list_name.index('E')
                list_name[j] = 'e'
        title = " ".join(list_name)
        print(title)