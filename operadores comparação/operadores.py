x = y = z = False
n1 = n2 = 0


print ('Digite um numero')
n1 = int(input())
n2 = int(input('digite outro numero='))

x = n1 == n2 
print ('são iguais?', x, '\n')

z = n1 > n2
print(n1, 'é maior que', n2, '?', z,'\n')

y = n1 != n2
print('são diferentes?' + str(y))


# Este código demonstra o uso de operadores de comparação em Python.
# Os operadores de comparação são usados para comparar dois valores.
# Os resultados das comparações podem ser usados para controlar o fluxo do código.


# As variáveis `n1` e `n2` são inicializadas com o valor 0.
# O usuário é solicitado a digitar dois números.
# Os números digitados são armazenados nas variáveis `n1` e `n2`.
