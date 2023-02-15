def notasparciais():
    nota1 = float(input("Insira a primeira nota (de 0 a 20): "))
    nota2 = float(input("Insira a segunda nota (de 0 a 20): "))
    
    media = (nota1+nota2)/2
    
    if (nota1<0 and nota1>20 and nota2<0 and nota2>20):
        print("Notas inválidas.")
        
    elif (media<9.5 and media>=0):
        print("O aluno está reprovado com média de {} valores.".format(media))
    
    elif (media>=9.5 and media<19):
        print("O aluno está aprovado com média de {}.".format(media))
    
    elif (media>=19 and media<=20):
        print("O aluno está aprovado com distinção com média de {} valores.".format(media))
    
    else:
        print("Notas inválidas.")
        
notasparciais()
        