def maior_de_varios_numeros():
    lista_num = []
    
    for n in range (0, 10):
        num = int(input("Digite um número: "))
        lista_num.append(num)
        print(lista_num)
    
    maior_da_lista = max(lista_num)
    print("O maior número é o {}.".format(maior_da_lista))
        
maior_de_varios_numeros()
