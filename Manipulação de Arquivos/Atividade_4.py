import pandas as pd

dados = {
    "Produto": ["Celular"],
    "Quantidade": [10]
}

df = pd.DataFrame(dados)

df.to_excel("vendas.xlsx", index=False)
