# ATIVIDADE 1

import pandas as pd
import numpy as np
import os

# 1. Coletando Dados
try:
    tb_vendas = pd.read_csv("tb_Vendas2017_Miranda.csv", sep=";", encoding="iso-8859-1")
    tb_produtos = pd.read_csv("tb_CadastroProdutos2017_Miranda.csv", sep=";", encoding="iso-8859-1")

    df_vendas = tb_vendas[["ID Produto", "Quantidade Vendida"]]
    df_produtos = tb_produtos[["ID Produto", "Preco Unitario"]]
    
    # convertendo preco unitario para numero
    df_produtos.loc[:, "Preco Unitario"] = df_produtos["Preco Unitario"].str.replace(",",".").astype(float)
    
    # NAO USADO - Convertendo arquivos
    # df_produtos.loc[:, "ID Produto"] = df_produtos["ID Produto"].astype(str)
    # df_vendas.loc[:, "ID Produto"] = df_vendas["ID Produto"].astype(str)
    # df_vendas.loc[:, "Quantidade Vendida"] = df_vendas["Quantidade Vendida"].astype(int)

    # Unindo os dados das duas tabelas
    df_vendasprodutos = pd.merge(df_vendas, df_produtos, on="ID Produto")

    # Descobrindo o valor total vendido
    df_vendasprodutos["Valor Total"] = df_vendasprodutos["Quantidade Vendida"] * df_vendasprodutos["Preco Unitario"]

    # Agrupando ID por produto
    df_vendasprodutos = df_vendasprodutos.groupby("ID Produto").agg({
        "Quantidade Vendida" : "sum",
        "Valor Total" : "sum"
    }).reset_index()

    # Print de teste
    print(df_vendasprodutos)

except Exception as e:
    print(f"Erro {e}")
    exit()

# 2. Interpretando Dados
try:
    # ARRAY NUMPY
    array_produtos_vendidos = np.array(df_vendasprodutos["Valor Total"])

    media_produtos_vendidos = np.mean(array_produtos_vendidos)
    mediana_produtos_vendidos = np.median(array_produtos_vendidos)
    distancia = abs((media_produtos_vendidos - mediana_produtos_vendidos) / mediana_produtos_vendidos) * 100

    # medidas de dispersão
    maximo = np.max(array_produtos_vendidos)
    minimo = np.min(array_produtos_vendidos)
    amplitude = maximo - minimo
    
    q1 = np.quantile(array_produtos_vendidos, 0.25, method="weibull")
    q3 = np.quantile(array_produtos_vendidos, 0.75, method="weibull")

    # IQR é a amplitude do intervalo dos dados centrais. ignora e não sofre interferência dos valores extremos
    # mais proximo de zero, mais homogeneo. mais proximo do q3, mais heterogeneo
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    # Filtrar o dataframe para outliers inferiores
    df_vendasprodutos_outinf = df_vendasprodutos[df_vendasprodutos["Valor Total"] < limite_inferior]
    df_vendasprodutosoutsup = df_vendasprodutos[df_vendasprodutos["Valor Total"] > limite_superior]

    # Calculando medidas (Da aula 20)
    variancia_vendas = np.var(array_produtos_vendidos)
    dp_vendas = np.std(array_produtos_vendidos)
    dist_vendas = variancia_vendas / (media_produtos_vendidos ** 2)
    coef_vendas = (dp_vendas / media_produtos_vendidos)*  100

    # Prints
    print(f"\nMedidas de Tendência Central")
    print(f"Média do Valor Total: {media_produtos_vendidos}")
    print(f"Mediana do Valor Total: {mediana_produtos_vendidos}")
    print(f"Distância: {distancia}%")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Amplitude: {amplitude}")
    print(f"Q1: {q1}")
    print(f"Q3: {q3}")
    print(f"IQR: {iqr}")
    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    # Medidas da aula 20:
    print(f"Variância das vendas: {variancia_vendas}")
    print(f"Desvio padrão das vendas: {dp_vendas}")
    print(f"Distância entre variância e média: {dist_vendas}")
    print(f"Coeficiente de variação: {coef_vendas}")

    # Calculando Outliers
    if len(df_vendasprodutos_outinf) == 0:
        print("\nNÃO EXISTEM OUTLIERS INFERIORES")
    else:
        print("\nOUTLIERS INFERIORES:")
        print(df_vendasprodutos_outinf.sort_values(by="Valor Total", ascending=True))
    
    if len(df_vendasprodutosoutsup) == 0:
        print("\nNÃO EXISTEM OUTLIERS SUPERIORES")
    else:
        print("\nOUTLIERS SUPERIORES:")
        print(df_vendasprodutosoutsup.sort_values(by="Valor Total", ascending=False))

except Exception as e:
    print(f"Erro {e}")

