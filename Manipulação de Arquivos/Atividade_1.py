with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Ola mundo, eu sou Layslla Eduarda!\n")
    arquivo.write("Estou aprendendo Python!\n")

#Abre o arquivo em modo de leitura, "r"
arquivo = open("meu_arquivo.txt", "r")

#Lê o conteúdo do arquivo
#reusltado = arquivo.readlines() - lê com tudo na linha
resultado = arquivo.read()
print(resultado)

#Colocar caminho se não estiver dentro da pasta
with open("meu_arquivo.txt", "r") as arquivo:
    arquivo = open("meu_arquivo.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)

import csv
with open('meu_arquivoCsv.csv', 'w') as f:
    writer = csv.writer(f)

    # Escreve as linhas no arquivo
    writer.writerow("Nome, Preco")  # Primeira linha (cabeçalho)
    writer.writerow("Livro, 20")  # Segunda linha

print("Arquivo CSV criado com sucesso!")


with open('meu_arquivoCsv.csv', 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv)
    for row in reader:
        print(row)