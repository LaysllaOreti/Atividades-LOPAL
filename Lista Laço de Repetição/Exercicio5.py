tentativas = 3
senha = str(input("Digite a sua senha: "))

while True:
    confirmar = str(input("Confirme a sua senha: "))
    
    if senha == confirmar:
        print("Senha correta!")
    
    else:
        tentativas -= 1
        print(f"Você possui mais {tentativas} tentativa(s). Tenet novamente")
        
    if tentativas == 0:
        print("Suas tentativas acabaram!")
        break