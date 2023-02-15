def   generoletra():
    letra = str(input("Insira a letra que corresponde ao ser género: "))
    
    if (letra=="m"):
        print("O seu género é o género masculino.")
    elif (letra=="f"):
        print("O seu género é o género feminino.")
    else:
        print("Género inválido.")
        
generoletra()
