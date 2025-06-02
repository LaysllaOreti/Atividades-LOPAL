import csv
import json

dados = []

with open("pedidosEcommerce.csv", encoding='utf-8') as csv_file:
    leitor = csv.DictReader(csv_file)
    for linha in leitor:
        dados.append(linha)

with open("pedidosEcommerce.json", "w", encoding='utf-8') as json_file:
    json.dump(dados, json_file, indent=4)
