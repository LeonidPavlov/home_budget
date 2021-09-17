from typing import List, Dict
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QMainWindow, QMenu, QToolBar

from resources import qrc_resources
from src.view.menu.synced_actions import SyncedActions
from src.view.central_widget import WidgetInCenter
              

class EntryMenu:

    _action_params: List[List[str]] = [ 
        ['&new entry', '&edit entry', '&search entry'], 
        [':entry', ':edit', ':search'], 
        ['Ctrl+N', 'Ctrl+E', 'Ctrl+A']
    ]
    @staticmethod
    def huy_tebe() -> None:
        print('huy tebe')

    def __init__(self, parent: QMainWindow, menu: QMenu,
                        menu_name: str, central_widget: WidgetInCenter) -> None:
        self._parent: QMainWindow = parent
        self._menu: QMenu = menu
        self._menu_name = menu_name
        self._create_widget = central_widget
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
        self._actions[0].triggered.connect(self._entry_action_precced)

    @staticmethod
    def _entry_action_precced() -> None:
        print('ebat colotit')