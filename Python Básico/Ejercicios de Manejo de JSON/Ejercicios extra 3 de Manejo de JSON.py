import json

def read_json_file(path):
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def show_pokemon_stats(data):
    print("statistics: ")
    for pokemon in data:
        print(f"Name: {pokemon['name']}")
        print(f"attack: {pokemon['stats']['attack']}")
        print(f"defense: {pokemon['stats']['defense']}")
        print(f"speed: {pokemon['stats']['speed']}")
        print()

def main():
    data = read_json_file("pokemon.json")
    show_pokemon_stats(data)
    
main()