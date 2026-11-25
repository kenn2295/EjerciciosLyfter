from datetime import datetime

class Camera:
    
    def take_photo(self):
        return "taking a picture"

class GPS:
    def location(self):
        return "current location: Costa Rica"

class Time:
    def timeline(self):
        return datetime.now().strftime("%a %d-%m-%Y at %H:%M")

class SmartPhone(Camera,GPS,Time):
    pass
    
my_phone = SmartPhone()

print(my_phone.take_photo())
print(my_phone.location())
print(my_phone.timeline())
# La herencia múltiple permite que una clase herede atributos y métodos de dos o más clases padre,
# combinando sus funcionalidades y permitiendo reutilizar código sin volver a definir los mismos en la clase hija.