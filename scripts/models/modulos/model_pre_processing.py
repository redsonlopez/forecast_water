# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split 


def separar_base(data): 
    """Separa a base entre treino validação, treino e teste 

    Args:
        data (dataframe): dataframe pandas com os dados 

    Returns:
        X_train, X_val, X_test, y_train, y_val, y_test
    """
    X = data.drop(columns=["VALOR_FATURA"])
    y = data["VALOR_FATURA"]

    # treino+validação e teste
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # treino+validação em treino e validação
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42)
    # A validação será 20% (0.25 * 0.8) dos dados totais.

    print("Tamanho do treino:", X_train.shape)
    print("Tamanho da validação:", X_val.shape)
    print("Tamanho do teste:", X_test.shape)
    
    return X_train, X_val, X_test, y_train, y_val, y_test
    
    
    
    
    
    
def remover_colunas(data): 
    """Remove colunas que não são relevantes para nosso modelo 
    """
    drop_features = [
                    'MATRICULA', 'DATA_VENCIMENTO', # irrelevante
                    'BAIRRO'# Estamos removendo o bairro por sua alta dimensionalide 
                     ]
    data = data.drop(columns = drop_features)
    
    return data 





def importar_dados(): 
    """
    Importa os dados para o projeto

    Returns:
        data: dataframe pandas com os dados para o modelo
    """
    data = pd.read_csv('..\\..\\data\\processed\\final_data.csv')
    data = remover_colunas(data) 
    X_train, X_val, X_test, y_train, y_val, y_test = separar_base(data)

    # Salva os dados como arquivos 
    
    X_train.to_csv("Train&TestData\\X_train.csv", index = False)
    X_val.to_csv("Train&TestData\\X_val.csv", index = False)
    X_test.to_csv("Train&TestData\\X_test.csv", index = False)
    y_train.to_csv("Train&TestData\\y_train.csv", index = False)
    y_val.to_csv("Train&TestData\\y_val.csv", index = False)
    y_test.to_csv("Train&TestData\\y_test.csv", index = False)
    
    # Carregar os dados
    X_train= pd.read_csv("Train&TestData\\X_train.csv", index_col= False)
    X_val= pd.read_csv("Train&TestData\\X_val.csv",index_col= False)
    X_test= pd.read_csv("Train&TestData\\X_test.csv",index_col= False)
    y_train= pd.read_csv("Train&TestData\\y_train.csv",index_col= False)
    y_val= pd.read_csv("Train&TestData\\y_val.csv",index_col= False)
    y_test= pd.read_csv("Train&TestData\\y_test.csv",index_col= False)
    
    return  X_train, X_val, X_test, y_train, y_val, y_test



def preprocessar_dados():

    """
    Transformer para pré-processamento dos dados. Recebe um dataframe como parametro e aplica as transformações
    listadas. 
    
    """    
        
    # Selecionando variaveis numericas, categoricas e variaveis que devem ser removidas para evitar data leakage
    numerical_features = ['VALOR_FATURA_lag1','VALOR_FATURA_lag2']
    
   
    preprocessor = ColumnTransformer(
        transformers=[
            # Aplica escalonamento aos dados numéricos.
            ('num', StandardScaler(), numerical_features),
        
        ])

    
    return preprocessor


