contador = 0 #inicializa o contador atribuindo valor 0

while True:   #enquanto for verdade
    senha = input("Digite a senha: ")
    contador += 1  #contar quantas vezes a pessoa tentou acertar a senha
    if senha == '091408':   #se a pessoa inserir essa senha
        break               #o looping irá parar
    else:
        print("Senha incorreta! Tente novamente")

if contador == 1: #se a pessoa acertou de primeira
    print("Correto! Você levou apenas uma tentativa! ") #irá exibir isso
else:      #se não acertar de primeira
    print("Correto! Você levou {} tentativas".format(contador))  #exibirá a quantidade de vezes que a pessoa tentou