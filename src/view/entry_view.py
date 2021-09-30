from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from typing import Optional


class EntryView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        label = QLabel("EBAT NI EBATSA")
        self._layout = QVBoxLayout()
        self._layout.addWidget(label)
        self.setLayout(self._layout)
        print('constructor')
        
    def instance(self) -> QWidget:
        print('instance')
        return self
