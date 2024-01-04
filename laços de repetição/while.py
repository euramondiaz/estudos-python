nome = None

while True:
    print('Digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'bem vindo, {nome}')
print('ate logo')