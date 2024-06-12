from PyQt5 import QtWidgets
import sys
from radio_button import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
#--*
        self.ui.radTR.setChecked(True) # Başlangıçta seçili olarak birini seçer
        self.ui.radHSchool.setChecked(True)
        
        self.ui.radTR.toggled.connect(self.onClickedCountry)
        self.ui.radGE.toggled.connect(self.onClickedCountry)
        self.ui.radNL.toggled.connect(self.onClickedCountry)
        self.ui.radGR.toggled.connect(self.onClickedCountry)
        
        self.ui.radHSchool.toggled.connect(self.onClickedEdu)
        self.ui.radCollege.toggled.connect(self.onClickedEdu)
        self.ui.radMaster.toggled.connect(self.onClickedEdu)
        self.ui.radPHD.toggled.connect(self.onClickedEdu)
        
        self.ui.btnCountry.clicked.connect(self.getSelectedCountry)
        self.ui.btnEducation.clicked.connect(self.getSelectedEdu)
        
    def onClickedCountry(self):
        rb = self.sender()
        if rb.isChecked():
            print('Selected radio button: ' + rb.text()) # Formda seçileni terminalde yazdırır

    def onClickedEdu(self):
        rb = self.sender()
        if rb.isChecked():
            print('Selected radio button: ' + rb.text()) # Formda seçileni terminalde yazdırır


    def getSelectedCountry(self):
        items = self.ui.groupBoxCountry.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblCountry.setText('Selected Country: ' + rb.text())
                
    def getSelectedEdu(self):
        items = self.ui.groupBoxEdu.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEducation.setText('Selected Education: ' + rb.text())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
    
app()