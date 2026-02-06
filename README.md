# Painel Interativo de Previsão do Consumo de Água com Séries Temporais

Aplicação web desenvolvida para análise e previsão do consumo de água da Prefeitura de Belo Horizonte, utilizando modelagem de séries temporais para estimar custos futuros com base em dados históricos a partir de 2022.  
O painel tem como objetivo apoiar a tomada de decisão e o planejamento eficiente dos recursos públicos.

---

A aplicação está disponível em nuvem via **Streamlit Cloud**:
https://redsonlopez-forecast-water-appapp-ulo5y7.streamlit.app/

Projeto desenvolvido em parceria por:
- **Hedson Lopes** — https://www.linkedin.com/in/redsonlopez/
- **Pedro Henrique** — https://www.linkedin.com/in/pedro-io/

---

## Estrutura do Projeto

A organização dos diretórios segue o modelo abaixo:

```plaintext
water_prediction/
├── data/
│   ├── raw/           # Dados brutos (registros originais a partir de 2022)
│   └── processed/     # Dados processados para análises e modelagem
├── notebooks/
│   └── eda/           # Notebooks de análise exploratória de dados
├── scripts/
│   ├── preprocessing/ # Scripts para limpeza e preparação dos dados
│   └── models/        # Scripts de treinamento, avaliação e predição
├── requirements.txt   # Dependências do Python (para uso com pip)
├── .gitignore         # Arquivos e pastas a serem ignorados pelo Git
└── README.md          # Documentação inicial do projeto
