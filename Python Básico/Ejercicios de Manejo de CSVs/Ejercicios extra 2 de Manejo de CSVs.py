import csv

def read_csv_file_by_lines(path):
    with open(path,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)
                        
def select_a_category(reader):
    while True:
        esrb_rating = input("Seleccione una clasificación ESRB (M, E10+, E, T): ").upper()
        for values in reader[1:]:
            if esrb_rating == values[3]: 
                return esrb_rating
        print("Clasificación incorrecta***\n")
        
def valid_category(reader,esrb_rating): 
    games_list = []      
    print("\nJuegos Disponibles: ")
    for values in reader[1:]:
        if values[3] == esrb_rating:
            games_list.append(values[0])
    return games_list

def show_games(games_list):
    for games in games_list:
        print(games)
            
def main():
    reader = read_csv_file_by_lines("first_csv_file.csv")
    esrb_rating = select_a_category(reader)
    games_list = valid_category(reader,esrb_rating)
    show_games(games_list)
    
main()