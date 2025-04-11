#Programa que solicitará 10 números e vai separá-los em pares e ímpares

pares = []
impares = []
numeros = []

#Entrada dos dados
for i in range(0,10):
    num = int(input(f"Digite o {i+1}° número:"))
    numeros.append(num)
    
#Lógica para verificarse é par ou ímpares
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
#Exibir o resultado
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")