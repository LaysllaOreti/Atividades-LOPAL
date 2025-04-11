lista = []
i = 0 #inicializa como 0

for i in range(1,11):
    lista.append(i)
numero_maior = lista.remove(max(lista))

print(f"O segundo maior número é: {max(lista)}")
