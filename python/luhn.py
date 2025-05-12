valid_number = "4539578763621486"
not_valid_number = "4539548763621486"
reveris = valid_number[-1: - len(valid_number): -2]
print(list(reversed(valid_number)))
print(reveris)

def translate_number(original_number):
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_number = original_number.translate(card_translation)
    return translated_number

def luhn(number_client: str) -> str:
    card_numbers_mutated = translate_number(number_client)
    reversed_lst = list(reversed(card_numbers_mutated))

    new_nine = list(map(lambda x: x - 9 if x > 9 else x, map(lambda i: int(reversed_lst[i]) * 2, range(1, len(reversed_lst), 2))))

    list_integers_one = list(map(lambda i: int(reversed_lst[i]), range(0, len(reversed_lst), 2)))

    total_sum = sum(list_integers_one) + sum(new_nine)

    return f'Your number is valid for a card' if total_sum % 10 == 0 else f'Your number is not valid'
    
print(luhn(valid_number))
print(luhn(not_valid_number))
print(luhn('4111-1111-4555-1142'))