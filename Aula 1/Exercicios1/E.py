import math

def areacircunferencia():
    raio = float(input("Indique o valor do raio da circunferência: "))
    
    area = (raio**2)*math.pi
    
    print("A área da circunferência de raio {} é de {} unidades de área.".format(raio, area))
    
areacircunferencia()
