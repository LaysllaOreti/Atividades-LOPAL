idade = int(input("Digite sua idade: "))
if idade >= 18 and idade < 70:
    print(f"Seu Voto é obrigatório!")
elif idade == 16 or idade == 17 or idade > 70:
    print(f"Seu Voto é Facultativo!")
else:
    print(f"Você não é um eleitor")
