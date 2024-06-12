from PyQt5 import QtWidgets
import sys
from combo_box import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        combo = self.ui.cbCities
        
        # combo.addItem('Ankara')
        # combo.addItem('Istanbul')
        # combo.addItem('Izmir')
        # combo.addItems(['Kocaeli', 'Adanda'])
        
        self.ui.btnLoad.clicked.connect(self.LoadItems)
        self.ui.btnGet.clicked.connect(self.GetItems)
        self.ui.btnClear.clicked.connect(self.ClearItems)

        
        self.ui.cbCities.currentIndexChanged.connect(self.SelectedChangedIndex)
        self.ui.cbCities.currentIndexChanged[str].connect(self.SelectedChangedText)
    
    def ClearItems(self):
        self.ui.cbCities.clear()

    def SelectedChangedText(self, text):
        print(text)

    def SelectedChangedIndex(self, index):
        print(index)
        
    def GetItems(self):
        print(self.ui.cbCities.currentText())
        print(self.ui.cbCities.currentIndex())
        
        count = self.ui.cbCities.count()
        for index in range(count):
            print(self.ui.cbCities.itemText(index)) # Verdiğimiz index numarasında olan texti bize getirir.
        
    def LoadItems(self):
        cities = ['Adana', 'Edirne', 'Rize']
        
        self.ui.cbCities.addItems(cities)
        
        


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
    
app()