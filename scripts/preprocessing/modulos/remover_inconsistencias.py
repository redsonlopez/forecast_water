import pandas as pd 

def formata_valores_fatura(data): 
    # Remover os pontos (separadores de milhar) na coluna com os valores das faturas
    data['VALOR_FATURA'] = data['VALOR_FATURA'].str.replace('.', '', regex=False)

    # Substituir ',' por '.'
    data['VALOR_FATURA'] = data['VALOR_FATURA'].str.replace(',', '.', regex=False)

    # Converter para númerico
    data['VALOR_FATURA']= pd.to_numeric(data['VALOR_FATURA'])
    
    # Removendo espaços extra
    data["BAIRRO"]= data["BAIRRO"].str.strip()
    data['DATA_VENCIMENTO'] = data['DATA_VENCIMENTO'].str.strip()

    # Formatando a data
    data["DATA_VENCIMENTO"] = pd.to_datetime(data["DATA_VENCIMENTO"], format='mixed', dayfirst=True)    
    return data 
 
 
    
def remove_colunas(data): 
    colunas_para_manter = ["MATRICULA", "DATA_VENCIMENTO", "BAIRRO", "VALOR_FATURA"]
    data = data[colunas_para_manter]
    return data



def remove_outliers(data, coluna): 
    """ Utiliza os quartis do dataframe para remover outliers
        O IQR é calculado como a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1). Outliers são definidos como pontos abaixo de 
        Q1-1.5*IQR ou acima de Q3+1.5*IQR.
        
    Args:
        data (dataframe): dataframe com os dados
        coluna (string) : Nome da coluna que vai ser tratada
    Returns:
        _type_: _description_
    """
    # Calculando Q1, Q3 e IQR
    Q1 = data[coluna].quantile(0.25)
    Q3 = data[coluna].quantile(0.75)
    IQR = Q3 - Q1

    # Definindo limites
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    # Removendo outliers
    data = data[(data[coluna] >= limite_inferior) & (data[coluna] <= limite_superior)]
        
    return data