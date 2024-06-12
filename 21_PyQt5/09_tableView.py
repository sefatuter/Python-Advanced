from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from table_view import Ui_MainWindow
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)
        
    
    def doubleClick(self): # Çift tıklanan hücredeki bilgileri almaya yarar
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(), item.column(), item.text())
            
        # print(self.ui.tableProducts.selectedItems())
        
    
    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()
        
        
        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            print(rowCount)
            self.ui.tableProducts.insertRow(rowCount) # Yeni satırı ekler
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))
        
    
    def loadProducts(self):
        
        products = [
            {'name': 'Iphone 7', 'price': 3000},
            {'name': 'Iphone 8', 'price': 4000},
            {'name': 'Iphone X', 'price': 3000},
            {'name': 'Iphone 11', 'price': 15000}
        ]
        
        
        
        self.ui.tableProducts.setRowCount(len(products)) #  satır
        self.ui.tableProducts.setColumnCount(2) #  kolon
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name', 'Price'))
        self.ui.tableProducts.setColumnWidth(0,120)
        self.ui.tableProducts.setColumnWidth(1,100)
        
        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))

            rowIndex += 1
        # self.ui.tableProducts.setItem(0,0, QTableWidgetItem('Iphone 7')) # ilk satır ilk kolondaki eleman ne olsun 
        # self.ui.tableProducts.setItem(0,1, QTableWidgetItem('3000')) # ilk satır ilk kolondaki eleman ne olsun 
        # self.ui.tableProducts.setItem(1,0, QTableWidgetItem('Iphone 8')) # ilk satır ilk kolondaki eleman ne olsun 
        # self.ui.tableProducts.setItem(1,1, QTableWidgetItem('4000')) # ilk satır ilk kolondaki eleman ne olsun 
        # self.ui.tableProducts.setItem(2,0, QTableWidgetItem('Iphone X')) # ilk satır ilk kolondaki eleman ne olsun 
        # self.ui.tableProducts.setItem(2,1, QTableWidgetItem('6000')) # ilk satır ilk kolondaki eleman ne olsun 
        
        
        
        
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
    
app()