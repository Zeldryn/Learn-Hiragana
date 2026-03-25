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
            self.setText("Learn Hiragana Version 1.0")
            self.QFont.setPointSize(15)
            self.setFont(self.QFont)

            self.effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(self.effect)
            self.effect.setOpacity(0)
            
            self.anim = QPropertyAnimation(self.effect, b"opacity")
            self.anim.setDuration(2000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)


        elif self.id == "ownerShip":
            self.setText("made by Ahmad Rizki")
            self.QFont.setPointSize(10)
            self.setFont(self.QFont)
            self.setStyleSheet("color: rgba(rgba(53, 88, 114, 0.6))")

            self.effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(self.effect)
            self.effect.setOpacity(0)
            
            self.anim = QPropertyAnimation(self.effect, b"opacity")
            self.anim.setDuration(1000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)

        elif self.id == "bMode":
            self.setText("Basic Hiragana")
            self.setObjectName("vModeMain")
            self.setGeometry(QRect(self.parent.width() * 0.03, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
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
            self.anim.setDuration(1000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)

            self.animUp = QPropertyAnimation(self, b"geometry")
            self.animUp.setDuration(300)
            self.animUp.setStartValue(QRect(self.parent.width() * 0.03, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
            self.animUp.setEndValue(QRect(self.parent.width() * 0.02, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))

            self.animDown = QPropertyAnimation(self, b"geometry")
            self.animDown.setDuration(300)
            self.animDown.setStartValue(QRect(self.parent.width() * 0.02, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))
            self.animDown.setEndValue(QRect(self.parent.width() * 0.03, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))


        elif self.id == "vMode":
            self.setText("Variants Hiragana")
            self.setObjectName("vModeMain")
            self.setGeometry(QRect(self.parent.width() * 0.35, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
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
            self.anim.setDuration(1000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)

            self.animUp = QPropertyAnimation(self, b"geometry")
            self.animUp.setDuration(300)
            self.animUp.setStartValue(QRect(self.parent.width() * 0.35, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
            self.animUp.setEndValue(QRect(self.parent.width() * 0.34, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))

            self.animDown = QPropertyAnimation(self, b"geometry")
            self.animDown.setDuration(300)
            self.animDown.setStartValue(QRect(self.parent.width() * 0.34, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))
            self.animDown.setEndValue(QRect(self.parent.width() * 0.35, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))

        elif self.id == "cMode":
            self.setText("Combinations Hiragana")
            self.setObjectName("vModeMain")
            self.setGeometry(QRect(self.parent.width() * 0.67, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
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
            self.anim.setDuration(1000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)

            self.animUp = QPropertyAnimation(self, b"geometry")
            self.animUp.setDuration(300)
            self.animUp.setStartValue(QRect(self.parent.width() * 0.67, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))
            self.animUp.setEndValue(QRect(self.parent.width() * 0.66, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))

            self.animDown = QPropertyAnimation(self, b"geometry")
            self.animDown.setDuration(300)
            self.animDown.setStartValue(QRect(self.parent.width() * 0.66, self.parent.height() * 0.17,self.parent.width() *0.32,self.parent.height() * 0.05))
            self.animDown.setEndValue(QRect(self.parent.width() * 0.67, self.parent.height() * 0.18,self.parent.width() *0.3,self.parent.height() * 0.05))


        elif self.id == "hBasicText":
            self.setText("Basic Hiragana")
            self.QFont.setPointSize(15)
            self.QFont.setItalic(True)
            self.setFont(self.QFont)
            self.setStyleSheet("color:white")

  
