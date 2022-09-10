a = 3
b = 4.4

print(a + b)

texto = 'Sua idade e...'
idade = 23

# print(texto + str(idade))
print(f'{texto} {12 + 13}')

saudacao = 'bom dia '
print(3 * saudacao)

# EM PYTHON NAO EXISTE CONSTANTES MAS EXISTE UMA CONVERSAO QUE VOCE VAI USAR LETRAS MAISCULAS PARA DEFINIR CONSTANTES!

PI = 3.14
PI = 3.1415
raio = float(input('Informe o raio da circ? '))
# area = PI * raio * raio
area = PI * pow(raio, 2)

print(f'A area da circ e {area} m2.')