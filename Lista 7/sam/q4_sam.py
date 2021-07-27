phrase = input()
phrase = phrase.lower()
phrase = phrase.replace("!", "")
phrase = phrase.replace(",", "")
phrase = phrase.replace(".", "")
phrase = phrase.replace("?", "")

phrase2 = input()
phrase2 = phrase2.lower()
phrase2 = phrase2.replace("!", "")
phrase2 = phrase2.replace(",", "")
phrase2 = phrase2.replace(".", "")
phrase2 = phrase2.replace("?", "")

# a, b, c, d, e, f, g and h are variables just to convert the phrase into a letter-by-letter on alphabetical order list
a = phrase.split(" ")
b = "".join(a)
c = list(b)
d = sorted(c)

e = phrase2.split(" ")
f = "".join(e)
g = list(f)
h = sorted(g)

print(bool(d == h))