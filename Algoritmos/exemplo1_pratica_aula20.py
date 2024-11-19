# EXEMPLO PRÁTICO - AULA 20

# Dados em listas
dados = {1, 2, 3, 4, 5}

# Calcula a media
media = sum(dados) / len(dados)
print(f"Média: {media}")

# Calcular as diferenças entre cada valor e a média
diferencas = [x - media for x in dados] # Subtrai o valor menos a media para cada X na lista de dados
print(f"Diferenças em relação a média: {diferencas}")

# Elevar as diferenças ao quadrado (Para evitar valores negativos)
quadrado_diferencas = [x**2 for x in diferencas]
print(f"Quadrados das diferenças: {quadrado_diferencas}")

# Calcular a média dos quadrados das diferenças
media_quadrados_diferencas = sum(quadrado_diferencas) / len(quadrado_diferencas)
print(f"Variancia é a média dos quadrados das difereças: {media_quadrados_diferencas}")

# Calcular a raiz quadrada da média dos quadrados das diferenças
desvio_padrao = media_quadrados_diferencas ** 0.5
print(f"Desvio padrão é a raíz quadrada da variância: {desvio_padrao}")
