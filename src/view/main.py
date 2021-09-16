from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar,\
                            QToolBar, QWidget, QLabel, QMenu
from PyQt5.QtCore import Qt, left
import sys
import typing
import PyQt5.QtCore as QtCore

from src.storage.storage import Storage
from src.view.central_widget import WidgetInCenter
from src.view.menu.menu_bar import MenuBar


class Main(QMainWindow):
    def __init__(self, parent:  typing.Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        self._add_parameters()

    def _add_parameters(self) -> None:
        self.setWindowTitle('Home Budget')
        self.setGeometry(320, 180 ,1024 ,576)

        central_widget = WidgetInCenter(self)
        MenuBar(self, central_widget)

class App:
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        win = Main()
        win.show()
        sys.exit(app.exec_())
