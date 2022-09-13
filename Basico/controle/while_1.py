## COM QUANTIDADE DETERMINADA DE REPETICOES
### NESTE TIPO DE CASO A MELHOR OPCAO E USAR O 'FOR'
x = 10

while x:
    print(x)
    x -= 1

print('FIM')

## SEM QUANTIDADE DETERMINADA DE REPETICOES

total = 0
nota = 0
qtde = 0

while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota !=-1:
        qtde += 1
        total += nota

print(f'A media da aturma e {total / qtde}')
