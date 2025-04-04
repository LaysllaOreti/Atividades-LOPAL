num1 = float(input("Informe o primeiro número: "))  
num2 = float(input("Informe o segundo número: "))  
operacao = input("Informe a operação (+, -, *, /): ")  
if operacao == "+":  
    resultado = num1 + num2  
elif operacao == "-":  
    resultado = num1 - num2  
elif operacao == "*":  
    resultado = num1 * num2  
elif operacao == "/":  
    if num2 != 0:  
    resultado = num1 / num2  
else: 
    resultado = "Erro na divisão! Não é possível dividir um número por zero"

