dict = {"cat": "chat", "dog": "chien"}
words = ["dog", "horse"]
for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, " not in dict")