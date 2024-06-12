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
    
    win.show()                       # Pencereyi göster
    sys.exit(app.exec_())            # Çarpı ikonuna basılmasıyla durdurur
    
    
    
    
window()




