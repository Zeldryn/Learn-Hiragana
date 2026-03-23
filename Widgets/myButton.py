from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self,id,parent):
        super().__init__()
        self.id = id
        self.parent = parent

        if self.id == "firstMode":
            pass
