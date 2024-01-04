#simples, composto, encadeado
n1 = n2 = 0.0
media = 0.0
n1 = float(input('Digite a primeira  nota:'))
n2 = float(input('Digite a segunda nota:'))

#calcular a media aritmetica das notas

media = (n1 + n2) / 2
if (media >= 7):
    print('você foi aprovado!')
elif (media >= 5):
    print('você está de recuperação!')
else:
    print('que pena, você foi reprovado!')

print('Sua média é {}'.format(media))




# Este código usa desvios condicionais para verificar a situação de um aluno com base na sua média.
#
# A instrução `if` verifica se a média do aluno é maior ou igual a 7. Se for, o aluno é aprovado.
#
# A instrução `elif` verifica se a média do aluno é maior ou igual a 5. Se for, o aluno está de recuperação.
#
# A instrução `else` é executada se as condições das instruções `if` e `elif` não forem atendidas. 
# No caso deste código, isso significa que o aluno foi reprovado.
