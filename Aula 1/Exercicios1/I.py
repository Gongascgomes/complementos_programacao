def pesoideal():
    genero = str(input("Insira o seu genero (M/F): "))
   
    
    if (genero=="m"):
        altura = float(input("Insira a sua altura em metros: "))
        pesoideal = ((72.7*altura)-58)
        
        print("O peso ideal de um homem com {} metros de altura seria de {}Kg.".format(altura, pesoideal))
    
    elif (genero=="f"):
        altura = float(input("Insira a sua altura em metros: "))
        pesoideal = ((62.1*altura)-44.7)
        
        print("O peso ideal de uma mulher com {} metros de altura seria de {}Kg.".format(altura, pesoideal))
        
    else:
        print("Error")
        
pesoideal()
