capital = int(input("Insira o valor do capital: "))
juros = int(input("Insira a taxa de juros: "))
tempo = int(input("Insira o tempo em anos: "))

juros_compostos = capital*(1+juros)**tempo

print(f"O valor total do montante é igual a: {juros_compostos}")
