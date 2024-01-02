#programa disparo de alarme

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
mensagem = 'alarme disparado?' + str(alarme)
print(mensagem)



# O operador `or` em Python é usado para realizar uma disjunção lógica.
# Isso significa que o resultado da operação será `True` se
# **pelo menos um** dos operandos for `True`.

# No código acima, a variável `alarme` é inicializada com o valor da operação
# `(porta == 'a') or (janela == 'a')`.
# Essa operação verifica se a porta está aberta ou se a janela está aberta.

# Se **pelo menos uma** das condições for atendida, a operação `or` retornará o valor `True`.
# Caso contrário, se **ambas** as condições não forem atendidas, a operação `or` retornará o valor `False`.
