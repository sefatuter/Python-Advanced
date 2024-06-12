from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from message_box import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):
        
        result = QMessageBox.question(self, 'Close Application', 'Are you sure ?', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        # Kısa yoldan result yapma aşağıdakilere alternatif
        
        if result == QMessageBox.Ok:
            print('Yes Clicked')
            QtWidgets.qApp.quit()
        else:
            print('No Clicked')       
        
        
        # msg = QMessageBox()
        
        # msg.setWindowTitle('Close Application?')
        # msg.setText('Are you sure?')
        # # msg.setIcon(QMessageBox.Question)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        
        # msg.setDefaultButton(QMessageBox.Cancel) # İlk açıldığında hangisi seçili olarak gelsin
        # msg.setDetailedText('Details....')      
        # msg.buttonClicked.connect(self.popup_button)
        
        
        # x = msg.exec_()
        
        # print(x)
    
    # def popup_button(self, i): # Tıklanılan butonu elde etme
    #     print(i.text())
        
    #     if i.text() == 'OK':
    #         print('Okey')
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel':
    #         print('Canceling...')
    #     elif i.text() == 'Ignore':
    #         print('Ignore....')    

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
    
app()