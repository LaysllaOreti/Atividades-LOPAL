valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))

valores_pares = (valor1 % 2 == 0) and (valor2 %2 == 0)

print(f"Os dois valores inseridos são pares?: {valores_pares}")
