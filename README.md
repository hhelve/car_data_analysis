# Projeto de Análise de Dados de Carros

Este projeto analisa dados de carros usando scripts Python para geração de dados, modelagem orientada a objetos e predição de aprendizado de máquina. Inclui criação de dados sintéticos, cálculos de ajuste de preços e modelagem de regressão para prever preços de carros com base em recursos como modelo, ano e quilometragem.

## Visão Geral do Projeto

O projeto consiste em vários scripts Python que trabalham juntos para processar e analisar dados de carros:

- **Geração de Dados**: Cria um conjunto de dados sintético de carros com atributos como modelo, ano, preço e quilometragem.
- **Modelagem de Dados**: Define uma classe `Car` para representar carros individuais e calcular preços ajustados considerando depreciação e quilometragem.
- **Aprendizado de Máquina**: Usa XGBoost para treinar um modelo de regressão para prever preços de carros.

## Descrição dos Arquivos

### Scripts Python

#### `dataset.py`
- **Propósito**: Gera um conjunto de dados sintético de 10.000 carros e realiza análise estatística básica.
- **Funcionalidade**:
  - Cria dados aleatórios para modelos de carros (3 Series, 5 Series, i3, Z4, X1), anos (2010-2023), preços (R$ 15.000-R$ 80.000) e quilometragem (5.000-150.000 km).
  - Salva o conjunto de dados completo em `carros_teste.csv`.
  - Computa e imprime estatísticas básicas: média, mediana, desvio padrão dos preços e o modelo mais comum.
  - Exibe um histograma interativo usando Plotly mostrando a relação entre quilometragem e preço, colorido por modelo.
  - Aplica um filtro para carros com preço > R$ 30.000 e modelo == "i3", salva os dados filtrados em `carros_filtro.csv`.
- **Dependências**: `pandas`, `random`, `plotly.express`.

#### `main.py`
- **Propósito**: Carrega dados de carros e cria objetos `Car` com cálculos de ajuste de preços.
- **Funcionalidade**:
  - Carrega dados de `carros_teste.csv` usando pandas.
  - Define uma classe `Car` com atributos: modelo, ano, preco, mileage.
  - Implementa o método `idade()` para calcular a idade do carro com base no ano atual.
  - Implementa o método `preco_ajustado()` para calcular o preço ajustado:
    - Aplica depreciação anual de 5% por ano.
    - Reduz o preço com base na quilometragem (0,01% por km).
    - Garante que o preço não fique abaixo de 0.
  - Instancia objetos `Car` a partir do conjunto de dados, tratando possíveis erros (ValueError, KeyError, exceções gerais).
- **Dependências**: `pandas`, `datetime`.

#### `analise.py`
- **Propósito**: Treina um modelo de regressão XGBoost para prever preços de carros.
- **Funcionalidade**:
  - Carrega dados de `carros_teste.csv`.
  - Prepara recursos transformando logaritmicamente o alvo (preço) e codificando one-hot a coluna 'modelo'.
  - Divide os dados em conjuntos de treinamento (80%) e teste (20%).
  - Treina um regressor XGBoost com hiperparâmetros especificados:
    - 2500 estimadores, taxa de aprendizado 0,02, profundidade máxima 2, etc.
  - Faz previsões nos dados de teste e avalia usando Erro Quadrático Médio (MSE).
  - Imprime o valor do MSE.
- **Dependências**: `xgboost`, `pandas`, `sklearn`, `numpy`.

### Arquivos de Dados

#### `carros_teste.csv`
- Contém o conjunto de dados sintético completo gerado por `dataset.py`.
- Colunas: modelo, ano, preco, mileage.

## Dependências

Para executar os scripts, instale os seguintes pacotes Python:

```
pip install pandas plotly xgboost scikit-learn numpy
```

## Como Executar

1. **Gerar Conjunto de Dados**:
   ```
   python dataset.py
   ```
   Isso criará `carros_teste.csv`, e exibirá estatísticas e mostrará um histograma.

2. **Processar Dados com Classe Car**:
   ```
   python main.py
   ```
   Isso carregará os dados e criará objetos `Car` (sem saída a menos que ocorram erros).

3. **Treinar e Avaliar Modelo**:
   ```
   python analise.py
   ```
   Isso treinará o modelo XGBoost e imprimirá o Erro Quadrático Médio no conjunto de teste.

## Análise das Funcionalidades do Código

- **Geração de Dados (`dataset.py`)**: Fornece um ambiente controlado para testar scripts de análise com distribuições realistas de dados de carros. A capacidade de filtragem permite análise focada em modelos específicos de carros ou faixas de preço.

- **Modelagem Orientada a Objetos (`main.py`)**: Encapsula dados de carros e lógica de negócio para ajustes de preços. O modelo de depreciação (5% por ano + fator de quilometragem) simula a depreciação real de valor de carros.

- **Aprendizado de Máquina (`analise.py`)**: Implementa um pipeline robusto de regressão para predição de preços. A transformação logarítmica do alvo ajuda com distribuições enviesadas de preços, e a codificação one-hot trata recursos categóricos. A avaliação do modelo fornece insights sobre a precisão da predição.

Este projeto demonstra um fluxo de trabalho completo de ciência de dados, desde a criação de dados sintéticos até a modelagem preditiva, útil para aprendizado ou prototipagem de sistemas de análise de preços de carros.

