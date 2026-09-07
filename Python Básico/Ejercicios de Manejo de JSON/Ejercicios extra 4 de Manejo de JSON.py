import json

def read_json_file(path):
    with open(path,'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def pokemon_group(data):
    new_list = {}
    for pokemon in data:
        key = pokemon["type"]
        value = pokemon["level"]
        if key in new_list:
            new_list[key].append(value)
        else:
            new_list[key] = [value]
    return new_list

def get_average(new_list):
    for types in new_list:
        average = sum(new_list[types]) / len(new_list[types])
        print(f"Type: {types} → Average level: {average:.2f}")
                    
def main():
    data = read_json_file("pokemon.json")
    new_list = pokemon_group(data)
    get_average(new_list)
    
main()