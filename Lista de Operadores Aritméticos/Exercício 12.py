nota1 = float(input("Digite a sua primeira nota: "))
peso1 = float(input("Insira o peso da primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))
peso2 = float(input("Insira o peso da segunda nota: "))

nota3 = float(input("Digite a sua terceira nota: "))
peso3 = float(input("Insira o peso da terceira nota: "))

ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A média ponderada é igual a {ponderada}")
