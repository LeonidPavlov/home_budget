

from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt
import typing

class WidgetInCenter:
    def __init__(self, parent: QMainWindow) -> None:
        self.label: QLabel = QLabel('<h1>EBAT COLOTIT</h1>')
        parent.setCentralWidget(self.label)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    
    def set_text(self, text: str = 'default') -> None:
        self.label.setText(text) 
