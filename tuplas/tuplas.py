# As tuplas 'halogenios' e 'gases_nobres' são criadas e contêm elementos específicos.
# A tupla 'elementos' é criada concatenando as tuplas 'halogenios' e 'gases_nobres'.
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

# A tupla 't1' é criada com diversos valores numéricos.
t1 = (5, 2, 6, 2, 4, 4, 6, 7, 78, 6, 67, 6, 7, 5, 344, 2, 12)

# Imprime o valor máximo da tupla 't1' utilizando a função max().
print(max(t1))

# Imprime o valor mínimo da tupla 't1' utilizando a função min().
print(min(t1))
