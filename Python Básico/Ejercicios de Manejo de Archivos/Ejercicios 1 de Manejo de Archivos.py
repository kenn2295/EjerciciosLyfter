def read_file_by_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return lines
            
def sort_songs(lines):
    new_order = sorted(lines)
    return new_order

def create_new_file(new_order):
    file_name = "new_order.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        for song in new_order:
            file.write(song)
    print(f"\nArchivo creado correctamente: {file_name}")
    
def main():
    lines = read_file_by_lines("song.txt")
    new_order = sort_songs(lines)
    print("\nSORTED LIST:")
    for number, song in enumerate(new_order, start=1):
        print(f"Line {number}: {song.strip()}")
        
    create_new_file(new_order)

main()