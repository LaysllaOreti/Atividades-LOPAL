qtd = float(input("Digite a quantidade de produtos a ser adquirido:"))
valor_inicial = float(input("Digite o valor unitário:"))
print(f"O valor inicial foi: {valor_inicial}")
print(f"A quantidade solicitada foi: {qtd}")
if(qtd>100):
desc = valor_inicial * (10 /100)
else: 
desc= valor_inicial * (5/100)
valor_desc = valor_inicial - desc
valor_final= qtd * valor_desc
print(f" O desconto é de: {desc:.2f}")
print(f"O valor final a pagar é: {valor_final:.2f}")

