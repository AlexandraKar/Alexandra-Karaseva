a = []
word = input('enter a word:')
while word:
    a.append(word)
    word = input('enter a word:')
for w in a:
    if len(str(w)) > 5:
        print(w)
