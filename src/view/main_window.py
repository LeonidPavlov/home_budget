from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QKeySequence, QKeyEvent
from PyQt5.QtWidgets import QAction, QLabel, QMainWindow,\
                         QMenu, QMenuBar, QToolBar
from PyQt5.QtCore import Qt
from functools import partial

import qrc.qrc_resources as res
from src.view.entry_view import EntryView
from src.storage.crud import Crud
from src.model.transaction import AccountingEntry
from src.view.dialogs.confirmation import Confirmation

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setCentralWidget(QLabel('<h1>PLACEHOLDER</h1>'))
        # self.setMinimumSize(640, 360)
        self._add_menu_bar()
        self.set_dev_style()

    def _add_menu_bar(self) -> None:
        menu_bar: QMenuBar = QMenuBar(self)
        
        self.entry_menu = QMenu('&accounting entry', menu_bar)
        menu_bar.addMenu(self.entry_menu)
        
        self.search_menu = QMenu('&search entry', menu_bar)
        menu_bar.addMenu(self.search_menu)
        
        self._add_entry_toolbar()
        self.setMenuBar(menu_bar)

    def _add_entry_toolbar(self) -> None:
        toolbar: QToolBar = QToolBar('accounting entry', self)
        
        new_action: QAction = QAction(QIcon(':entry'), 'new', self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.\
                connect(partial(self._setup_entry_widget, AccountingEntry()))
        toolbar.addAction(new_action)
        self.entry_menu.addAction(new_action)

        search_action: QAction = QAction(QIcon(':search'), 'select', self)
        search_action.setShortcut(QKeySequence.SelectAll)
        search_action.triggered.connect(self._setup_search_widget)
        toolbar.addAction(search_action)
        self.search_menu.addAction(search_action)
         
        self.addToolBar(Qt.LeftToolBarArea, toolbar)
        # toolbar.setVisible(False)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def _setup_entry_widget(self, entry: AccountingEntry) -> None:
        EntryView(self, entry)
    
    def _setup_search_widget(self) -> None:
        print('search widget')
    
    def set_dev_style(self) -> None:
        self.setStyleSheet('''
            background-color: bisque;
            color: navy;
            border-color: navy;
            font-size: 14px;
            font-weight: 900;
        ''')

    def close_callback(self, event) -> None:
        print(event)
        self.close()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape:
            Confirmation(self, self.close_callback, 'Close App ? ...', True)
        super().keyPressEvent(event)        