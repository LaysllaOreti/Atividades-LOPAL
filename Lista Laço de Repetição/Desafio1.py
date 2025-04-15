# solicitar os dados ao usuário 
pop_inicial = int(input("Digite o número atual de coelhos: ")) 
taxa_reproducao = float(input("Insira a taxa de reprodução (% por cada geração): ")) 
taxa_mortalidade = float(input("Insira a taxa de mortalidade (% por cada geração): ")) 
geracoes = int(input("Digite o número de gerações que deseja simular: ")) 

populacao = pop_inicial # inicializando a variável da população 

for geracao in range(1, geracoes + 1): 
    populacao += populacao * (taxa_reproducao / 100) # aumentar a população pela reprodução 
    
    populacao -= populacao * (taxa_mortalidade / 100) # diminuir a população pela mortalidade 
    print(f"A geração {geracao} possui: {int(populacao)} coelhos")