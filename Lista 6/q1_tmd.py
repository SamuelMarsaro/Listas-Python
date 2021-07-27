not_allowed = dict()
num = int(input())
bad_words_list = list()
for i in range(0, num):
    line = input().upper().split()
    bad_words = line[0]
    peso = float(line[1])
    if '.' in bad_words:
        bad_words = bad_words.replace('.', '')
    if ',' in bad_words:
        bad_words = bad_words.replace(',', '')
    bad_words_list.append(bad_words)

threshold = int(input())

text = input().upper()
if '.' in text:
    text = text.replace('.', '')
if ',' in text:
    text = text.replace(',', '')
text = text.split()

for w in text:
    if w not in not_allowed:
        not_allowed[w] = 1
    else:
        not_allowed[w] += 1


total = 0
for i in bad_words_list:
    result = not_allowed.get(i, None)
    if result is not None:
        total += result * peso

if total > threshold:
    message = 'SIM'
else:
    message = 'NAO'


for i in bad_words_list:
    result = not_allowed.get(i, None)
    if result is not None:
        if i in not_allowed:
            print(i, result)

print(message)