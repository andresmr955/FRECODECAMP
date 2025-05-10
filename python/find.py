alphabet = 'abcdefghijklmnopqrstuvwxyz'
text = 'Hello World'
text[0] = 'P'
shift = 3

print(alphabet.find('z'))

print(alphabet.find(text[0]))
index = alphabet.find(text[0].lower())
shifted = alphabet[index]
print(shifted)
