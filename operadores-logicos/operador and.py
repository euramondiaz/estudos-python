
idade = 25
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
mensagem = 'pode participar do evento?' + str(resultado)

print (mensagem)

# O operador `and` em Python é usado para realizar uma conjunção lógica.
# Isso significa que o resultado da operação será `True` apenas se
# **ambos** os operandos forem `True`.

# No código acima, a variável `resultado` é inicializada com o valor da operação
# `(idade >= 18) and (altura >= 1.70)`.
# Essa operação verifica se a idade da pessoa é maior ou igual a 18 e se a altura da pessoa é maior ou igual a 1,70 metro.

# Se **ambos** os critérios forem atendidos, a operação `and` retornará o valor `True`.
# Caso contrário, se **um ou ambos** os critérios não forem atendidos, a operação `and` retornará o valor `False`.
