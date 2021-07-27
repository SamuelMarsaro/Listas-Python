number = int(input())
lines = (number + 1)
phrases = list()
while lines > 1:
    phrases.append(input())
    lines = lines - 1

letters_phrases = "".join(phrases)
letters_phrases_list = list(letters_phrases)

letters_to_search = str(input())
letters_to_search_list = list(letters_to_search)

i = 0
while i < len(letters_to_search_list):
    print(letters_to_search_list[i], "=", letters_phrases_list.count(letters_to_search_list[i]))
    i = i + 1