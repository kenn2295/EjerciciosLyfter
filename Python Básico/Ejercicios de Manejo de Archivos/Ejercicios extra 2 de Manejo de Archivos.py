def read_whole_file(path):
    with open(path,'r',encoding='utf-8') as file:
        content = file.read()
    return content

def count_words(lines):
    words = lines.split()
    print(f"Este archivo contiene {len(words)} palabras")
    
def main():
    lines = read_whole_file("extra2.txt")
    count_words(lines)
    
main()