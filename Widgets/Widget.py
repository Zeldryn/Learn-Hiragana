from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect,QHBoxLayout,QPushButton
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
        self.anim.setStartValue(QRect(self.parent.width() // 2,0,0,self.parent.height() * 0.07))
        self.anim.setEndValue(QRect(-1,0, self.parent.width() + 1,self.parent.height() * 0.07))
        self.anim.finished.connect(self.Text)
        self.anim.start()

    
    def Text(self):
        self.QHBox.addWidget(self.text,alignment=Qt.AlignCenter)
        self.text.anim.start()

class Box1(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("Box1")
        self.parent = parent
        self.setStyleSheet("""#Box1 {
                           background-color:white;
                           border: 2px solid black;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.15,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.03,self.parent.height() * 0.12,self.parent.width() * 0.3, self.parent.height() * 0.8))
        self.anim.start()

class Box2(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("Box1")
        self.parent = parent
        self.setStyleSheet("""#Box1 {
                           background-color:white;
                           border: 2px solid black;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.15,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.35,self.parent.height() * 0.12,self.parent.width() * 0.3, self.parent.height() * 0.8))
        self.anim.start()

class Box3(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("Box1")
        self.parent = parent
        self.setStyleSheet("""#Box1 {
                           background-color:white;
                           border: 2px solid black;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.15,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.67,self.parent.height() * 0.12,self.parent.width() * 0.3, self.parent.height() * 0.8))
        self.anim.start()


