numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número da sequência: "))
    numeros.append(numero) #colocar o número dentro da lista
    
#cálculo da média
media = sum(numeros) / len(numeros) #sum é os números que tem dentro da lista e o len quantos números estão na lista

#conta os números menores que a média
menores = 10
for num in numeros:
    if num < media:
        menores += 10
        
#exibir o resultado
print(f"A média dos números é: {media}") #.2f é para exibir apenas duas casas decimais
print(f"\nA quantidade de número(s) menor(es) que a média é(são): {menores}")