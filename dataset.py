import pandas as pd
import random
import plotly.express as px

modelos = ["3 Series", "5 Series", "i3", "Z4", "X1"]
anos = list(range(2010, 2024))
dados = []

for _ in range(10000):
    modelo = random.choice(modelos)
    ano = random.choice(anos)
    preco = random.randint(15000, 80000)
    mileage = random.randint(5000, 150000)
    dados.append([modelo, ano, preco, mileage])

df = pd.DataFrame(dados, columns=["modelo", "ano", "preco", "mileage"])

# Salvando CSV sem filtro
df.to_csv("carros_teste.csv", index=False)

# Media dos precos
print(df["preco"].mean())

# Mediana dos precos
print(df["preco"].median())

# Desvio padrao
print(df["preco"].std())

# Item mais comum
print(df["modelo"].mode())

# Grafico de dispersao
fig = px.histogram(df, x="mileage", y="preco", color="modelo")
fig.show()

# Filtro
filtro = df.query('preco > 30000 and modelo == "i3"')
print(filtro)

filtro.to_csv("carros_filtro.csv", index=False)