from random import randint

# Definição de funções

#Definindo o tabuleiro, cada célula possuindo ou não uma moeda
def definir_tabuleiro(n_linhas, n_colunas):
    T = []
    while len(T) != n_linhas:
        linha = []
        while len(linha) != n_colunas:
            a = randint(0,1)
            linha.append(a)
        T.append(linha)

    return T

def print_matriz(matriz):
    for i in range(0,len(matriz)):
        print(matriz[i])

# Função recursiva que percorre todos os caminhos possiveis e retorna o valor
# da maior quantidade de moedas que pode ser pega
def caminhar(T, n_linhas, n_colunas, n, m):
    if n == 1 and m == 1:
        return T[n_linhas-1][n_colunas-1]

    # Se ainda nao for a última coluna
    if (m > 1):
        # Ve o caminho para direita
        soma1 = T[n_linhas - n][n_colunas - m] + caminhar(T,n_linhas, n_colunas, n, m-1)
    else:
        soma1 = 0

    # Se ainda não for a última linha
    if (n > 1):
         # Ve o caminho para baixo
        soma0 = T[n_linhas - n][n_colunas - m] + caminhar(T, n_linhas, n_colunas, n-1, m)
    else:
        soma0 = 0


    if soma1 > soma0:
        return soma1
    else:
        return soma0


# Programa principal

#Lendo informações de tamanho da tabela
n_linhas = int(input("Digite a quantidade de linhas do tabuleiro:"))
n_colunas = int(input("Digite a quantidade de colunas do tabuleiro:"))


#Inicializando matriz do tabuleiro com as moedas
T = definir_tabuleiro(n_linhas, n_colunas)
print("\nTabuleiro: \n")
print_matriz(T)

# Chamando função que calcula a maior quantidade de moedas a ser pega
soma = caminhar(T,n_linhas, n_colunas, n_linhas, n_colunas)

print("\nMaior numero de moedas que pode ser pego: \n" + str(soma))
