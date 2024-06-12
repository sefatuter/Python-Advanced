import sys
from PyQt5 import QtWidgets
from check_box import Ui_MainWindow


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.cbCinema.stateChanged.connect(self.show_state) # seçim
        self.ui.cbRead.stateChanged.connect(self.show_state) # seçim
        self.ui.cbSport.stateChanged.connect(self.show_state) # seçim
        
        
        self.ui.btnTakeHobbies.clicked.connect(self.getAllHobbies)
        self.ui.btnTakeLessons.clicked.connect(self.getAllLessons)
        
    def getAllLessons(self):
        result = ''
        items = self.ui.groupLesson.findChildren(QtWidgets.QCheckBox) # Belirli bir şey altındaki itemleri alma
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
            
        self.ui.lblResultLessons.setText(result)
    
    
    
    def getAllHobbies(self):
        result = ''
        items = self.ui.groupHobbies.findChildren(QtWidgets.QCheckBox) # Belirli bir şey altındaki itemleri alma
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
            
        self.ui.lblResultHobbies.setText(result)
                
                # print(cb.text())
                # print(cb.isChecked())    
        
    def show_state(self, value):
        cb = self.sender()
        print(cb.text()) # Hangi checkbox'a tıklandıysa onun bilgisini alır
        print(cb.isChecked())
        
        # print(value)
        # print(self.ui.cbCinema.isChecked())
        # print(self.ui.cbCinema.text())
        

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
    
    
app()
