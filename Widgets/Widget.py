from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect,QHBoxLayout,QPushButton
from PySide6.QtCore import QRect, QPropertyAnimation,Qt,QTimer

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
        self.count = 0
        self.parent = parent
        self.setStyleSheet("""#Box1 {
                           background-image: url(assets/image/hiraganaImage.jpg);
                           background-repeat: no-repeat;
                           background-position:bottom;
                           border: 2px solid #0992C2;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.15,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.03,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim.finished.connect(self.textIn)
        self.anim.start()

    def textIn(self):
        self.parent.bMode.anim.start()

    def enterEvent(self,event):
        self.setCursor(Qt.PointingHandCursor)
        self.anim1 = QPropertyAnimation(self, b"geometry")
        self.anim1.setDuration(200)
        self.anim1.setStartValue(QRect(self.parent.width() * 0.03,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim1.setEndValue(QRect(self.parent.width() * 0.02,self.parent.height() * 0.25,self.parent.width() * 0.32, self.parent.height() * 0.68))
        self.anim1.start()
        self.parent.bMode.animUp.start()

    def leaveEvent(self,event):
        self.setCursor(Qt.ArrowCursor)
        self.anim2 = QPropertyAnimation(self, b"geometry")
        self.anim2.setDuration(200)
        self.anim2.setStartValue(QRect(self.parent.width() * 0.02,self.parent.height() * 0.25,self.parent.width() * 0.32, self.parent.height() * 0.68))
        self.anim2.setEndValue(QRect(self.parent.width() * 0.03,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim2.start()

        self.parent.bMode.animDown.start()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.BusyCursor)
            self.timer = QTimer()
            self.timer.timeout.connect(self.countTime)
            self.timer.start(500)

    def countTime(self):
        self.count += 1
        if self.count == 1:
            self.setCursor(Qt.ArrowCursor)
            self.count = 0


class Box2(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("Box2")
        self.parent = parent
        self.setStyleSheet("""#Box2 {
                           background-image: url(assets/image/gaImage.png);
                           background-repeat: no-repeat;
                           background-position:bottom;
                           border: 2px solid #0992C2;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.45,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.35,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim.finished.connect(self.textIn)
        self.anim.start()

    def textIn(self):
        self.parent.vMode.anim.start()
        
    def enterEvent(self,event):
        self.anim1 = QPropertyAnimation(self, b"geometry")
        self.anim1.setDuration(300)
        self.anim1.setStartValue(QRect(self.parent.width() * 0.35,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim1.setEndValue(QRect(self.parent.width() * 0.34,self.parent.height() * 0.25,self.parent.width() * 0.32,self.parent.height() * 0.68))
        self.anim1.start()

        self.parent.vMode.animUp.start()
        
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self,Event):
        self.anim2 = QPropertyAnimation(self, b"geometry")
        self.anim2.setDuration(300)
        self.anim2.setStartValue(QRect(self.parent.width() * 0.34,self.parent.height() * 0.25,self.parent.width() * 0.32,self.parent.height() * 0.68))
        self.anim2.setEndValue(QRect(self.parent.width() * 0.35,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim2.start()
        self.setCursor(Qt.ArrowCursor)
        self.parent.vMode.animDown.start()


class Box3(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setObjectName("Box3")
        self.parent = parent
        self.setStyleSheet("""#Box3 {
                           background-image: url(assets/image/paImage.png);
                           background-repeat: no-repeat;
                           background-position:bottom;
                           border: 2px solid #0992C2;
                           border-radius: 5px ;
                           }""")
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(self.parent.width() * 0.75,self.parent.height() * 0.4,0,0))
        self.anim.setEndValue(QRect(self.parent.width() * 0.67,self.parent.height() * 0.26,self.parent.width() * 0.3, self.parent.height() * 0.66))
        self.anim.finished.connect(self.textIn)
        self.anim.start()


    def textIn(self):
        self.parent.cMode.anim.start() 
    def enterEvent(self,event):
        self.setCursor(Qt.PointingHandCursor)
        self.anim1 = QPropertyAnimation(self, b"geometry")
        self.anim1.setDuration(200)
        self.anim1.setStartValue(QRect(self.parent.width() * 0.67,self.parent.height() * 0.26,self.parent.width() * 0.30, self.parent.height() * 0.66))
        self.anim1.setEndValue(QRect(self.parent.width() * 0.66,self.parent.height() * 0.25,self.parent.width() * 0.32, self.parent.height() * 0.68))
        self.anim1.start()

        self.parent.cMode.animUp.start()

    def leaveEvent(self,event):
        self.setCursor(Qt.ArrowCursor)
        self.anim2 = QPropertyAnimation(self, b"geometry")
        self.anim2.setDuration(200)
        self.anim2.setStartValue(QRect(self.parent.width() * 0.66,self.parent.height() * 0.25,self.parent.width() * 0.32, self.parent.height() * 0.68))
        self.anim2.setEndValue(QRect(self.parent.width() * 0.67,self.parent.height() * 0.26,self.parent.width() * 0.30, self.parent.height() * 0.66))
        self.anim2.start()

        self.parent.cMode.animDown.start()

