import random

def lancar_moeda(): #função que simula o lançamento de uma moeda
    return random.choice(["cara", "coroa"])

#inicializando as variáveis
sequencia = []
contador_cara = 0

#simula o lançamento
while contador_cara < 3:
    resultado = lancar_moeda()
    print(f"Lançamento: {resultado}")
    
    #adiciona o resultado no final da sequência
    sequencia.append(resultado)
    
    #verifica se as últimas 3 jogadas foram "cara"
    if len(sequencia) >= 3 and sequencia[-3:] == ["cara", "cara", "cara"]:
        contador_cara = 3  #encerrar o loop
    else:
        contador_cara = sequencia[-3:].count("cara")  #conta o número de "caras" consecutivas

print("Sequência final de lançamentos:", sequencia)
