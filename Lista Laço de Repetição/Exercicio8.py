import random

i = 0 #inicializa como 0
escolha = []

while i < 3:
    operacao = random.choice(["cara", "coroa"])
    escolha.append(operacao)
    if operacao == "cara":
        i += 1
    else:
        continue
    print(escolha)
