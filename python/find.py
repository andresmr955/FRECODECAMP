# alphabet = 'abcdefghijklmnopqrstuvwxyz'
text_var = 'Hello Zorld'
# text[0] = 'P'
# shift = 3

# print(alphabet.find('z'))

# print(alphabet.find(text[0]))
# index = alphabet.find(text[0].lower())
# shifted = alphabet[index]
# print(shifted)

def caesar(text: str, offset: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_encrypted = ''

    for char in text.lower():
        if char == ' ':
            new_encrypted += " "
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            new_encrypted += alphabet[new_index]
            
    print(text)
    print(new_encrypted)

caesar(text_var, 3)