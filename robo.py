import sys
import time

from random import randint
import copy
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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
    for i in range(n_linhas):
        l = []
        for j in range(n_colunas):
            l.append(0)
        F.append(l)
    return F

def print_matriz(matriz):
    for i in range(0,len(matriz)):
        print(matriz[i])

def maior_qtd(matriz):
    return matriz[len(matriz)-1][len(matriz[0])-1]

def caminhar(geral,T, n_linhas, n_colunas, n, m):
    if n == 1 and m == 1:
        geral.setVetorBruto([n_linhas-1,n_colunas-1])
        geral.setVetorSomas(0)
        return int(T[n_linhas-1][n_colunas-1])

    # Se ainda nao for a última coluna
    if (m > 1):
        # Ve o caminho para direita
        geral.setVetorSomas(0)
        geral.setVetorBruto([n_linhas - n, n_colunas - m])
        s = int(caminhar(geral,T,n_linhas, n_colunas, n, m-1))
        soma1 = int(T[n_linhas - n][n_colunas - m]) + s
        geral.setVetorBruto([n_linhas - n, n_colunas - m])
        geral.setVetorSomas(s)
        
    else:
        soma1 = 0

    # Se ainda não for a última linha
    if (n > 1):
         # Ve o caminho para baixo
        geral.setVetorSomas(0)
        geral.setVetorBruto([n_linhas - n, n_colunas - m])
        s = int(caminhar(geral,T, n_linhas, n_colunas, n-1, m))
        soma0 = int(T[n_linhas - n][n_colunas - m]) + s
        geral.setVetorBruto([n_linhas - n, n_colunas - m])
        geral.setVetorSomas(s)
    else:
        soma0 = 0


    if int(soma1) > int(soma0):
        return int(soma1)
    else:
        return int(soma0)

def algoritmo(geral,n,m):
    #Lendo informações de tamanho da tabela
    n_linhas = n
    n_colunas = m
    matrizes = []
    coloracao = []
    coloracao1 = []
    coloracao2 = []
    #Inicializando matrizes
    T = geral.matriz
    F = criar_tabela(n_linhas, n_colunas)
    
    #Inicializando percurso
    F[0][0] = T[0][0]
    coloracao.append([0,0,173 ,255 ,47])
    coloracao1.append([0,0,135  ,206  ,250])
    coloracao2.append([0,1,255 ,255 ,255])
    matrizes.append(copy.deepcopy(F))
    print(F)
    #Preenchendo primeira linha
    for j in range(1,n_colunas):
        F[0][j] = int(F[0][j-1]) + int(T[0][j])
        coloracao.append([0,j,173 ,255 ,47])
        coloracao1.append([0,j,135  ,206  ,250])
        coloracao2.append([0,j-1,135 ,206 ,250])
        matrizes.append(copy.deepcopy(F))
        print(F)
        time.sleep(1)
        
    for i in range(1,n_linhas):
        #Preenchendo primeira coluna
        F[i][0] = int(F[i-1][0]) + int(T[i][0])
        coloracao.append([i,0,173 ,255 ,47])
        coloracao1.append([i,0,135  ,206  ,250])
        coloracao2.append([i-1,0,135 ,206 ,250])
        matrizes.append(copy.deepcopy(F))
        print(F)
        time.sleep(1)
        #Preenchendo restante
        for j in range(1,n_colunas):
            F[i][j] = max(int(F[i-1][j]),int(F[i][j-1])) + int(T[i][j]) 
            coloracao.append([i,j,173 ,255 ,47])
            coloracao1.append([i,j,135  ,206  ,250])
            if(int(F[i-1][j]) > int(F[i][j-1])):
                coloracao2.append([i-1,j,135 ,206 ,250])
            else:
                coloracao2.append([i,j - 1,135 ,206 ,250])
            matrizes.append(copy.deepcopy(F))
            print(F)
            time.sleep(1)
    print(matrizes)
    geral.setColoracaoR(copy.deepcopy(coloracao))
    geral.setColoracaoT(copy.deepcopy(coloracao1))
    geral.setColoracaoR1(copy.deepcopy(coloracao2))
    print(coloracao)
    return matrizes
class Geral(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.vetoresBruto = []
        self.vetorSomas = []
        self.vetorVolta = []
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 13))
        grid1 = QGridLayout()
        grid1.setVerticalSpacing(10)
        grid1.setHorizontalSpacing(10)
        
        grid2 = QGridLayout()
        grid2.setVerticalSpacing(10)
        grid2.setHorizontalSpacing(10)
        
        grid3 = QGridLayout()
        grid3.setVerticalSpacing(10)
        grid3.setHorizontalSpacing(10)
        
        grid4 = QGridLayout()
        grid4.setVerticalSpacing(10)
        grid4.setHorizontalSpacing(10)
        
        grid5 = QGridLayout()
        grid5.setHorizontalSpacing(15)
        
        grid6 = QGridLayout()
        grid6.setHorizontalSpacing(1)
        
        grid7 = QGridLayout()
        grid7.setVerticalSpacing(20)
        
        grid8 = QGridLayout()
        grid8.setVerticalSpacing(20)
        
        grid9 = QGridLayout()
        grid9.setHorizontalSpacing(20)
        
        grid10 = QGridLayout()
        grid10.setVerticalSpacing(20)
        
        titulo = QLabel('Algoritmo para o problema do robo e as moedas', self)
        titulo.setAlignment(Qt.AlignCenter)
        
        configura = QLabel('Configurações do tabuleiro', self)
        
        bruto = QLabel('Algoritmo -  Bruto', self)
        
        pd = QLabel('Algoritmo -  Programação dinamica', self)
        
        lbl1 = QLabel('Digite o valor n do tabuleiro:', self)
        self.n = QLineEdit()

        lbl2 = QLabel('Digite o valor m do tabuleiro:', self)
        self.m = QLineEdit()
        
        self.soma = QLabel('0', self)
        igual = QLabel('=', self)
        mais = QLabel('+', self)
        self.s1 = QLabel('0', self)
        self.s2 = QLabel('0', self)
        
      
        btn = QPushButton('Definir tabuleiro', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.buttonClicked)
        
        btn1 = QPushButton('Gerar tabuleiro aleatório', self)
        btn1.resize(btn.sizeHint())
        btn1.clicked.connect(self.gerarMatriz)
        
        btn2 = QPushButton('Rodar algoritmo', self)
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(self.rodarAlgoritmo)

        btn3 = QPushButton('Proximo passo', self)
        btn3.resize(btn.sizeHint())
        btn3.clicked.connect(self.proximaMatriz)
        
        btn4 = QPushButton('Rodar algoritmo bruto', self)
        btn4.resize(btn.sizeHint())
        btn4.clicked.connect(self.rodarAlgoritmoBruto)
        
        btn5 = QPushButton('Proxima soma', self)
        btn5.resize(btn.sizeHint())
        btn5.clicked.connect(self.proximaSoma)
        
        
        #grid.addWidget(titulo, 0,1)

        
        self.createTable(4,4)
        

        grid1.addWidget(lbl1, 1, 0)
        grid1.addWidget(self.n, 1, 1)
        grid1.addWidget(lbl2, 2, 0)
        grid1.addWidget(self.m, 2, 1)
        
        
        grid2.addWidget(btn, 0, 0)
        grid2.addWidget(btn1, 1, 0)
        
        grid3.addLayout(grid1,0,0)
        grid3.addLayout(grid2,1,0)
        
        
        grid4.addLayout(grid3,0,0)
        grid4.addWidget(self.tableWidget, 0, 1)
        
        grid5.addWidget(btn4,0,0)
        grid5.addWidget(btn5,0,1)
        
        grid6.addWidget(self.soma,0,0)
        grid6.addWidget(igual,0,1)
        grid6.addWidget(self.s1,0,2)
        grid6.addWidget(mais,0,3)
        grid6.addWidget(self.s2 ,0,4)
        
        grid7.addLayout(grid5,0,0)
        grid7.addLayout(grid6,1,0)
        
        grid8.addWidget(btn2,0,0)
        grid8.addWidget(btn3,1,0)
        
        grid9.addLayout(grid8,0,0)
        grid9.addWidget(self.resultado,0,1)
        
        grid10.addWidget(titulo,0,0)
        grid10.addWidget(configura,1,0)
        grid10.addLayout(grid4,2,0)
        grid10.addWidget(bruto,3,0)
        grid10.addLayout(grid7,4,0)
        grid10.addWidget(pd,6,0)
        grid10.addLayout(grid9,7,0)
        
        self.setLayout(grid10)
        
        self.setWindowTitle('Trabalho de PAA')
        self.show()

    def buttonClicked(self):
        b = self.tableWidget.rowCount()
        a = self.tableWidget.columnCount()
        for i in range(b):
            for j in range(b):
                self.tableWidget.removeRow(j)
                self.resultado.removeRow(j)
        for i in range(a):
            for j in range(a):
                self.tableWidget.removeColumn(j)
                self.resultado.removeColumn(j)
        tam = int(self.n.text())
        for i in range(tam):
            self.tableWidget.insertRow(i)
            self.resultado.insertRow(i)
        tam = int(self.m.text())
        for i in range(tam):
            self.tableWidget.insertColumn(i)
            self.resultado.insertColumn(i)
        self.zerarResultado()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.resultado.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    def zerarResultado(self):
        linha = self.resultado.rowCount()
        coluna = self.resultado.columnCount()
        for i in range(linha):
            for j in range(coluna):
                self.led = QLineEdit(str(0))
                self.item = QTableWidgetItem(self.led.text())
                self.resultado.setItem(i, j, self.item )
        
            
    def getMatriz(self):
        linha = self.tableWidget.rowCount()
        coluna = self.tableWidget.columnCount()
        self.matriz= []
        for i in range(linha):
            l = []
            for j in range(coluna):
                l.append(self.tableWidget.item(i,j).text())
            self.matriz.append(l)

    def gerarMatriz(self):
        linha = self.tableWidget.rowCount()
        coluna = self.tableWidget.columnCount()
        self.matriz = definir_tabuleiro(linha,coluna)
        for i in range(linha):
            for j in range(coluna):
                self.led = QLineEdit(str(self.matriz[i][j]))
                self.item = QTableWidgetItem(self.led.text())
                self.tableWidget.setItem(i, j, self.item )


    def rodarAlgoritmo(self):
        self.getMatriz()
        self.corT = [0,0]
        self.fMatriz = algoritmo(self,self.tableWidget.rowCount(),self.tableWidget.columnCount())
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Alerta")
        dlg.setIcon(QMessageBox.Information)
        dlg.setText("Algoritmo já rodou.\nVocê já pode ver o 1 passo.")
        dlg.exec_()
    
    def rodarAlgoritmoBruto(self):
        self.getMatriz()
        linha = self.tableWidget.rowCount()
        coluna = self.tableWidget.columnCount()
        m = caminhar(self,self.matriz,linha,coluna,linha,coluna)
        self.setVetorSomas(m)
        self.corT = [-1,-1]
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Alerta")
        dlg.setIcon(QMessageBox.Information)
        dlg.setText("Algoritmo já rodou.\nVocê já pode ver o 1 passo.")
        dlg.exec_()

    def setColoracaoR(self,colora):
        self.coloracaoR = colora

    def setColoracaoR1(self,colora):
        self.coloracaoR1 = colora
        
    def setColoracaoT(self,colora):
        self.coloracaoT = colora
    
    def setVetorBruto(self,m):
        self.vetoresBruto.append(m)
        
    def setVetorVolta(self,m):
        self.vetorVolta.append(m)
        
    def setVetorSomas(self,s):
        self.vetorSomas.append(s)
        
    def proximaSoma(self):
        if(len(self.vetoresBruto) != 0):
            if(self.corT[0] != -1):
                self.tableWidget.item(self.corT[0],self.corT[1]).setBackground(QColor(100 ,100 ,100))
            self.corT = self.vetoresBruto.pop(0)
            self.tableWidget.item(self.corT[0],self.corT[1]).setBackground(QColor(173 ,255 ,47))
        if(len(self.vetorSomas) != 0):
            somaA = self.vetorSomas.pop(0)
            self.s2.setText(self.tableWidget.item(self.corT[0],self.corT[1]).text())
            self.s1.setText(str(somaA))
            a = int(somaA) + int(self.tableWidget.item(self.corT[0],self.corT[1]).text())
            self.soma.setText(str(a))
        else:
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Alerta")
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("Ultima soma já realizado")
            dlg.exec_()
        
        
    def proximaMatriz(self):
        if(len(self.fMatriz) != 0):
            self.tableWidget.item(self.corT[0],self.corT[1]).setBackground(QColor(255 ,255 ,255))
            linha = self.resultado.rowCount()
            coluna = self.resultado.columnCount()
            self.matriz = self.fMatriz.pop(0)
            self.corR = self.coloracaoR.pop(0)
            self.corR1 = self.coloracaoR1.pop(0)
            self.corT = self.coloracaoT.pop(0)
            for i in range(linha):
                for j in range(coluna):
                    self.led = QLineEdit(str(self.matriz[i][j]))
                    self.item = QTableWidgetItem(self.led.text())
                    self.resultado.setItem(i, j, self.item )
                    
            self.resultado.item(self.corR[0],self.corR[1]).setBackground(QColor(self.corR[2] ,self.corR[3] ,self.corR[4]))
            self.resultado.item(self.corR1[0],self.corR1[1]).setBackground(QColor(self.corR1[2] ,self.corR1[3] ,self.corR1[4]))
            self.tableWidget.item(self.corT[0],self.corT[1]).setBackground(QColor(self.corT[2] ,self.corT[3] ,self.corT[4]))
        else:
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Alerta")
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("Ultimo passo já realizado")
            dlg.exec_()
        
        
    def createTable(self,n,m):
        self.tableWidget = QTableWidget()
        self.resultado = QTableWidget()
        self.tableWidget.setRowCount(n)
        self.resultado.setRowCount(n)
        self.tableWidget.setColumnCount(m)
        self.resultado.setColumnCount(m)
        self.zerarResultado()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.resultado.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Geral()
    sys.exit(app.exec_())

