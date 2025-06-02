def descriptografar(texto, deslocamento=3):#Deslocado 3 letras do alfabeto
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nova_letra = chr((ord(letra) - base - deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

with open("textocriptografado.txt", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    texto_original = descriptografar(linha.strip())
    print(texto_original)