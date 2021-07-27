words_counts = dict()
words_to_search = input()
words_to_search = words_to_search.upper()
words_to_search = words_to_search.split()
words_to_search = sorted(words_to_search)
y = ""
text = ""
while text != "FIM":
    text = input()
    if text != "FIM":
        text = text.upper()
        text = text.replace(",", " ")
        text = text.replace(".", " ")
        y += " " + text
        words_list = y.split(" ")

i = 0
while i < len(words_list):
    if words_list[i] not in words_counts:
        words_counts[words_list[i]] = 1
    else:
        words_counts[words_list[i]] += 1
    i += 1

i = 0
while i < len(words_to_search):
    if words_to_search[i] in words_counts:
        print(words_to_search[i], words_counts[words_to_search[i]])
    i += 1