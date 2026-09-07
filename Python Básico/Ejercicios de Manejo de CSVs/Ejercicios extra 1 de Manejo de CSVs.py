import csv

def read_csv_file_by_lines(path):
    with open(path,'r',encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

def show_games_list(reader):    
    keys = reader[0]
    for values in reader[1:]:
        for i in range(len(keys)):
            print(f"{keys[i]}: {values[i]}")
        print()
        
def main():                        
    reader = read_csv_file_by_lines("first_csv_file.csv")
    show_games_list(reader)

main()