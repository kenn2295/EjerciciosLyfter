def second_number(current_num,operator):
    while True:
        try:
            return int(input(f"{current_num} {operator} "))
        except ValueError:
            print("\n**Ingrese un valor numérico**")
    
def sum_num(current_num):
    print("\nSUMA")
    return current_num + second_number(current_num, "+")        

def rest_num(current_num):
    print("\nRESTA")
    return current_num - second_number(current_num, "-" ) 

def multi_num(current_num):
    print("\nMULTIPLICACIÓN")
    return current_num * second_number(current_num, "*" ) 

def div_num(current_num):
    print("\nDIVISIÓN")
    while True: 
        try:   
            return current_num / second_number(current_num, "/" )  
        except ZeroDivisionError:
            print("\n**No se puede dividir entre cero**")
    
def current_num():
    while True:
        try:
            number  = int(input("Ingrese el número: "))
            return number
        except ValueError:
            print(f"\n**Debes ingresar solamente valores numéricos**\n")
            

def main(current_num):
    while True:
            print(f"\nNúmero actual: {current_num}")
            print("1-SUMA") 
            print("2-RESTA")
            print("3-MULTIPLICACIÓN")
            print("4-DIVISIÓN")
            print("5-BORRAR")
            try:
                menu = int(input("Elija una operación: "))
            except ValueError:
                print("\n**Debes ingresar solamente valores numéricos**")
                continue
            if menu <= 0 or menu > 5:
                print("\n**Opción inválida**")
                continue
            if menu == 1:
                current_num = sum_num(current_num)
            elif menu == 2:
                current_num = rest_num(current_num)
            elif menu == 3:
                current_num = multi_num(current_num)
            elif menu == 4:
                current_num = div_num(current_num)
            if menu == 5:
                current_num = 0
                message = "\nResultado borrado"
            else:
                message = f"\nResultado: {current_num}"
            print(message)
            
main(current_num())