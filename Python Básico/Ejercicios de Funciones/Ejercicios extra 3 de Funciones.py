text = input("Ingrese su texto para contar vocales: ").lower()

def total_vowel(text):
    vowel = "aeiouáéíóúü"
    total = 0
    for letter in text:
        if letter in vowel:
            total +=1
    return total

print(total_vowel(text))