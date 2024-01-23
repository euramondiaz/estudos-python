# Importa o módulo random, que fornece funcionalidades para geração de números aleatórios.
import random

# Imprime uma mensagem informando a geração de cinco números aleatórios entre 1 e 50.
print('gerar cinco numeros elatorios entre 1 e 50, \n')

# Utiliza um loop for para gerar e imprimir cinco números aleatórios.
for i in range(5):
    # Gera um número aleatório inteiro no intervalo de 1 a 50 (inclusive) e atribui à variável 'n'.
    n = random.randint(1, 50)
    
    # Imprime o número aleatório gerado.
    print(f'numero gerado: {n}')
