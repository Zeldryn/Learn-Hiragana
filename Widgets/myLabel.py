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
            self.setText("Learn Hiragana Versi Demo")
            self.QFont.setPointSize(15)
            self.setFont(self.QFont)

            self.effect = QGraphicsOpacityEffect(self)
            self.setGraphicsEffect(self.effect)
            self.effect.setOpacity(0)
            
            self.anim = QPropertyAnimation(self.effect, b"opacity")
            self.anim.setDuration(2000)
            self.anim.setStartValue(0)
            self.anim.setEndValue(1)


