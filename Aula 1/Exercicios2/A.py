def numeromaior():
    num1 = int(input("Insira o primeiro número: "))
    
    num2 = int(input("Insira o segundo número: "))
    
    if (num1>num2):
        print("O número {} é maior que o número {}.".format(num1, num2))
        
    else:
        print("O número {} é maior que o número {}.".format(num2, num1))
        
numeromaior()
