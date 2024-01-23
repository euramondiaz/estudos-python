# Duas listas são definidas, n1 e n2, contendo valores numéricos.
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]

# A lista 'valores' é criada concatenando as listas n1 e n2.
valores = n1 + n2

# O primeiro elemento da lista 'valores' é alterado para 9.
valores[0] = 9

# Imprime o comprimento (número de elementos) da lista 'valores'.
print(len(valores))

# Imprime a lista 'valores' ordenada de forma decrescente.
print(sorted(valores, reverse=True))

# Imprime a soma de todos os elementos da lista 'valores'.
print(sum(valores))

# Imprime o valor mínimo da lista 'valores'.
print(min(valores))

# Imprime o valor máximo da lista 'valores'.
print(max(valores))
