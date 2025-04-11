#inicializa as variáveis
maior = None
segundo_maior = None

while True:
    numero = input("Digite um número (ou 'sair' para terminar): ")
    
    if numero.lower() == 'sair':
        break
    
    try:
        numero = int(numero)
        
        #verifica o maior e segundo maior números
        if maior is None or numero > maior:
            segundo_maior = maior
            maior = numero
        elif segundo_maior is None or numero > segundo_maior:
            segundo_maior = numero
    except ValueError:
        print("Por favor, digite um número válido.")

#exibe o segundo maior número
if segundo_maior is not None:
    print(f"O segundo maior número é: {segundo_maior}")
else:
    print("Não há segundo maior número. Foi digitado apenas um número.")
