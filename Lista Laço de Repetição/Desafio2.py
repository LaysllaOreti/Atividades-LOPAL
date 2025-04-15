import random

palavras = ["layslla", "marcia", "python", "backend", "tecnologia"]

palavra = random.choice(palavras).lower() #transforma todas as letras em minúsculas

letras_erradas = []
letras_certas = []
tentativas = 6

print("***** Seja bem-vindo(a) ao Jogo da Forca *****")
print("_ " * len(palavra)) #mostra o tamanho da palavra

while tentativas > 0:
    letra = input("\nDigite uma letra: ").lower() #transforma em minúsculo
    
    if letra in letras_erradas or letra in letras_certas: #faz a verificação para ver se a letra está em algumas das listas, e continua 
        print("Você já digitou essa letra antes. Por favor, escolha outra.") 
        continue
    
    if letra in palavra: 
        letras_certas.append(letra) 
        print("Letra correta, parabéns! Continue jogando.") 
        
    else:
        letras_erradas.append(letra) #Se a letra estiver errada, diminui 1 das tentativas 
        tentativas -= 1 
        print(f"Letra errada! Restam {tentativas} tentativas.")
        
    progresso = "" 
    for l in palavra: 
        if l in letras_certas: 
            progresso += l + " "
        else: 
            progresso += "_ "
            
    print("\nPalavra:", progresso) 
    print("Letras erradas:", ", ".join(letras_erradas)) #.join usado para separar itens em uma lista
    
    if all(l in letras_certas for l in palavra): 
        print(f"\nParabéns, você ganhou! A palavra era: {palavra}") 
        break
    
else:
    print("\nFim de jogo! Infelizmente você perdeu.")
    print(f"A palavra correta era: {palavra}")