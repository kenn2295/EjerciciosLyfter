import json

def read_json_file(path):
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def create_new_pokemon(data):
    name = input("Nombre: ")
    type = input("Tipo: ")
    while True:
        try:
            level = int(input("nivel: "))
            break
        except ValueError:
            print("Ingrese un valor numérico")
    while True:
        try:  
            weight_kg = float(input("Peso(kg): "))
            break
        except ValueError:
            print("Ingrese un valor numérico")    
    is_shiny = input("¿Es shiny? (si/no): ").lower() == "si"
    held_item = input("Objeto equipado (deje vacío si no tiene): ")
    if held_item == "":
        held_item = None
    skills = []
    for i in range(4):
        skill = input(f"Ingrese la habilidad {i + 1}: ")
        skills.append(skill)
    while True:
        try:
            stats = {
            "hp": int(input("HP: ")),
            "attack": int(input("Attack: ")),
            "defense": int(input("Defense: ")),
            "sp_attack": int(input("Special Attack: ")),
            "sp_defense": int(input("Special Defense: ")),
            "speed": int(input("Speed: "))
            }
            break
        except ValueError:
            print("Solamente valores numéricos")
    new_pokemon = {
    "name": name,
    "type": type,
    "level": level,
    "weight_kg": weight_kg,
    "is_shiny": is_shiny,
    "held_item": held_item,
    "skills": skills,
    "stats": stats
    }
    data.append(new_pokemon)
    return data

def add_pokemon_to_json_file(data,file_name):
    with open(file_name,'w',encoding='utf-8') as file:
        json.dump(data,file,indent=4)

def main():
    data = read_json_file("pokemon.json")
    data = create_new_pokemon(data)
    add_pokemon_to_json_file(data,"pokemon.json")
    print("Archivo json actualizado")
    
main()