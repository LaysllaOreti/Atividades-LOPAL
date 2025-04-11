#solicita a frase para o usuário
frase = input("Digite uma frase: ")

#converter as letras para minúsculas
frase = frase.lower()

#inicializa os contadores para cada vogal que tiver
vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

#percorrer e contar as vogais de cada frase
for letra in frase:
    if letra in vogais:
        vogais[letra] += 1

#exibir o resultado
print("\nA quantidade de vogais na frase é: ")
for vogal, quantidade in vogais.items():
    print(f"{vogal}: {quantidade}")
