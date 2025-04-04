print("Esse programa verifica se os valores digitados formam um quadrado, um retângulo ou nenhum dos dois")
lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))
lado4 = float(input("Informe o quarto lado: "))
if lado1 == lado2 == lado3 == lado4:
resultado = "Quadrado"
elif (lado1 == lado3) and (lado2 == lado4):
resultado = "Retângulo"
else:
resultado = "Nenhum dos dois" 
print(f"A figura formada é: {resultado}")
