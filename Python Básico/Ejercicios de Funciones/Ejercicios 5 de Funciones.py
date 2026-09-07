my_text = input('Ingrese su texto: ')

def count_upper_and_lower(my_text):
    upper_count = 0
    lower_count = 0
    for letter in my_text:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
    return upper_count, lower_count

upper, lower = count_upper_and_lower(my_text)

print(f"There's {upper} upper cases and {lower} lower cases")