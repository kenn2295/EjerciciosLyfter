def first_print(second_print):
    phrase_1 = 'Desde aca se llama a la segunda función:'
    
    print(phrase_1)
    second_print()
    
def second_print():
    phrase_2 = 'Si ves este texto es porque me llaman desde la primer función correctamente'
    
    print(phrase_2)

first_print(second_print)
