# EXEMPLO 2: AULA 20
import pandas as pd
import numpy as np

dados = pd.Series([2,4,6,8,10])

# Transforma os dados em array numpy
conjunto_dados = np.array(dados)

print(f"Conjunto de dados: {conjunto_dados}")

# Calcula a média
md_dados = conjunto_dados.mean()
print(f"Média dos dados: {md_dados}")

# Calcula a variancia
var_dados = np.var(conjunto_dados)
print(f"Variância da série de dados: {var_dados}")

# Calcula o desvio padrão
# O desvio padrão é a raiz quadrada da variancia
dp1_dados = np.sqrt(conjunto_dados.var())
print(f"Desvio padrão 1 da série de dados: {dp1_dados}")

# Forma mais direta de calcular o desvio padrão
# Calcula diretamente o DP do conjunto de dados
dp2_dados = np.std(conjunto_dados)
print(f"Desvio padrão 2 da série de dados: {dp2_dados}")

# Distancia entre a variancia e a média
distancia_var_media = var_dados / (md_dados ** 2)
print(f"Distância entre a variância e a média: {distancia_var_media}")

# Coeficiente de variação
coef_variacao = (dp2_dados / md_dados) * 100
print(f"Coeficiente de variação: {coef_variacao}")

# Calcula a variancia DO CALCULO DE AMOSTRA
var_a_dados = np.var(conjunto_dados, ddof=1)
print(f"Variância amostral da série de dados: {var_a_dados}")

# Desvio padrão AMOSTRAL
dpa_dados = np.std(conjunto_dados, ddof=1)
print(f"Desvio padrão amostral da série de dados: {dpa_dados}")