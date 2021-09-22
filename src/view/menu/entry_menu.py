from typing import List, Dict
from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow, QMenu, QToolBar

from resources import qrc_resources
from src.view.menu.synced_actions import SyncedActions
              

class EntryMenu:

    _action_params: List[List[str]] = [ 
        ['&new entry', '&edit entry', '&search entry'], 
        [':entry', ':edit', ':search'], 
        ['Ctrl+N', 'Ctrl+E', 'Ctrl+A']
    ]

    def __init__(self,  parent: QMainWindow, menu: QMenu,\
                        menu_name: str) -> None:
        self._parent: QMainWindow = parent
        self._menu: QMenu = menu
        self._menu_name = menu_name
        self._create_actions()

    def _create_actions(self) -> None:
        sa: SyncedActions = SyncedActions(  EntryMenu._action_params, 
                                            self._parent)
        self._actions: List[QAction] = sa.actions_icon_header_shortcut()
        self._toolbar = QToolBar(self._menu_name, self._parent)
        for action in self._actions:
            self._menu.addAction(action)
            self._toolbar.addAction(action)
        self._toolbar.setHidden(True)
        self._toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self._parent.addToolBar(Qt.TopToolBarArea, self._toolbar)
        
        entryActions: EntryActions = EntryActions(self._parent)
        self._actions[0].triggered.connect(entryActions.mousePressEvent)


class EntryActions:
    def __init__(self, parent: QMainWindow) -> None:
        EntryActions.__parent: QMainWindow = parent

    @staticmethod
    def mousePressEvent(event: QEvent) -> None:
        EntryActions.__parent.changeCentralWidget(QLabel('<h2>ebanaftumba</h2>'))