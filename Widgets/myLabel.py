from PySide6.QtWidgets import QLabel,QGraphicsOpacityEffect
from PySide6.QtCore import QRect, QPropertyAnimation,Qt
from PySide6.QtGui import QFont


class Label(QLabel):
    def __init__(self,id,parent):
        super().__init__()
        self.id = id
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.QFont = QFont()

        if self.id == "headLabel":
            self.setText("Learn Hiragana Demo Version")
            self.QFont.setPointSize(15)
            self.setFont(self.QFont)

            self.effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(self.effect)
            self.effect.setOpacity(0)
            
            self.anim = QPropertyAnimation(self.effect, b"opacity")
            self.anim.setDuration(2000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)


        elif self.id == "vMode":
            self.setText("Variants Mode")
            self.setObjectName("vModeMain")
            self.QFont.setPointSize(15)
            self.QFont.setItalic(True)
            self.setFont(self.QFont)
            self.setAlignment(Qt.AlignCenter)
            self.setStyleSheet("""#vModeMain {
                               background-color : transparent;
                               border: 2px solid #0992C2;
                               border-radius:5px;
                               }""")
            



            self.effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(self.effect)
            self.effect.setOpacity(0)
            
            self.anim = QPropertyAnimation(self.effect, b"opacity")
            self.anim.setDuration(200)
            self.anim.setStartValue(0)
            self.anim.finished.connect(self.textDrop)
            self.anim.setEndValue(1)

            self.animUp = QPropertyAnimation(self,b"geometry")
            self.animUp.setDuration(250)
            self.animUp.setStartValue(QRect(self.parent.width() * 0.43, self.parent.height() * 0.18,self.parent.width() *0.15,self.parent.height() * 0.05))
            self.animUp.setEndValue(QRect(self.parent.width() * 0.43, self.parent.height() * 0.09,self.parent.width() * 0.15,self.parent.height() * 0.05))
            self.animUp.finished.connect(self.textOut)



    def textDrop(self):
            self.animDrop = QPropertyAnimation(self,b"geometry")
            self.animDrop.setDuration(250)
            self.animDrop.setStartValue(QRect(self.parent.width() * 0.43, self.parent.height() * 0.09,self.parent.width() * 0.15,self.parent.height() * 0.05))
            self.animDrop.setEndValue(QRect(self.parent.width() * 0.43, self.parent.height() * 0.18,self.parent.width() *0.15,self.parent.height() * 0.05))
            self.animDrop.start()

            
    def textOut(self):
            self.animOut = QPropertyAnimation(self.effect, b"opacity")
            self.animOut.setDuration(200)
            self.animOut.setStartValue(1)
            self.animOut.setEndValue(0)
            self.animOut.start()

