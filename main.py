from PySide6.QtWidgets import QWidget,QApplication, QGraphicsOpacityEffect
from Widgets.myButton import Button
from Widgets.Widget import Header,Box1,Box2,Box3
from Widgets.myLabel import Label
from PySide6.QtCore import QRect, QPropertyAnimation,QTimer


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.outsideWidget = False
        self.setObjectName("Main")
        self.setWindowTitle("Learn Hiragana")
        self.getWidthMonitor = self.screen().availableGeometry().width()
        self.getHeightMonitor = self.screen().availableGeometry().height()
        self.move(0,0,)
        self.resize(self.getWidthMonitor,self.getHeightMonitor)
        self.setStyleSheet("""#Main {
                           background-color: white}""")
        self.Btn1 = Box1(self)
        self.Btn2 = Box2(self)
        self.Btn3 = Box3(self)

        self.headLabel = Label("headLabel",self)
        self.Header = Header(self,self.headLabel)
        self.ownerShip = Label("ownerShip",self)

        self.bMode = Label("bMode",self)
        self.vMode = Label("vMode",self)
        self.cMode = Label("cMode",self)


        self.Header.setParent(self)
        self.Header.show()

        self.bMode.setParent(self)
        self.bMode.show()
        self.Btn1.setParent(self)
        self.Btn1.show()

        self.vMode.setParent(self)
        self.vMode.show()
        self.Btn2.setParent(self)
        self.Btn2.show()

        self.cMode.setParent(self)
        self.cMode.show()
        self.Btn3.setParent(self)
        self.Btn3.show()

        self.ownerShip.setParent(self)
        self.ownerShip.move(self.width() * 0.015,self.height() * 0.95)
        self.ownerShip.anim.start()
    
    # def enterEvent(self,event):
    #     QApplication.exit()




app = QApplication([])
window = Main()
window.show()
app.exec()