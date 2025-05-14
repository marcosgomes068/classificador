# Classificador de Flores Iris

## Objetivo do Projeto
O projeto "Classificador de Flores Iris" tem como objetivo desenvolver um modelo de aprendizado de máquina capaz de prever a espécie de uma flor Iris com base em quatro características numéricas: comprimento do sépalo, largura do sépalo, comprimento da pétala e largura da pétala. Utilizando o conjunto de dados `load_iris()` da biblioteca `sklearn.datasets`, o projeto explora técnicas de pré-processamento, treinamento de modelos e avaliação de desempenho.

## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

```
Classificador-de-Flores-Iris
├── data
│   └── processed
│       └── .gitkeep
├── notebooks
│   └── iris_classification.ipynb
├── src
│   ├── __init__.py
│   ├── data_preparation.py
│   ├── model.py
│   └── visualization.py
├── models
│   └── .gitkeep
├── reports
│   └── figures
│       └── .gitkeep
├── requirements.txt
├── README.md
└── .gitignore
```

## Como Executar o Projeto
1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd Classificador-de-Flores-Iris
   ```

2. **Instale as dependências**:
   Utilize o arquivo `requirements.txt` para instalar as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o Jupyter Notebook**:
   Inicie o Jupyter Notebook e abra o arquivo `notebooks/iris_classification.ipynb`:
   ```bash
   jupyter notebook
   ```

4. **Siga as instruções no notebook**:
   O notebook contém todas as etapas do projeto, incluindo análise exploratória de dados, pré-processamento, treinamento de modelos e avaliação.

## O que você pode aprender
- Como carregar e preparar dados usando `pandas`.
- Técnicas de visualização de dados com `seaborn` e `matplotlib`.
- Implementação de modelos de aprendizado de máquina, como Regressão Logística, KNN e Árvore de Decisão.
- Avaliação de modelos utilizando métricas como matriz de confusão e relatório de classificação.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.