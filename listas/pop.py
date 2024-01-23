# Duas listas são definidas, n1 e n2, contendo valores numéricos.
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]

# A lista 'valores' é criada concatenando as listas n1 e n2.
valores = n1 + n2

# O primeiro elemento da lista 'valores' é alterado para 9.
valores[0] = 9

# Remove o último elemento da lista 'valores' utilizando o método pop().
valores.pop()
print(valores)

# Remove o elemento na posição 3 da lista 'valores' utilizando o método pop(index).
valores.pop(3)
print(valores)
