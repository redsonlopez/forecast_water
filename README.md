# Sistema de Previsão de Consumo de Água da PBH com Séries Temporais

Aplicação web para análise e previsão do consumo de água da prefeitura, utilizando modelagem de séries temporais para estimar custos futuros com base nos registros a partir de 2022, com deploy em Streamlit Cloud.

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
