import pandas as pd

df = pd.read_excel("pedidosEcommerce.xls")

df.to_csv("pedidosEcommerce.csv", index=False)

print("Arquivo convertido para .csv com sucesso total!")
