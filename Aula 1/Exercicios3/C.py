 #Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
#uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
#de anos necessários para que a população do país A ultrapasse ou iguale a população do
#país B, mantidas as taxas de crescimento.

def paisA_paisB():
    pais_a = 80000
    pais_b = 200000
    anos = 0
    while True:
        habitantes_a = pais_a+0.03
        pais_a += (habitantes_a-pais_a)
        habitantes_b = pais_b+0.015
        pais_b += (habitantes_b-pais_b)
        anos += 1
        print("No ano {} o pais A tem {} habitantes e o pais B tem {} habitantes.".format(anos, habitantes_a, habitantes_b))
        if (pais_a==pais_b):
            break
        
paisA_paisB()

