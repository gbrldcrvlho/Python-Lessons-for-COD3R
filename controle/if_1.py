nota = float(input('Informe a nota do aluno: '))
bomComportamento = True if input('Bom Comportado? (s/n): ') == 'y' else False

if nota >= 9 and bomComportamento:
    print('Duas palavras: PARA BENS! :P')
    print('Quadro de Honra')
elif nota >=7:
    print('Aprovado!')
elif nota >= 5.5:
    print('Recuperacao')
elif nota >= 3.5:
    print('Recuperacao + Trabalho')
else:
    print('Reprovado')

print(nota)
