from PySide6.QtWidgets import QWidget,QApplication, QGraphicsOpacityEffect
from Widgets.myButton import Button
from Widgets.Widget import Header
from Widgets.myLabel import Label
from PySide6.QtCore import QRect, QPropertyAnimation


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Main")
        self.getWidthMonitor = self.screen().availableGeometry().width()
        self.getHeightMonitor = self.screen().availableGeometry().height()
        self.move(0,0,)
        self.resize(self.getWidthMonitor,self.getHeightMonitor)
        self.setStyleSheet("""#Main {
                           background-color: #EBF4F6}""")
        self.firstBtn = Button("firstMode",self)
        self.headLabel = Label("headLabel",self)
        self.Header = Header(self,self.headLabel)

        self.Header.setParent(self)
        self.Header.show()


app = QApplication([])
window = Main()
window.show()
app.exec()