import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)     # Komut bilgisi aktarıldı
    win = QMainWindow()

    
    win.setWindowTitle('First App')  # Uygulamanın başlığı
    win.setGeometry(200,200,500,500) # Uygulamanın boyutu
    win.setWindowIcon(QIcon("C:/Users/SefaPc/Desktop/btkPythonL/21_PyQt5/dicon.png")) # Icon ekleme
    win.setToolTip('My Tooltip')     # Mouse üzerine gelindiğinde gösterir
    
    lbl_name = QtWidgets.QLabel(win) # Pencere içerisine label ekledik
    lbl_name.setText('Name: ')
    lbl_name.move(50,30)
    
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Surname: ')
    lbl_surname.move(50,70)
    
    txt_name = QtWidgets.QLineEdit(win) # Kimin objesi olduğunu yaz win
    txt_name.move(150,30)
    
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)
    
    def clicked(self):
        print('Clicked. Name: ' + txt_name.text() + ', Surname: ' + txt_surname.text() + ' ' + 'Saved!')
        
    
    btn_save = QtWidgets.QPushButton(win)
    btn_save.move(150,110)
    btn_save.setText('Save')
    
    btn_save.clicked.connect(clicked) # click özelliğine bir fonksiyon atadık
    
    
    
    win.show()                       # Pencereyi göster
    sys.exit(app.exec_())            # Çarpı ikonuna basılmasıyla durdurur
        
    
window()

# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar



