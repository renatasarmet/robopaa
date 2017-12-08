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

#Criando tabela F de forma que todas as células iniciam-se com zero
def criar_tabela(n_linhas, n_colunas):
    F = []
    while len(F) != n_linhas:
        linha = []
        while len(linha) != n_colunas:
            linha.append(0)
        F.append(linha)

    return F

def print_matriz(matriz):
    for i in range(0,len(matriz)):
        print(matriz[i])

def maior_qtd(matriz):
    return matriz[len(matriz)-1][len(matriz[0])-1]

# Programa principal

#Lendo informações de tamanho da tabela
n_linhas = int(input("Digite a quantidade de linhas do tabuleiro:"))
n_colunas = int(input("Digite a quantidade de colunas do tabuleiro:"))


#Inicializando matrizes
T = definir_tabuleiro(n_linhas, n_colunas)
print("\nTabuleiro: \n")
print_matriz(T)
F = criar_tabela(n_linhas, n_colunas)

#Inicializando percurso
F[0][0] = T[0][0]

#Preenchendo primeira linha
for j in range(1,n_colunas):
    F[0][j] = F[0][j-1] + T[0][j]

for i in range(1,n_linhas):
    #Preenchendo primeira coluna
    F[i][0] = F[i-1][0] + T[i][0]

    #Preenchendo restante
    for j in range(1,n_colunas):
        F[i][j] = max(F[i-1][j],F[i][j-1]) + T[i][j]

print("\nPercurso: \n")
print_matriz(F)
print("\nMaior numero de moedas que pode ser pego: \n" + str(maior_qtd(F)))
