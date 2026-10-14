import os

os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 + n4) / 4
    return media

def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    if os.path.exists(caminho) and os.path.isdir(caminho):
        tipo = 'w'
        enc = 'utf-8'
        if os.path.exists(caminho + '/' + arquivo):
            tipo = 'a'
        with open(caminho + '/' + arquivo, tipo, encoding=enc) as file:
            file.write(linha_arq)
    else:
        print('Diretorio invalido')

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir
    global arq
    linha: str = ''

    dir = '/tmp/exercicios'
    arq = 'ex21.txt'
    linha = nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'
    escreveArq(dir, arq, linha)

def entrada():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input('Digite o nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
    valor_media = med(nota1, nota2, nota3, nota4)
    print('Media:', valor_media)
    if valor_media >= 6.0:
        print('APROVADO')
    elif valor_media >= 3.0:
        print('EXAME')
    else:
        print('RETIDO')
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def main():
    contador: int = 0

    os.makedirs('/tmp/exercicios', exist_ok=True)
    os.chmod('/tmp/exercicios', 0o744)

    for contador in range(0, 5, 1):
        entrada()

if __name__ == '__main__':
    main()
