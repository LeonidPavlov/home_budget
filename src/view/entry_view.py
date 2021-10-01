from functools import partial
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction, QFormLayout, QLabel, QMainWindow, QWidget
from src.view.alert import Achtung

from src.model.transaction import AccountingEntry


class EntryView:
    def __init__(self,  parent: QMainWindow, entry: AccountingEntry) -> None:
        self.widget : QWidget = QWidget(parent)
        self.parent: QMainWindow = parent
        self.layout: QFormLayout  = QFormLayout()
        self._init_fields()
        self.widget.setLayout(self.layout)       
        self.parent.setCentralWidget(self.widget)

    def _init_fields(self) -> None:
        pass
