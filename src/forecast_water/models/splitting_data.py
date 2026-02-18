#%%
import pandas as pd 
from pre_processing import separar_base, remover_colunas

#%%
data = pd.read_csv('../../data/processed/final_data.csv')
data = remover_colunas(data) 
X_train, X_val, X_test, y_train, y_val, y_test = separar_base(data)



# %%
X_train.to_csv("../../data/train_test/X_train.csv", index = False)
X_val.to_csv("../../data/train_test/X_val.csv", index = False)
X_test.to_csv("../../data/train_test/X_test.csv", index = False)
y_train.to_csv("../../data/train_test/y_train.csv", index = False)
y_val.to_csv("../../data/train_test/y_val.csv", index = False)
y_test.to_csv("../../data/train_test/y_test.csv", index = False)
# %%
