number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

number_negative = (number1 < 0) or (number2 < 0)
print(f"Pelo menos um dos valores é negativo: {number_negative}")
