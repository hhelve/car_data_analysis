import pandas as pd
import datetime

ano_atual = datetime.datetime.now().year
df = pd.read_csv("carros_teste.csv")


class Carro:
    def __init__(self, modelo, ano, preco, mileage):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.mileage = mileage

    def idade(self, ano_atual):
        return ano_atual - self.ano

    def preco_ajustado(self, ano_atual):
        idade = self.idade(ano_atual)
        preco_apos_idade = self.preco * (0.95**idade)
        preco_apos_mileage = preco_apos_idade * (1 - (self.mileage * 0.0001))
        preco_final = max(preco_apos_mileage, 0)
        return round(preco_final, 2)


carros = []
for _, row in df.iterrows():
    try:
        carro = Carro(
            marca=row["marca"],
            modelo=row["modelo"],
            ano=row["ano"],
            preco=row["preco"],
            mileage=row["mileage"],
    )
        carros.append(carro)
    except ValueError:
        print(f"Erro ao criar carro com dados: {row}")
    except KeyError:
        print(f"Coluna faltosa no carro: {row}")
    except Exception as e:
        print(f"Erro ao criar carro com dados: {row}")
