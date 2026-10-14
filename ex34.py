import os

os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)


valor: int = 0
dir: str = ''
arq: str = ''

def mult(vlr, tab):
    res: int = 0
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir
    global arq
    dir = '/tmp/exercicios'
    arq = 'ex34.txt'
    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    tipo = 'w'
    enc = 'utf-8'
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):
        if os.path.exists(dir + '/' + arq) and c > 0:
            tipo = 'a'
        with open(dir + '/' + arq, tipo, encoding=enc) as file:
            file.write(linha)
    else:
        print('Diretorio invalido')

def main():
    global valor
    contador: int = 0
    result: int = 0

    os.makedirs('/tmp/exercicios', exist_ok=True)
    os.chmod('/tmp/exercicios', 0o744)

    valor = int(input('Digite um valor entre 1 e 10: '))
    for contador in range(0, 11, 1):
        result = mult(valor, contador)
        grava(contador, result)

if __name__ == '__main__':
    main()