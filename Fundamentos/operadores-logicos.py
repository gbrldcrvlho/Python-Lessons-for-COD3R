True or False
7 != 3 and 2 > 3

# Tabela verdade do AND
True and True #verdadeiro
True and False #falso
False and True #falso
False and False #falso

# Tabela verdade do OR
True or True #verdadeiro
True or False #verdadeiro
False or True #verdadeiro
False or False #falso

# Tabela verdade do XOR
True != True #falso
True != False #verdadeiro
False != True #verdadeiro
False != False #falso

# Operador de Negacao (unario)
not True #falso
not False #verdadeiro
not 0 #verdadeiro
not 1 #falso
not -1 #verdadeiro
not not -1 #verdadeiro

# Cuidado!
True & True
False | True

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)