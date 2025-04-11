contador = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 3 == 0:
        contador+= 1

print(f"Você digitou {contador} número(s) múltiplo(s) de 3.")