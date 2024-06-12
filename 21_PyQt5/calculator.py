import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()
    
    def initUI(self):
        
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText('Number 1: ')
        self.lbl_num1.move(50,30)
        
        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150,30)
        self.txt_num1.resize(200,32)       
        
        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText('Number 2: ')
        self.lbl_num2.move(50,80)
        
        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150,80)
        self.txt_num2.resize(200,32)       

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText('+')
        self.btn_sum.move(150,130)
        self.btn_sum.clicked.connect(self.calculate)
        
        self.btn_minus = QtWidgets.QPushButton(self)
        self.btn_minus.setText('-')
        self.btn_minus.move(250,130)
        self.btn_minus.clicked.connect(self.calculate)
        
        self.btn_mult = QtWidgets.QPushButton(self)
        self.btn_mult.setText('*')
        self.btn_mult.move(150,170)
        self.btn_mult.clicked.connect(self.calculate)
        
        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText('/')
        self.btn_div.move(250,170)
        self.btn_div.clicked.connect(self.calculate)
        
    
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Answer = ')
        self.lbl_result.move(150,200)


    # def sum(self):
    #     result = int(self.txt_num1.text()) + int(self.txt_num2.text())
    #     self.lbl_result.setText('Answer = ' + str(result))
    
    # def minus(self):
    #     result = int(self.txt_num1.text()) - int(self.txt_num2.text())
    #     self.lbl_result.setText('Answer = ' + str(result))
    
    # def mult(self):
    #     result = int(self.txt_num1.text()) * int(self.txt_num2.text())
    #     self.lbl_result.setText('Answer = ' + str(result))
    
    # def div(self):
    #     result = int(self.txt_num1.text()) / int(self.txt_num2.text())
    #     self.lbl_result.setText('Answer = ' + str(result))
    
    def calculate(self):
        sender = self.sender().text()
        result = 0
        
        if sender == '+':
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == '-':
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == '*':
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == '/':
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())        
        
        self.lbl_result.setText('Answer = ' + str(result))
    
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
    
    
app()