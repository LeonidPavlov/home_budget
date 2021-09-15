from PyQt5.QtWidgets import QMainWindow, QMenu, QMenuBar, QToolBar, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from typing import Dict

from src.view.central_widget import WidgetInCenter
import resources.qrc_resources


class MenuWidgets:

    _entry_actions_name: tuple = ('&new entry', '&select', '&update', 
                                    '&delete', '&hren znaet')
    _entry_actions: Dict[str, QAction] = {}


    def __init__(self,  parent: QMainWindow, 
                        central_widget: WidgetInCenter) -> None:
        self._parent: QMainWindow = parent
        self._create_actions()
        self._create_menu_bar()


    def _create_actions(self) -> None:
        self.new_action = QAction('&new',self._parent)
        self.edit_action = QAction('&edit',self._parent)
        self.delet_action = QAction('&delete',self._parent)
        self.update_action = QAction('&update',self._parent)
        
    def _create_menu_bar(self) -> None:
        self.menu_bar: QMenuBar = QMenuBar(self._parent)
        self._parent.setMenuBar(self.menu_bar)
        entry: QMenu = self.menu_bar.addMenu(QIcon(':entry.ico'), 'entry')
        for item in MenuWidgets._entry_actions_name:
            action: QAction = QAction(item, self._parent)
            MenuWidgets._entry_actions[item] = action
            entry.addAction(action) 

    def _create_tool_bars(self) -> None:
        edit_tool_bar: QToolBar = QToolBar('edit bar', self._parent)
        self._parent.addToolBar(Qt.TopToolBarArea, edit_tool_bar)

        create_tool_bar: QToolBar = QToolBar('create bar', self._parent)
        self._parent.addToolBar(Qt.LeftToolBarArea, create_tool_bar)

        help_tool_bar: QToolBar = QToolBar('help bar', self._parent)
        self._parent.addToolBar(Qt.RightToolBarArea, help_tool_bar)
            
