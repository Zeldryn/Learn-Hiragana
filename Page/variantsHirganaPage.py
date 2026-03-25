from PySide6.QtWidgets import QWidget,QPushButton,QGridLayout,QScrollArea,QVBoxLayout,QSizePolicy,QHBoxLayout
from Widgets.myButton import Button
from PySide6.QtCore import Qt


class variantsHiraganaPage(QWidget):
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
        ["が\nga","ぎ\ngi","ぐ\ngu","げ\nge","ご\ngo"],
        ["ざ\nza","じ\nji","ず\nzu","ぜ\nze","ぞ\nzo"],
        ["だ\nda","ぢ\nji","づ\nzu","で\nde","ど\ndo"],
        ["ば\nba","び\nbi","ぶ\nbu","べ\nbe","ぼ\nbo"],
        ["ぱ\npa","ぴ\npi","ぷ\npu","ぺ\npe","ぽ\npo"]
       ]

        self.buttons = []

        for iRow,data in enumerate(self.hiragana):
            for iCol,char in enumerate(data):
                if char != " ":
                    self.btn = Button(char,self)
                    self.layout.addWidget(self.btn,iRow,iCol)
                    self.buttons.append(char)



