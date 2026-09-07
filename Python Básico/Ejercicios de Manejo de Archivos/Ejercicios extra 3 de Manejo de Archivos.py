def read_file_by_lines(path):
    with open(path,'r',encoding='utf-8') as file:
        content = file.readlines()
    return content

def convert_to_uppercase(lines):
    new_file = []
    for line in lines:
        new_line = line.upper()
        new_file.append(new_line)
    return new_file

def create_new_file(file_name, new_file):
    try:
        with open(file_name, 'x', encoding='utf-8') as file:
            for line in new_file:
                file.write(line)
            print("Archivo creado correctamente")
            
    except FileExistsError:
        print("Archivo existente")
    
def main():
    file_name = "mama22dddd3.txt"
    lines = read_file_by_lines("archivo_original.txt")
    new_file = convert_to_uppercase(lines)
    create_new_file(file_name,new_file)
        

main()