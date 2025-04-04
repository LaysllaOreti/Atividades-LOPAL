numero = int(input("Digite um número: "))

mensagem = ("É um número par", "É um número ímpar")

print(f"{numero} {mensagem[numero % 2]}")
