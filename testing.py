def palindome(sentence):
    for i in (",.?'/><}{{}}'"):
        sentence = sentence.replace(i, "")
    palindome = []
    words = sentence.split(' ')
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            palindome.append(word)
    return palindome
sentence = input('Enter a sentence : ')
print(palindome(sentence))
