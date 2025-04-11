#verificar se um número é primo
def primo(num):
    if num < 2:  #se o número for menor que 2
        return False #retornará falso, pois não tem números primos menores que 2
    for i in range(2, int(num**0.5) + 1):  #verifica se o número é divisível por 2 e a raiz quadrada dele
        if num % i == 0: #resultado sendo 0
            return False #se for, ele retornará false, pois não é um número primo
    return True  #se ele não for divisível, ele é primo e retorna True

#entrada dos números
inicio = int(input("Digite o primeiro número inteiro: "))
fim = int(input("Digite o segundo número inteiro: "))

#caso o segundo número seja maior que o primeiro, ajusta a ordem
if inicio > fim:
    inicio, fim = fim, inicio

print(f"O(s) número(s) primo(s) entre {inicio} e {fim} são:")
for numero in range(inicio, fim + 1):
    if primo(numero):
        print(numero)