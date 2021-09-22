from PyQt5.QtWidgets import QMainWindow, QMenu, QMenuBar, QToolBar, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from typing import Dict, List

from src.view.menu.entry_menu import EntryMenu


class MenuBar:

    _menu_names: List[str] = [  '&accounting entry', '&selection', '&graphics', 
                                '&settings', '&about']

    def __init__(self,  parent: QMainWindow) -> None:
        self._parent: QMainWindow = parent
        self._place_menu_bar()
        self._add_menu()
        EntryMenu(self._parent, self._menus[MenuBar._menu_names[0]], 
                    MenuBar._menu_names[0])

    def _place_menu_bar(self) -> None:
        self._menu_bar = QMenuBar(self._parent)
        self._parent.setMenuBar(self._menu_bar)
            
    def _add_menu(self) -> None:
        self._menus: Dict[str, QMenu] = {}
        for name in MenuBar._menu_names:
            self._menus[name] = QMenu(name,self._parent)
            self._menu_bar.addMenu(self._menus[name])
