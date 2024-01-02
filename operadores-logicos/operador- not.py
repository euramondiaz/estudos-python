tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
mensagem = 'Tem dinheiro?' + str(tem_dinheiro)
print(mensagem)

# O operador `not` em Python é usado para negar o valor lógico de uma expressão.
# Isso significa que o resultado da operação será `True` se a expressão for `False` e `False` se a expressão for `True`.

# No código acima, a variável `tem_dinheiro` é inicializada com o valor `True`.
# Em seguida, a variável `tem_dinheiro` é atualizada com o valor do operador
# `not tem_dinheiro`.
# A operação `not tem_dinheiro` nega o valor lógico da variável `tem_dinheiro`, que é `True`.
# Portanto, o valor da operação é `False`.
# Como a variável `tem_dinheiro` é atualizada com o valor `False`, a mensagem
# `Tem dinheiro? False` será impressa.
