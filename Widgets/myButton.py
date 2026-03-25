from PySide6.QtWidgets import QPushButton,QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl,QTimer

class Button(QPushButton):
    def __init__(self,char,parent):
        super().__init__()
        self.char = char.split("\n")[0].strip()
        self.parent = parent
        self.setText(char)
        self.count = 0
        self.setObjectName("btn")
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.QFont = QFont()
        self.QFont.setPointSize(30)
        self.setFont(self.QFont)
        self.setStyleSheet("""#btn {
                           background-color: #7AAACE;
                           color:white;
                           
                           }
                           
                           #btn:hover {
                            background-color: rgba(122, 170, 206, 0.5);
                           color:white;
                           
                           }""")

        self.clicked.connect(self.clickHandle)
        hiraganaToRomaji = {

            "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",


            "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",


            "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",


            "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",


            "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",


            "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",


            "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",


            "や": "ya", "ゆ": "yu", "よ": "yo",


            "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",


            "わ": "wa", "を": "wo",

            "ん": "n",

            #Variants
            "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",

            "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",

            "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",

            "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",

            "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",


        }
        
        romaji = hiraganaToRomaji.get(self.char)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setSource(QUrl.fromLocalFile(f"assets/audio/{romaji}.mp3"))

    def clickHandle(self):
        self.player.play()

        self.setStyleSheet("""#btn {
                    background-color: #7AAACE;
                    color:white;
                    border: 3px solid #9CD5FF;
                    border-radius: 5px;
                    
                    }
                    
                    #btn:hover {
                    background-color: rgba(122, 170, 206, 0.5);
                    color:white;
                    
                    }""")
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.changeBack)
        self.timer.start(1000)
        
    def changeBack(self):
        self.count += 1
        if self.count == 2:
            self.setStyleSheet("""#btn {
                    background-color: #7AAACE;
                    color:white;
                            
                        }
                        
                        #btn:hover {
                        background-color: rgba(122, 170, 206, 0.5);
                        color:white;
                        
                        }""")
            self.count = 0
            self.timer.stop()
        


