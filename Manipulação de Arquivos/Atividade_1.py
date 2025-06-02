import pandas as pd

historico_pedidos = [
    {'ID': 1, 'Nome': 'Layslla', 'Endereço': 'Rua Clovis, 100', 'Produto': 'Whey Protein', 'Quantidade': 1, 'Preço': 160, 'Data': '01/04/2025'},
    {'ID': 2, 'Nome': 'Daniel', 'Endereço': 'Rua das Veredas, 450', 'Produto': 'Pre-Treino', 'Quantidade': 2, 'Preço': 120, 'Data': '04/04/2025'},
    {'ID': 3, 'Nome': 'Pamella', 'Endereço': 'Rua Luciano da Silva, 185', 'Produto': 'Pasta de Amendoim', 'Quantidade': 1, 'Preço': 80, 'Data': '10/04/2025'},
    {'ID': 4, 'Nome': 'Eduardo', 'Endereço': 'Rua Carlos Antonio, 280', 'Produto': 'Creatina', 'Quantidade': 1, 'Preço': 76, 'Data': '20/04/2025'}
]

df = pd.DataFrame(historico_pedidos)

df.to_excel("pedidosEcommerce.xls", index=False)

print("Arquivo gerado com sucesso total!")
