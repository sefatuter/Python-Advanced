from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_UI_MainWindow
# pyuic5 C:\Users\SefaPc\Desktop\btkPythonL\21_PyQt5\MainWindow.ui -o MainWindow.py
# pyuic5 C:\Users\SefaPc\Desktop\btkPythonL\21_PyQt5\MainWindow.ui -o C:\Users\SefaPc\Desktop\btkPythonL\21_PyQt5\MainWindow.py # Alt Dosyaya kayıt için.
# komutu ile Designer uygulamasında kaydedilen düzenlenen UI kodda güncellenir.

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_UI_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSum.clicked.connect(self.calculate)
        self.ui.btnMinus.clicked.connect(self.calculate)
        self.ui.btnMult.clicked.connect(self.calculate)
        self.ui.btnDiv.clicked.connect(self.calculate)
        
        
    def calculate(self):
        sender = self.sender().text()
        result = 0
        
        if sender == '+':
            result = int(self.ui.txt_num1.text()) + int(self.ui.txt_num2.text())
        elif sender == '-':
            result = int(self.ui.txt_num1.text()) - int(self.ui.txt_num2.text())
        elif sender == '*':
            result = int(self.ui.txt_num1.text()) * int(self.ui.txt_num2.text())
        elif sender == '/':
            result = int(self.ui.txt_num1.text()) / int(self.ui.txt_num2.text())        
        
        self.ui.lbl_result.setText('Answer = ' + str(result))
        

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
    
    
app()