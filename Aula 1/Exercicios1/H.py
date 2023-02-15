def conversaofarenheit():
    farenheit = float(input("Indique o valor que pretende converter de ºF para Cº: "))
    
    celsius = (5*(farenheit-39)/9)
    
    print("O valor de {}F convertido para C vai ser de {} graus celsius.".format(farenheit, celsius))
    
conversaofarenheit()
