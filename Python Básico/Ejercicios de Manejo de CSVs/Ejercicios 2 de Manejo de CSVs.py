import csv

def create_dictionary():
    games = []
    amount = int(input("Cuantos diccionarios desea ingresar: "))
    for video_games in range(amount):
        name = input("Ingrese el nombre: ")
        genre = input("Ingrese la género: ")
        developer = (input("Ingrese el desarrollador: "))
        esrb_rating = input("Ingrese la clasificación ESRB: ")
        video_games = {
            "name" : name,
            "genre": genre,
            "developer": developer,
            "esrb_rating": esrb_rating
        }
        games.append(video_games)
    return games
        
def create_CSV_file(file_name,games): 
    with open(file_name,'w',encoding='utf-8',newline='') as file:
        headers = games[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers,dialect = "excel-tab")
        writer.writeheader()
        writer.writerows(games)
        
def main():
    file_name = "second_csv_file.csv"
    games = create_dictionary()
    create_CSV_file(file_name,games)
    print("Archivo CVS creado correctamente")
    
main()

#Se utiliza dialect="excel-tab" para indicarle al DictWriter que separe los campos del archivo con TAB.
#También se puede utilizar delimiter para asignarle el separador deseado manualmente, por ejemplo "\t".
# La diferencia es que uno ya está predeterminado y en el segundo asignamos TAB manualmente.