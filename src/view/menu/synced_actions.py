from typing import List
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidget


class SyncedActions:
    def __init__(self, params: List[List[str]], parent: QWidget) -> None:
        self._parent = parent
        self._headers: List[str] = params[0]
        self._icons: List[str] = params[1]
        self._shortcuts: List[str] = params[2]

    def actions_icon_header_shortcut(self) -> List[QAction]:
        actions: List[QAction] = []
        length: int = len(self._headers)
        for j in range(length):
            action: QAction = QAction(QIcon(self._icons[j]), 
                                            self._headers[j], self._parent)
            action.setShortcut(self._shortcuts[j])
            actions.append(action)
        return actions
