lado = float(input("Insira a medida do lado do quadrado: "))

def areaquadrado():
    area = lado**2
    
    print("A área do quadrado de lado {} é de {} unidades.".format(lado, area))
    
def perimetroquadrado():
    perimetro = lado*4
    
    print("O perímetro do quadrado de lado {} é de {} unidades.".format(lado, perimetro))
    

areaquadrado()

perimetroquadrado()
