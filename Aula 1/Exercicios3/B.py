def user_password():
    while True:
        user = str(input("Insira o seu nome de utilizador: "))
        password = str(input("Insira a sua password: "))
        if (user==password):
            print("erro")
        else:
            print("Seja bem-vindo {}!".format(user))
            break
        
user_password()   
    