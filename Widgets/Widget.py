from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect
from PySide6.QtCore import QRect, QPropertyAnimation,Qt

class Line(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("line")
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground,True)

        self.setStyleSheet("""#line {
                           background-color : #BBE0EF;
                           border: 2px solid #BBE0EF;
                           border-radius: 2px;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(self.parent.width() // 2,self.parent.height() * 0.05,0,4))
        self.anim.setEndValue(QRect(0,self.parent.height() * 0.05, self.parent.width(),4))
        self.anim.start()
