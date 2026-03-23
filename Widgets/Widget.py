from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect,QHBoxLayout
from PySide6.QtCore import QRect, QPropertyAnimation,Qt

class Header(QWidget):
    def __init__(self,parent,text):
        super().__init__()
        self.setObjectName("line")
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.QHBox = QHBoxLayout(self)
        self.text = text
        self.setStyleSheet("""#line {
                           background-color : transparent;
                           border: 2px solid transparent;
                           border-bottom: 2px solid #0992C2;
                           border-radius: 2px;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(self.parent.width() // 2,0,0,self.parent.height() * 0.05))
        self.anim.setEndValue(QRect(0,0, self.parent.width(),self.parent.height() * 0.05))
        self.anim.finished.connect(self.Text)
        self.anim.start()

    
    def Text(self):
        self.QHBox.addWidget(self.text,alignment=Qt.AlignCenter)
        self.text.anim.start()

