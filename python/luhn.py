valid_number = "4539578763621486"
not_valid_number = "4539548763621486"

def luhn(number_client: int) -> str:

    reversed_lst = list(reversed(number_client))
    list_multiply = []
    
    list_not_modified = []

    for i in range(1, len(number_client), 2):
        list_multiply.append(int(reversed_lst[i]) * 2)
        new_nine = [ i - 9 if i > 9 else i for i in list_multiply]
    
    for j in range(0, len(number_client), 2):
        list_not_modified.append(reversed_lst[j])

    list_integers_one = list(map(int, list_not_modified))
    list_integers_two = list(map(int, new_nine))

    total_sum = sum(list_integers_one) + sum(list_integers_two)

    return f'Your number is valid for a card' if total_sum % 10 == 0 else f'Your number is not valid'

    
print(luhn(valid_number))
print(luhn(not_valid_number))