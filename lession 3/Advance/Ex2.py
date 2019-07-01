words = input()
check = []
for word in list(words):
    if word not in check:
        check.append(word)
        print(f"{word}({words.count(word)})")

