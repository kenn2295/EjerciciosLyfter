import json

def read_json_file(path):
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def select_type(data):
    while True:
        print("Types:")
        print("Normal | Fire | Water | Electric | Grass | Ice")
        print("Fighting | Poison | Ground | Flying | Psychic | Bug")
        print("Rock | Ghost | Dragon | Dark | Steel | Fairy")
        my_type = input("Select the type: ").capitalize()
        for pokemon in data:
            if my_type == pokemon['type']:
                return my_type
        print("\nInvalid Selection. Try again")

def show_pokemon_type(my_type,data):
    print("\nThe Pokemon of this type are: ")
    for pokemon in data:
        if my_type == pokemon['type']:
            print(pokemon['name'])

def main():
    data = read_json_file("pokemon.json")
    my_type = select_type(data)
    show_pokemon_type(my_type,data)
    
main()