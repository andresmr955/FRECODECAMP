alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_var = 'Hello Zorld'
text_var[0] = 'P'
shift = 3

print(alphabet.find('z'))

print(alphabet.find(text_var[0]))
index = alphabet.find(text_var[0].lower())
shifted = alphabet[index]
print(shifted)
