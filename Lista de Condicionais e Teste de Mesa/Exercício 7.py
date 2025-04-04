numero = int(input("Digite uma nota entre 0 e 10: "))
if numero >= 0 and numero < 3:
print("E")
elif numero >= 3 and numero < 5:
print("D")
elif numero >= 5 and numero < 7:
print("C")
elif numero >= 7 and numero < 9:
print("B")
elif numero >= 9 and numero <= 10:
print("A")
else:
print("Nota inválida")
