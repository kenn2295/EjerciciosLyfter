import json

def read_json_file(path):
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def show_pokemon_details(data):
    print("List of Pokemons: ")
    for pokemon in data:
        print(f"Name: {pokemon['name']}")
        print(f"Type: {pokemon['type']}")
        print(f"Level: {pokemon['level']}")
        print(f"Skills: {pokemon['skills']}")
        print()

def main():
    data = read_json_file("pokemon.json")
    show_pokemon_details(data)
    
main()