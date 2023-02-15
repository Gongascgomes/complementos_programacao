def salario():
    pagamento = float(input("Insira o valor monetário que recebe por hora de trabalho: "))
    
    horas = float(input("Insira o número de horas trabalhadas por mês: "))
    
    salario = pagamento*horas
    
    print("Tendo por base o montante de {}€ pagos por hora e as {} horas trabalhadas chegamos a um valor total do salário de {}€".format(pagamento, horas, salario))
    
salario()
