from PySide6.QtWidgets import QWidget,QApplication, QGraphicsOpacityEffect
from Widgets.myButton import Button
from Widgets.Widget import Line
from Widgets.myLabel import Label
from PySide6.QtCore import QRect, QPropertyAnimation
from PySide6.QtGui import QFontMetrics

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
        self.line = Line(self)


        
        self.metrics = QFontMetrics(self.headLabel.font())
        self.headLabel.setParent(self)
        self.headLabel.move((self.width() - self.metrics.horizontalAdvance(self.headLabel.text())) // 2 ,10)
        self.headLabel.show()


        self.line.setParent(self)
        self.line.anim.finished.connect(self.startAnimationText)
        self.line.show()

    def startAnimationText(self):
        self.headLabel.anim.start()

app = QApplication([])
window = Main()
window.show()
app.exec()