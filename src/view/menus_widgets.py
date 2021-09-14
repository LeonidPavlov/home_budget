from PyQt5.QtWidgets import QMainWindow, QMenu, QMenuBar

from src.view.central_widget import WidgetInCenter


class MenuWidgets:
    def __init__(self,  parent: QMainWindow, 
                        central_widget: WidgetInCenter) -> None:
        self._parent: QMainWindow = parent
        self._create_menu_bar()

    def _create_menu_bar(self) -> None:
        self.menu_bar: QMenuBar = QMenuBar(self._parent)
        self._parent.setMenuBar(self.menu_bar)
        edit: QMenu = self.menu_bar.addMenu('edit')
        create: QMenu = self.menu_bar.addMenu('create')
        help: QMenu = self.menu_bar.addMenu('help')
