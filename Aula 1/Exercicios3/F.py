def soma_media_numeros():
    lista_nums = []
    n = int(input("Digite a quantidade de números que pretende: "))
    for n in range (0, n):
        num = int(input("Digite os números que pretende: "))
        lista_nums.append(num)
        print(lista_nums)
        
    soma_lista = sum(lista_nums)
    
    media_lista = soma_lista/n
    
    print("A soma dos números que inseriu é {}.".format(soma_lista))
    print("A media dos números inseridos é {}.".format(media_lista)) 
    
soma_media_numeros()
    