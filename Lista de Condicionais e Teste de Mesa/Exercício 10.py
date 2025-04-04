print("10 - Esse programa irá calcular a média das três provas descartando a menor nota")  
 
nota1 = float(input("Informe a primeira nota: "))  
nota2 = float(input("Informe a segunda nota: "))  
nota3 = float(input("Informe a terceira nota: "))  
menor_nota = min(nota1, nota2, nota3)  
media = (nota1 + nota2 + nota3 - menor_nota) / 2  
 
print(f"A média calculada, descartando a menor nota, é: {media:.2f}")
