def read_file_by_lines(path):
    with open(path,'r',encoding='utf-8') as file:
        content = file.readlines()
        return content

def clean_lines(lines):
    new_lines = []  
    for line in lines:
        clear_words = line.strip()
        new_lines.append(clear_words)
    return new_lines

def create_single_line(new_lines):
    new_string = " ".join(new_lines)
    return new_string

def create_new_file(file_name,new_string):
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(new_string)
    
    
def main():
    file_name = "extra1_result.txt"
    lines = read_file_by_lines("extra1.txt")
    new_lines = clean_lines(lines)
    new_string = create_single_line(new_lines)
    create_new_file(file_name,new_string)  
    print("Archivo creado correctamente")
    
main()