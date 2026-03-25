from PySide6.QtWidgets import QWidget,QPushButton,QGridLayout,QScrollArea,QVBoxLayout,QSizePolicy,QHBoxLayout
from Widgets.myButton import Button
from PySide6.QtCore import Qt


class HiraganaPage(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setObjectName("hP")
        self.setWindowTitle("Basic Hiragana")
        self.setStyleSheet("#hP{background-color : #355872}")

        self.header = QWidget()
        self.header.setAttribute(Qt.WA_StyledBackground,True)
        self.header.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.header.setStyleSheet("background-color:transparent;")
        self.header.setFixedHeight(self.height()* 0.1)
        self.headerLayout = QHBoxLayout(self.header)
        self.headerLayout.addWidget(self.parent.childText,alignment=Qt.AlignCenter)




        self.QLayout = QVBoxLayout(self)
        self.QLayout.addWidget(self.header)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.container.setStyleSheet("background-color:#355872")
        self.layout = QGridLayout(self.container)
        self.scroll.setWidget(self.container)
        self.QLayout.addWidget(self.scroll)

        self.hiragana  = [
            
        ["あ\na","い\ni","う\nu","え\ne","お\no"],
        ["か\nka","き\nki","く\nku","け\nke","こ\nko"],
        ["さ\nsa","し\nshi","す\nsu","せ\nse","そ\nso"],
        ["た\nta","ち\nchi","つ\ntsu","て\nte","と\nto"],
        ["な\nna","に\nni","ぬ\nnu","ね\nne","の\nno"],
        ["は\nha","ひ\nhi","ふ\nfu","へ\nhe","ほ\nho"],
        ["ま\nma","み\nmi","む\nmu","め\nme","も\nmo"],
        [" ","や\nya","ゆ\nyu","よ\nyo"," "],
        ["ら\nra","り\nri","る\nru","れ\nre","ろ\nro"],
        [" ","わ\nwa","を\nwo","ん\nn"," "]
            
        ]

        self.buttons = []

        for iRow,data in enumerate(self.hiragana):
            for iCol,char in enumerate(data):
                if char != " ":
                    self.btn = Button(char,self)
                    self.layout.addWidget(self.btn,iRow,iCol)
                    self.buttons.append(char)



