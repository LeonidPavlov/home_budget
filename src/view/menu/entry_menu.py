from typing import List, Dict
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMainWindow, QMenu, QToolBar

from resources import qrc_resources
              

class EntryMenu:

    _entry_action_names: List[str] = ['&new entry', '&edit entry',\
                                     '&search entry']
    
    def __init__(self, parent: QMainWindow, menu: QMenu,
                        menu_name: str) -> None:
        self._parent: QMainWindow = parent
        self._menu = menu
        self._menu_name = menu_name
        self._menu_actions()
        self._add_toolbar()

    def _menu_actions(self) -> None:
        self._actions: Dict[str, QAction] = {}
        for name in EntryMenu._entry_action_names:
            self._actions[name] = QAction(name, self._parent)
            self._menu.addAction(self._actions[name])

    def _add_toolbar(self) -> None:
        self._toolbar = QToolBar(self._menu_name, self._parent)
        self._parent.addToolBar(Qt.TopToolBarArea, self._toolbar)
        