#%% 
import pandas as pd 
from modulos.remover_inconsistencias import * 
from modulos.feature_engineer import *
#%%

data= pd.read_csv("../../data/processed/stacked_water.csv")


#%% Aplicando pré-processamento dos dados

#Removendo colunas que não seram utilizadas 
data = remove_colunas(data)

# Formatando valores da base 
data = formata_valores_fatura(data)

#Removendo outliers utilizando o IQR 
data = remove_outliers(data, coluna='VALOR_FATURA')


# Removendo todas as faturas que estão zeradas:
data = data[data['VALOR_FATURA'] != 0]

#%%
# Adicionando região
#%%
data = adicionar_regiao_e_onehot(data)

#Extraindo Ano, trimestre e Mês
 
data = extrair_datas(data)

# Criando Lags com base nas análises ACF e PACF
data = criar_lags_por_matricula(data, col='VALOR_FATURA', id_col='MATRICULA', max_lag=2)

# Ordenando datas 
data = data.sort_values(by=['DATA_VENCIMENTO'], ascending=[True])

data.head()
#%%
data.to_csv("../../data/processed/final_data.csv", index=False, encoding="utf-8")
