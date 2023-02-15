def vogalouconsuante():
    vogais = ["a", "e", "i", "o", "u"]
    letra = str(input("Insira uma letra: "))
    
    if (letra in vogais):
        print("A letra '{}' é uma vogal.".format(letra))
    else:
        print("A letra '{}' é uma consuante.".format(letra))
        
vogalouconsuante()
    