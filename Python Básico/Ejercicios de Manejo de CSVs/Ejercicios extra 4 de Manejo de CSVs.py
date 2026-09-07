import csv

def read_csv_file_to_list(path):
    new_list = []
    with open (path,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for n in reader:
            new_list.append(n)
    return new_list

def options_of_developers():
    developer_name = input("Ingrese su desarrollador: ").upper()
    return developer_name

def find_games_by_developer(developer_name,new_list):
    found_games = []
    print("\nJuegos encontrados: ")
    for games in new_list:
        if developer_name == games["developer"].upper():
            found_games.append(games)
    return found_games

def show_found_games(found_games):
    if found_games:    
        for new_games in found_games:
            print(f"{new_games['name']} (Clasificación: {new_games['esrb_rating']}, género: {new_games['genre']})")
    else:
        print("Lo sentimos no hay juegos de este desarrollador")
    
def main():
    new_list = read_csv_file_to_list("first_csv_file.csv")
    developer_name = options_of_developers()
    found_games = find_games_by_developer(developer_name,new_list)            
    show_found_games(found_games)
    
main()