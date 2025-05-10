def encrypted(custom_word, key):
    u_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    key_index = 0
    new_word = ''

    for char in custom_word:
        if char.isalpha():
            base_alphabet = u_alphabet if char.isupper() else l_alphabet
            fst_index = base_alphabet.index(char)
            sec_char = key[key_index % len(key)]  
            base_alphabet_key = u_alphabet if sec_char.isupper() else l_alphabet
            sec_index = base_alphabet_key.index(sec_char)
            new_word += base_alphabet[(fst_index + sec_index) % len(base_alphabet)]
            key_index += 1
        else:
            new_word += char

    return new_word


def dencrypted(custom_word, key):
    u_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    key_index = 0
    new_word = ''

    for char in custom_word:
        if char.isalpha():
            base_alphabet = u_alphabet if char.isupper() else l_alphabet
            fst_index = base_alphabet.index(char)
            sec_char = key[key_index % len(key)]  
            base_alphabet_key = u_alphabet if sec_char.isupper() else l_alphabet
            sec_index = base_alphabet_key.index(sec_char)
            new_word += base_alphabet[(fst_index - sec_index) % len(base_alphabet)]
            key_index += 1
        else:
            new_word += char

    return new_word

if __name__ == '__main__':
    encrypted = encrypted(input("Your word: -> "), input("your key: -> "))
    dencrypted = dencrypted(input("Your word: -> "), input("your key: -> "))
    print("Encrypted: ", encrypted)
    print('Dencrypted: ', dencrypted)
