text_var = 'Hello Zorld'

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