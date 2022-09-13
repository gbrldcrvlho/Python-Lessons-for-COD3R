#              ENT.1 > PROCESSAMENTO (ALGORITMO)
# ENTRADAS  >  ENT.2 > PROCESSAMENTO (ALGORITMO)  >>>  SAIDA
#              ENT.3 > PROCESSAMENTO (ALGORITMO)

def saudacao(nome = 'Pessoa', idade = 20):
    print(f'Bom dia {nome},\nVoce nao parece ter {idade} anos!')

# def saudacao():
#     print(f'Boa tarde!')

def soma_e_multi(a, b, x):
    return a + b * x

## SO IRA UTILIZAR ESTA FORMA SE VOCE QUISER QUE ESTE SO SEJA EXECUTADO PELO ARQUIVO QUE DEU INICIO A SUA APLICACAO
if __name__ == '__main__':
    saudacao(nome = 'Ana', idade = 30)