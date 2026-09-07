def order_words(words):
    my_list = words.split('-')
    my_list.sort()
    result = '-'.join(my_list)
    return result

words = input('Ingrese sus palabras: ')    
print(order_words(words))