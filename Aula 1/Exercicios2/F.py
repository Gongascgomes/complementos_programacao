def maiordetres():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    num3 = int(input("Insira o terceiro número: "))
    
    if (num1>num2 and num1>num3):
        print("O maior número de entre os três números é o número {}.".format(num1))
    
    elif (num2>num1 and num2>num3):
        print("O maior número de entre os três números é o número {}.".format(num2))
        
    elif (num3>num1 and num3>num2):
        print("O maior número de entre os três números é o nùmero {}.".format(num3))
    
    else:
        print("Error.")    
        
maiordetres()
