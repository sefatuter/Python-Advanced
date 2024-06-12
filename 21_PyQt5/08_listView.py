from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from list_view import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Load Students
        self.loadStudents()
        
        # Add New Student
        self.ui.btnAdd.clicked.connect(self.addStudent)
        
        # Edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)
        
        # Delete Student
        self.ui.btnDelete.clicked.connect(self.deleteStudent)
        
        # Up
        self.ui.btnUp.clicked.connect(self.upStudent)
        
        # Down
        self.ui.btnDown.clicked.connect(self.downStudent)
        
        # Sort
        self.ui.btnSort.clicked.connect(self.sortStudents)
        
        # Exit
        self.ui.btnExit.clicked.connect(self.close)
        
        
    def close(self):
        quit()
        
    def sortStudents(self):
        self.ui.listItems.sortItems()
        
    def upStudent(self):
        index = self.ui.listItems.currentRow()
        
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)
    
    def downStudent(self):
        index = self.ui.listItems.currentRow()
        
        if index < self.ui.listItems.count() -1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)
        
        
    def deleteStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        
        if item is None:
            return
        
        q = QMessageBox.question(self, 'Remove Student!', 'Do you want to remove Student: {}'.format(item.text()), QMessageBox.Yes | QMessageBox.No)
        
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item
                        
    
    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        
        if item is not None:
            text, ok = QInputDialog.getText(self, 'Edit Student', 'New Student Name', QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
        
    def loadStudents(self):
        self.ui.listItems.addItems(['Ahmet', 'Ali', 'Veli'])
        self.ui.listItems.setCurrentRow(0)
        
    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        text, ok = QInputDialog.getText(self, 'Add Student', 'Enter Name')
        
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex, text)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
    
app()