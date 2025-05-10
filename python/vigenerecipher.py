def vigenere_encrypt(custom_word:str, custom_key: str) -> str:

    #Here we implement the alphabet to encrypt
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #here we guarantee that the custom args been lower
    lower_word = custom_word.lower()
    lower_key = custom_key.lower()
    index_key = 0
    new_word = ''

    for char in lower_word:
        
        if not char.isalpha():
            new_word += char
        else:

            char_two = lower_key[index_key % len(lower_key)]
            index_key += 1
            index = alphabet.index(char)
            sec_index = alphabet.find(char_two)
            new_index = (index + sec_index) % len(alphabet)
            new_word += alphabet[new_index]

    return f'Original word: {custom_word} and encrypted word: {new_word}'


if __name__ == '__main__':
    my_word = 'Attack at Dawn!'
    key = 'LEMON'
    print(vigenere_encrypt(my_word, key))
    print(ord('b'))