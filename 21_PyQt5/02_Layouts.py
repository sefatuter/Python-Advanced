import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)
        
        # layout = QtWidgets.QVBoxLayout() # Vertical layout
        # layout = QtWidgets.QHBoxLayout()   # Horizontal layout
        
        
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))
        
    #---*
        
        # hlayout1 = QtWidgets.QHBoxLayout()
        # hlayout1.addWidget(Color('green'))
        # hlayout1.addWidget(Color('blue'))
        # hlayout1.addWidget(Color('red'))

        
        # hlayout2 = QtWidgets.QHBoxLayout()
        # hlayout2.addWidget(Color('red'))
        # hlayout2.addWidget(Color('green'))

        
        # vlayout = QtWidgets.QVBoxLayout()
        # vlayout.addLayout(hlayout1)
        # vlayout.addLayout(hlayout2)
        
    #---* 
        
        # layout = QtWidgets.QGridLayout()
        
        # layout.addWidget(Color('green'), 0, 0)
        # layout.addWidget(Color('blue'), 1, 0) # ilk parametre aşağı doğru, ikinci sağa doğru
        # layout.addWidget(Color('red'), 0, 2)
        # layout.addWidget(Color('yellow'), 3, 2)
                
    #---*
        
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color('green'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('red'))
        # hlayout1.setSpacing(50) # her eleman arasına boşluk bırakır
        # hlayout1.setContentsMargins(30,20,0,30) # soldan, yukarıdan, sağdan ve aşağıdan boşluk bırakma
        
        
        widget = QWidget()
        widget.setLayout(hlayout1)
        
        # widget = Color('green')
        self.setCentralWidget(widget)
        

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
app()