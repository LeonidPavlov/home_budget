from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys
import typing

from src.view.menu.menu_bar import MenuBar


class Main(QMainWindow):

    def __init__(self, parent:  typing.Optional[QWidget] = None) -> None:
        super().__init__(parent=parent)
        self.__create_view()

    def __create_view(self) -> None:
        self.setWindowTitle('Home Budget')
        self.setGeometry(320, 180 ,1024 ,576)
        self.changeCentralWidget(QLabel('<h1>Default Text</h1>'))
        MenuBar(self)

    def changeCentralWidget(self, widget: QWidget) -> None:
        self.setCentralWidget(widget)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

class App:
    def __init__(self) -> None:
        app = QApplication(sys.argv)
        win = Main()
        win.show()
        sys.exit(app.exec_())
