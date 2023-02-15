def nota_entre_0_10():
    while True:
        num =  int(input("digite uma nota (0--10): "))
        if (num<=10 and num>=0):
            break

nota_entre_0_10()
