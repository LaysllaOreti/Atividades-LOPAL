hora= int(input("Digite alguma hora:"))
min= int(input("Digite algum minuto:"))
seg= int(input("Digite algum segundo:"))
if (hora>=0 and hora<=24) and (min>=0 and min<=60) and (seg>=0 and seg<=60):
print("Hora Válida")
else:
print("Inválido")
