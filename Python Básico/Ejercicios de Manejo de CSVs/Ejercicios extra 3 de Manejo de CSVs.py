import csv

def read_csv_file_as_dictionary(path):
    new_list = []
    with open (path,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for n in reader:
            new_list.append(n)
    return new_list

def total_of_genres(new_list):
    genre_list = {}
    for games in new_list:
        if games["genre"] in genre_list:
            genre_list[games["genre"]] +=1
        else:
            genre_list[games["genre"]] = 1
    return genre_list

def show_genre_list(genre_list):
    new_order = sorted(genre_list)
    print("Géneros encontrados:")
    for n in new_order:
        total_games = genre_list[n]
        print(f"{n}: {total_games}")

def main():
    new_list = read_csv_file_as_dictionary("first_csv_file.csv")
    genre_list = total_of_genres(new_list)
    show_genre_list(genre_list)
    
main()