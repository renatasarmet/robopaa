import sys
import time
from PyQt5.QtWidgets import (QMainWindow,QWidget, QToolTip, QMessageBox,
    QPushButton,QLabel,QLineEdit,QGridLayout,QTextEdit,QTableWidgetItem,QLineEdit,QTableWidget,QVBoxLayout,
                             QApplication)
from PyQt5.QtGui import QFont,QColor
from random import randint
import copy


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
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        grid = QGridLayout()
        grid.setVerticalSpacing(1)
        
        lbl1 = QLabel('Digite o valor n do tabuleiro:', self)
        self.n = QLineEdit()

        lbl2 = QLabel('Digite o valor m do tabuleiro:', self)
        self.m = QLineEdit()

        lbl3 = QLabel('Tabuleiro Original:', self)
        lbl4 = QLabel('Resultado', self)
        
        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(self.n, 1, 1)
        grid.addWidget(lbl2, 2, 0)
        grid.addWidget(self.m, 2, 1)
        
        
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
        
        grid.addWidget(btn, 4, 0)
        grid.addWidget(btn1, 4, 1)
        grid.addWidget(btn2, 4, 2)
        grid.addWidget(btn3, 4, 3)
        self.createTable(2,2)
        grid.addWidget(lbl3,5,0)
        grid.addWidget(lbl4,5,1)
        grid.addWidget(self.tableWidget,6,0)
        grid.addWidget(self.resultado,6,1) 
        self.setLayout(grid)
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

    def setColoracaoR(self,colora):
        self.coloracaoR = colora

    def setColoracaoR1(self,colora):
        self.coloracaoR1 = colora
        
    def setColoracaoT(self,colora):
        self.coloracaoT = colora
        
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
 
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Geral()
    sys.exit(app.exec_())

