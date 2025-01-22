#%% 
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import  OneHotEncoder

# Extraindo Ano e Mês de vencimento das faturas
def extrair_datas(data): 
    
    data['ANO_VENCIMENTO'] = data['DATA_VENCIMENTO'].dt.year
    data['MES_VENCIMENTO'] = data['DATA_VENCIMENTO'].dt.month
    data['TRIMESTRE'] = data['DATA_VENCIMENTO'].dt.quarter

    return data 
#%%[markdown]
# Vamos criar lags para faciliatar o nosso modelo a identificar padrões das faturas. 
# Como queremos prever o valor futuro da próxima fatura, é interessante que o modelo saiba qual foi o valor passado desta fatura,
# e para isso utilizaremos valores passados das faturas de cada matícula.  
#%%
def criar_lags_por_matricula(data, col, id_col, max_lag=5):
    """
    Cria colunas de lag para séries temporais agrupadas por um identificador.
    
    Parameters:
    - data (pd.DataFrame): DataFrame contendo os dados.
    - col (str): Nome da coluna para a qual os lags serão criados.
    - id_col (str): Nome da coluna de identificação para agrupar os dados (ex.: matrícula).
    - max_lag (int): Número máximo de lags a serem criados.
    
    Returns:
    - pd.DataFrame: DataFrame com as colunas de lag adicionadas.
    """
    def criar_lags_grupo(grupo):
        for lag in range(1, max_lag + 1):
            grupo[f'{col}_lag{lag}'] = grupo[col].shift(lag)
        return grupo
    
    # Aplica a função de lags para cada grupo
    data = data.groupby(id_col).apply(criar_lags_grupo)
    
    # Remove valores nulos gerados pelos lags
    data = data.dropna().reset_index(drop=True)
    
    return data





