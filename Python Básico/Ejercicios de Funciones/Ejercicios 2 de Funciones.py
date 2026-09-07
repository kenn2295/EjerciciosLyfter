def my_local():
    name = 'Kenneth'
#No se puede acceder porque su alcance es local dentro de la función
#print(name)
name = 'Andres'
def my_global():
    global name
    name = 'Kenneth'
    print(name)
    
my_global()
# aquí se imprime la variable global ya modificada
print(name) 