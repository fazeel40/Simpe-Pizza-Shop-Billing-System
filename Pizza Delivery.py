import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QInputDialog , QMessageBox
from PyQt5.uic import loadUi

class my_app(QMainWindow):
    def __init__(self):
        super(my_app,self).__init__()
        loadUi("Pizza_UI.ui",self)
        self.pizza_list.addItems(["Fajita","Perri","Makhan","Large"])
        self.button.clicked.connect(self.press_)
    def press_(self):
        index = self.pizza_list.currentIndex()
        item = self.pizza_list.itemText(index)
        self.chose_pizza.setText("You Picked "+item)
        
def window():
    app = QApplication(sys.argv)
    win = my_app()
    win.setWindowTitle("Pizza Delivery")
    win.show()
    sys.exit(app.exec_())
window()