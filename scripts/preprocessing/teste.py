import pandas as pd

# Dados de exemplo (substitua pelos seus dados)
df = pd.read_csv("../../data/processed/final_data.csv")
# Converte a coluna para datetime
df['data_vencimento'] = pd.to_datetime(df['data_vencimento'])

# Extrai o mês e ano como um período (Period)
df['mes_ano_vencimento'] = df['data_vencimento'].dt.to_period('M') # 'M' para mês

# Agrupa e soma
df_agrupado = df.groupby(['matricula', 'mes_ano_vencimento'])['valor_fatura'].sum().reset_index()

print(df_agrupado)

# Para obter o mês e ano como strings formatadas:
df_agrupado['mes_ano_string'] = df_agrupado['mes_ano_vencimento'].dt.strftime('%Y-%m')
print("\nCom mês e ano como string:")
print(df_agrupado)

# Se precisar voltar para datetime:
df_agrupado['mes_ano_datetime'] = df_agrupado['mes_ano_vencimento'].dt.to_timestamp()
print("\nCom mês e ano como datetime:")
print(df_agrupado)