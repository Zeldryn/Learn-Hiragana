from PySide6.QtWidgets import QWidget,QPushButton,QGridLayout,QScrollArea,QVBoxLayout,QSizePolicy,QHBoxLayout
from Widgets.myButton import Button
from PySide6.QtCore import Qt


class combinationsHiraganaPage(QWidget):
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

        self.hiragana = [
            ["きゃ\nkya","きゅ\nkyu","きょ\nkyo"," "," "],
            ["しゃ\nsha","しゅ\nshu","しょ\nsho"," "," "],
            ["ちゃ\ncha","ちゅ\nchu","ちょ\ncho"," "," "],
            ["にゃ\nnya","にゅ\nnyu","にょ\nnyo"," "," "],
            ["ひゃ\nhya","ひゅ\nhyu","ひょ\nhyo"," "," "],
            ["みゃ\nmya","みゅ\nmyu","みょ\nmyo"," "," "],
            ["りゃ\nrya","りゅ\nryu","りょ\nryo"," "," "],
            ["ぎゃ\ngya","ぎゅ\ngyu","ぎょ\ngyo"," "," "],
            ["じゃ\nja","じゅ\nju","じょ\njo"," "," "],
            ["びゃ\nbya","びゅ\nbyu","びょ\nbyo"," "," "],
            ["ぴゃ\npya","ぴゅ\npyu","ぴょ\npyo"," "," "]
        ]

        self.buttons = []

        for iRow,data in enumerate(self.hiragana):
            for iCol,char in enumerate(data):
                if char != " ":
                    self.btn = Button(char,self)
                    self.layout.addWidget(self.btn,iRow,iCol)
                    self.buttons.append(char)



