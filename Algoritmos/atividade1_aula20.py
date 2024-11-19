# VARIANCIA ENTRE A IDADE
import pandas as pd
import numpy as np

idades = ([5,10,12,35,38])

array_dados = np.array(idades)

med_idades = array_dados.mean()
var_idades = np.var(array_dados)
dp_idades = np.std(array_dados)

dist_idades = var_idades / (med_idades ** 2)
coef_idades = (dp_idades / med_idades) * 100


print(f"Variância do conjunto de dados: {var_idades}")
print(f"Desvio padrão do conjunto de idades: {dp_idades}")
print(f"Distância entre a variância e a média: {dist_idades}")
print(f"Coeficiente de variação: {coef_idades}")
